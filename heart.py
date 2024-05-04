import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle
from sklearn.ensemble import RandomForestClassifier

def prediction_model(entry_values):
    x = [entry_values]
    randomforest = pickle.load(open('model.sav', 'rb'))
    predictions = randomforest.predict(x)
    if predictions == 0:
        result_label.config(text='********Less chance of Heart Stroke********')
    else:
        result_label.config(text='********High chance of Heart Stroke********')

# Load the dataset
df = pd.read_csv('heart.csv')

predictors = df.drop(['target'], axis=1)
target = df["target"]
x_train, _, y_train, _ = train_test_split(predictors, target, test_size=0.22, random_state=0)
randomforest = RandomForestClassifier()
randomforest.fit(x_train, y_train)

# Save the trained model
filename = 'model.sav'
pickle.dump(randomforest, open(filename, 'wb'))

# Create Tkinter window
window = tk.Tk()
window.title("Heart Stroke Predictor")

# Create and place widgets
age_label = ttk.Label(window, text="Age:")
age_label.grid(row=0, column=0, padx=10, pady=5)
age_entry = ttk.Entry(window)
age_entry.grid(row=0, column=1, padx=10, pady=5)

sex_label = ttk.Label(window, text="Sex:")
sex_label.grid(row=1, column=0, padx=10, pady=5)
sex_combo = ttk.Combobox(window, values=['Male', 'Female'])
sex_combo.grid(row=1, column=1, padx=10, pady=5)

cp_label = ttk.Label(window, text="Chest pain type:")
cp_label.grid(row=2, column=0, padx=10, pady=5)
cp_combo = ttk.Combobox(window, values=[0, 1, 2, 3])
cp_combo.grid(row=2, column=1, padx=10, pady=5)

trestbps_label = ttk.Label(window, text="Resting blood pressure:")
trestbps_label.grid(row=3, column=0, padx=10, pady=5)
trestbps_entry = ttk.Entry(window)
trestbps_entry.grid(row=3, column=1, padx=10, pady=5)

chol_label = ttk.Label(window, text="Serum cholestoral in mg/dl:")
chol_label.grid(row=4, column=0, padx=10, pady=5)
chol_entry = ttk.Entry(window)
chol_entry.grid(row=4, column=1, padx=10, pady=5)

fbs_label = ttk.Label(window, text="Fasting blood sugar > 120 mg/dl:")
fbs_label.grid(row=5, column=0, padx=10, pady=5)
fbs_combo = ttk.Combobox(window, values=[0, 1])
fbs_combo.grid(row=5, column=1, padx=10, pady=5)

restecg_label = ttk.Label(window, text="Resting electrocardiographic results:")
restecg_label.grid(row=6, column=0, padx=10, pady=5)
restecg_combo = ttk.Combobox(window, values=[0, 1, 2])
restecg_combo.grid(row=6, column=1, padx=10, pady=5)

thalach_label = ttk.Label(window, text="Maximum heart rate achieved:")
thalach_label.grid(row=7, column=0, padx=10, pady=5)
thalach_entry = ttk.Entry(window)
thalach_entry.grid(row=7, column=1, padx=10, pady=5)

exang_label = ttk.Label(window, text="Exercise induced angina:")
exang_combo = ttk.Combobox(window, values=[0, 1])
exang_combo.grid(row=8, column=1, padx=10, pady=5)

oldpeak_label = ttk.Label(window, text="Oldpeak:")
oldpeak_entry = ttk.Entry(window)
oldpeak_entry.grid(row=9, column=1, padx=10, pady=5)

slope_label = ttk.Label(window, text="The slope of the peak exercise ST segment:")
slope_entry = ttk.Entry(window)
slope_entry.grid(row=10, column=1, padx=10, pady=5)

ca_label = ttk.Label(window, text="Number of major vessels (0-3) colored by fluoroscopy:")
ca_entry = ttk.Entry(window)
ca_entry.grid(row=11, column=1, padx=10, pady=5)

thal_label = ttk.Label(window, text="Thal:")
thal_combo = ttk.Combobox(window, values=[0, 1, 2], state='readonly')
thal_combo.grid(row=12, column=1, padx=10, pady=5)

def get_values():
    entry_values = [
        int(age_entry.get()),
        1 if sex_combo.get() == 'Female' else 0,
        int(cp_combo.get()),
        int(trestbps_entry.get()),
        int(chol_entry.get()),
        int(fbs_combo.get()),
        int(restecg_combo.get()),
        int(thalach_entry.get()),
        int(exang_combo.get()),
        float(oldpeak_entry.get()),
        float(slope_entry.get()),
        float(ca_entry.get()),
        int(thal_combo.get())
    ]
    prediction_model(entry_values)

predict_button = ttk.Button(window, text="Predict", command=get_values)
predict_button.grid(row=13, column=0, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(window, text="")
result_label.grid(row=14, column=0, columnspan=2, padx=10, pady=5)

window.mainloop()
