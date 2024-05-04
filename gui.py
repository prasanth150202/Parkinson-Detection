import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading
import os

def run_external_script(script_name):
    # Hide all frames
    for frame in (spiral_frame, wave_frame, numbers_frame, stroke_frame):
        frame.pack_forget()

    # Run the external script
    script_path = os.path.join( script_name)
    os.system(f"python {script_path}")

# Function to switch to the Spiral Prediction section
def show_spiral_section():
    # Hide all frames
    for frame in (wave_frame, numbers_frame, stroke_frame):
        frame.pack_forget()

    # Show the Spiral Prediction frame
    spiral_frame.pack(fill=tk.BOTH, expand=True)
    threading.Thread(target=run_external_script, args=("spiral.py",)).start()

# Function to switch to the Wave Prediction section
def show_wave_section():
    # Hide all frames
    for frame in (spiral_frame, numbers_frame, stroke_frame):
        frame.pack_forget()

    # Show the Wave Prediction frame
    wave_frame.pack(fill=tk.BOTH, expand=True)
    threading.Thread(target=run_external_script, args=("wave.py",)).start()

# Function to switch to the Numbers in Report section
def show_numbers_section():
    # Hide all frames
    for frame in (spiral_frame, wave_frame, stroke_frame):
        frame.pack_forget()

    # Show the Numbers in Report frame
    numbers_frame.pack(fill=tk.BOTH, expand=True)
    threading.Thread(target=run_external_script, args=("number.py",)).start()

# Function to switch to the Stroke Detection section
def show_stroke_section():
    # Hide all frames
    for frame in (spiral_frame, wave_frame, numbers_frame):
        frame.pack_forget()

    # Show the Stroke Detection frame
    stroke_frame.pack(fill=tk.BOTH, expand=True)
    threading.Thread(target=run_external_script, args=("heart.py",)).start()

# Create the main window
root = tk.Tk()
root.title("Neurological Disease Detection")

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

# Create a label to display content related to neurological diseases
content_label = ttk.Label(root, text="Neurological Disease Detection", font=("Copperplate Gothic Bold", 20),foreground="blue")
content_label.pack(pady=20)

# Add content about neurological diseases
content_text = """
Neurological diseases affect the brain and nervous system, causing a wide range of symptoms 
and complications. Early detection and intervention are essential for managing these conditions 
and improving patient outcomes.
"""

content_text_label = tk.Label(root, text=content_text, font=(None, 14), wraplength=600, justify="left",foreground="blue")
content_text_label.pack(padx=20, pady=10)

# Create buttons for navigation
spiral_button = ttk.Button(root, text="Spiral Prediction", command=show_spiral_section, width=30, style="Blue.TButton")
spiral_button.pack(side=tk.TOP, anchor=tk.NE, padx=20, pady=10)

wave_button = ttk.Button(root, text="Wave Prediction", command=show_wave_section, width=30, style="Blue.TButton")
wave_button.pack(side=tk.TOP, anchor=tk.NE, padx=20, pady=10)

numbers_button = ttk.Button(root, text="Numbers in Report", command=show_numbers_section, width=30, style="Blue.TButton")
numbers_button.pack(side=tk.TOP, anchor=tk.NE, padx=20, pady=10)

stroke_button = ttk.Button(root, text="Stroke Detection", command=show_stroke_section, width=30, style="Blue.TButton")
stroke_button.pack(side=tk.TOP, anchor=tk.NE, padx=20, pady=10)

style = ttk.Style()
style.configure("Blue.TButton", foreground="blue", background="blue", font=(None, 14))

# Create frames for each section
spiral_frame = ttk.Frame(root)
wave_frame = ttk.Frame(root)
numbers_frame = ttk.Frame(root)
stroke_frame = ttk.Frame(root)

# Content for the Spiral Prediction section (You can replace this with your spiral.py content)
content_text_spiral = "This is the Spiral Prediction section."
content_label_spiral = ttk.Label(spiral_frame, text=content_text_spiral, font=(None, 16))
content_label_spiral.pack(pady=20)

# Content for the Wave Prediction section (You can replace this with your wave.py content)
content_text_wave = "This is the Wave Prediction section."
content_label_wave = ttk.Label(wave_frame, text=content_text_wave, font=(None, 16))
content_label_wave.pack(pady=20)

# Content for the Numbers in Report section (You can replace this with your numerics.py content)
content_text_numbers = "This is the Numbers in Report section."
content_label_numbers = ttk.Label(numbers_frame, text=content_text_numbers, font=(None, 16))
content_label_numbers.pack(pady=20)

# Start the GUI main loop
root.mainloop()
