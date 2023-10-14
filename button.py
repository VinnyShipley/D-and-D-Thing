import tkinter as tk
from PIL import Image, ImageTk

def countdown():
    # Get the number from the entry widget
    start_number = 20
    
    start_button.grid_forget()

    # Function to update the label
    def update_label(number):
        if number <= 20:
            label.config(text=str(number), fg="blue")
            
        if number <= 15:
            label.config(text=str(number), fg="yellow")
            
        if number <= 10:
            label.config(text=str(number), fg="orange")
            
        if number <= 5:
            label.config(text=str(number), fg="red", bg='black')
            root.configure(bg='black')
            spacer.configure(bg='black')
            
        if number > 0:
            root.after(1000, update_label, number - 1)

    update_label(start_number)

# Create the main application window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("800x400")

# Set the background color of the main window
root.configure(bg="lightblue")

# Load the JPEG image
button_image = Image.open("assets/recall.webp")
button_photo = ImageTk.PhotoImage(button_image)

# Calculate vertical padding based on button image height
button_height = button_photo.height()
window_height = root.winfo_height()
vertical_padding = (window_height - button_height) // 2

# Create a label to act as a spacer for vertical centering
spacer = tk.Label(root, text="", bg="lightblue", height=vertical_padding)
spacer.grid(row=0, column=0, pady=abs(vertical_padding))

# Create a button to start the countdown
start_button = tk.Button(root, image=button_photo, command=countdown)
start_button.image = button_photo
start_button.grid(row=1, column=0)

# Create a label to display the countdown
label = tk.Label(root, text="", bg='lightblue')
label.grid(row=2, column=0)

# Configure grid weights to center the label within the cell
root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)

# Center the label text
label.config(justify="center")


# Start the main event loop to display the window and handle user interactions
root.mainloop()
