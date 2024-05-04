import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from PIL import Image, ImageTk

# Load the Parkinson's disease dataset
parkinsons_data = pd.read_csv('parkinsons.csv')

# Save the column names
column_names = parkinsons_data.columns.tolist()

# Check and convert columns to numeric if needed
numeric_columns = [
    'MDVP:Fo(Hz)',
    'MDVP:Fhi(Hz)',
    'MDVP:Flo(Hz)',
    'MDVP:Jitter(%)',
    'MDVP:Jitter(Abs)',
    'MDVP:RAP',
    'MDVP:PPQ',
    'Jitter:DDP',
    'MDVP:Shimmer',
    'MDVP:Shimmer(dB)',
    'Shimmer:APQ3',
    'Shimmer:APQ5',
    'MDVP:APQ',
    'Shimmer:DDA',
    'NHR',
    'HNR',
    'status',
    'RPDE',
    'DFA',
    'spread1',
    'spread2',
    'D2',
    'PPE'
]

for column in numeric_columns:
    parkinsons_data[column] = pd.to_numeric(parkinsons_data[column], errors='coerce')

# Split the dataset into features (X) and target (Y)
X = parkinsons_data.drop(columns=['name', 'status'], axis=1)
Y = parkinsons_data['status']

# Standardize the features
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

# Create a Support Vector Machine (SVM) classifier with a linear kernel
model = svm.SVC(kernel='linear')
model.fit(X, Y)


# Define a function to predict Parkinson's Disease
def predict_parkinsons():
    # Get input data from the text box
    input_data_text = input_data_entry.get("1.0", "end-1c").strip()

    # Check if input data is empty
    if not input_data_text:
        messagebox.showerror("Error", "Please enter input data.")
        return

    # Convert input data to a list of float values
    input_data = [float(val) for val in input_data_text.split(",")]

    # Standardize the input data
    std_data = scaler.transform([input_data])

    # Make predictions for the input data
    prediction = model.predict(std_data)

    # Display the prediction result
    if prediction[0] == 0:
        result_label.config(text="The person does not have Parkinson's Disease",foreground='green')
    else:
        result_label.config(text="The person has Parkinson's Disease",foreground='red')


# Create the main GUI window
root = tk.Tk()
root.title("Parkinson's Disease Prediction")
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
# Set the window size and position it in the center of the screen
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Load and display a background image
bg_image = Image.open('background.jpg')  # Change 'background_image.jpg' to your image file
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = ttk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)
bg_label.image = bg_photo
content_label = ttk.Label(root, text="Parkinson's Disease Predection", font=("Copperplate Gothic Bold", 20),foreground="blue")
content_label.pack(pady=20)



content_text = """Parkinson's disease is a neurodegenerative disorder that affects movement control. One of the motor symptoms of Parkinson's disease is tremors, which can manifest as a characteristic spiral drawing pattern when a person attempts to draw a spiral shape, such as a circle. The spiral drawing test is a common clinical tool used to assess the severity of tremors and motor dysfunction in individuals suspected of having Parkinson's disease.

Here's how the readings prediction typically works in a medical context 

Type the readings of report that scanned by our software with 90% accuracy this solve the case

"""
content_text_label = tk.Label(root, text=content_text, font=("Copperplate Gothic Bold", 14), wraplength=600, justify="center",foreground="blue")
content_text_label.pack(padx=20, pady=10)
# Create a label and text box for input data
input_label = ttk.Label(root, text="Enter the readings:" , font=("Copperplate Gothic Bold", 20),foreground="blue")
input_label.pack(pady=10)

input_data_entry = tk.Text(root, height=3, width=50)
input_data_entry.pack()

# Create a "Predict" button
predict_button = ttk.Button(root, text="Predict", command=predict_parkinsons, width= 30 ,style="Blue.TButton")
predict_button.pack(pady=10)

style = ttk.Style()
style.configure("Blue.TButton", foreground="blue", background="blue", font=("Copperplate Gothic Bold", 14))

result_label = ttk.Label(root, text="", font=("Copperplate Gothic Bold", 14))
result_label.pack()

# Start the GUI main loop
root.mainloop()
