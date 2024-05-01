
from tkinter import *
from PIL import ImageTk, Image
import os

# Function to handle button click event
def on_click(file_path):
    if os.path.exists(file_path):
        os.system(file_path)
    else:
        print(f"File not found: {file_path}")

# Create main window
root = Tk()
root.title("Sports Utility Inventory Management System")
root.geometry("600x400")
root.config(bg="#F5F5F5")

# Load the background image
bg_image = Image.open("C:/Users/Santosh/Downloads/5e0c6875b768e.png")
bg_image = bg_image.resize((1200, 1400))  # Resize the image to match window size
background_photo = ImageTk.PhotoImage(bg_image)

# Create a label to display the background image
background_label = Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Title label
title_label = Label(root, text="Sports Utility Inventory Management System", font=("Arial", 30, "bold"), bg="#FF0000", fg="white")
title_label.pack(pady=15)

# College label
college_label = Label(root, text="Anand Vishwa Gurukul Sr. Night College - Thane(w)", font=("Arial", 18, "bold"), bg="#4CAF50", fg="black")
college_label.pack(pady=15)

# Define file paths for each functionality
file_paths = {
    "Add Item": "C:/Users/Santosh/Downloads/cLG-main/cLG-main/AddEquipment.py",
    "Remove Item": "C:/Users/Santosh/Downloads/cLG-main/cLG-main/DeleteEquipment.py",
    "View Inventory": "C:/Users/Santosh/Downloads/cLG-main/cLG-main/ViewEquipment.py",
    "Issue Item": "C:/Users/Santosh/Downloads/cLG-main/cLG-main/IssueEquipment.py",
    "Return Item": "C:/Users/Santosh/Downloads/cLG-main/cLG-main/ReturnEquipment.py"
}

# Buttons
for functionality, file_path in file_paths.items():
    button = Button(root, text=functionality, width=20, font=("Arial", 12, "bold"), command=lambda fp=file_path: on_click(fp))
    button.pack(pady=10)

exit_button = Button(root, text="Exit", width=20, bg="#555555", fg="white", font=("Arial", 12, "bold"), command=root.quit)
exit_button.pack(pady=10)

# Run the main event loop
root.mainloop()
