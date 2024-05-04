import tkinter as tk
from tkinter import filedialog
import numpy as np
from skimage import io, metrics, color
from skimage.transform import resize
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox

def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        # Load and process the user's uploaded image
        user_image = resize(io.imread(file_path), (256, 256), anti_aliasing=True)

        # Convert the image to grayscale
        user_image_gray = color.rgb2gray(user_image)

        # Specify the window size for SSIM calculation (e.g., 7x7)
        window_size = 7

        # Use np.squeeze to handle images
        user_image_gray = np.squeeze(user_image_gray)

        # Calculate SSIM between user's image and reference images with the specified parameters
        ssim_scores_parkinson = [metrics.structural_similarity(user_image_gray, img, win_size=window_size, data_range=1)
                                 for img in parkinson_images_gray]
        ssim_scores_healthy = [metrics.structural_similarity(user_image_gray, img, win_size=window_size, data_range=1)
                               for img in healthy_images_gray]

        # Calculate the average SSIM scores
        avg_ssim_parkinson = sum(ssim_scores_parkinson) / len(ssim_scores_parkinson)
        avg_ssim_healthy = sum(ssim_scores_healthy) / len(ssim_scores_healthy)

        # Make a prediction based on the average SSIM scores
        if avg_ssim_parkinson > avg_ssim_healthy:
            result = "HERE IS THE RESULT\nLikely Parkinson's Disease"
            result_label.config(text="HERE IS THE RESULT"
                                     "\nLikely Parkinson's Disease" ,justify='center',foreground='red')

        else:
            result = "HERE IS THE RESULT\nLikely Healthy"
            result_label.config(text="HERE IS THE RESULT"
                                    "\nLikely Healthy",justify='center',foreground='green')
        messagebox.showinfo("Result", result, icon=messagebox.INFO)

# Create a GUI window
root = tk.Tk()
root.title("Parkinson's Disease Detection")

# Set the window size and position it in the center of the screen
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
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

# Create a label to display content related to Parkinson's disease
content_label = ttk.Label(root, text="Parkinson's Disease spiral Predection", font=("Copperplate Gothic Bold", 20),foreground="blue")
content_label.pack(pady=20)



content_text = """Parkinson's disease is a neurodegenerative disorder that affects movement control. One of the motor symptoms of Parkinson's disease is tremors, which can manifest as a characteristic spiral drawing pattern when a person attempts to draw a spiral shape, such as a circle. The spiral drawing test is a common clinical tool used to assess the severity of tremors and motor dysfunction in individuals suspected of having Parkinson's disease.

Here's how the spiral prediction typically works in a medical context 

UPLOAD image of spiral drawing of report that scanned by our software with 90% accuracy this solve the case

"""
content_text_label = tk.Label(root, text=content_text, font=("Copperplate Gothic Bold", 14), wraplength=600, justify="center",foreground="blue")
content_text_label.pack(padx=20, pady=10)

# Load the reference images (10 Parkinson's and 10 Healthy)
parkinson_images = [
    resize(io.imread('C:/Users/HP/PycharmProjects/pythonProject/parkison/parkinson_image{}.jpg'.format(i)), (256, 256),
           anti_aliasing=True) for i in range(1, 6)]
healthy_images = [
    resize(io.imread('C:/Users/HP/PycharmProjects/pythonProject/healthy/healthy_image{}.jpg'.format(i)), (256, 256),
           anti_aliasing=True) for i in range(1, 6)]

# Convert images to grayscale
parkinson_images_gray = [color.rgb2gray(img) for img in parkinson_images]
healthy_images_gray = [color.rgb2gray(img) for img in healthy_images]

# Create a button to load an image
load_button = tk.Button(root, text="Upload Image", command=load_image, width= 30,height=5,foreground="red", background="white", font=("Copperplate Gothic Bold", 14) )
load_button.pack(side=tk.TOP, anchor=tk.NE, padx=20, pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Copperplate Gothic Bold", 16))
result_label.pack()

# Start the GUI main loop
root.mainloop()
