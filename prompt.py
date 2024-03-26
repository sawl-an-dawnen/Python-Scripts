import tkinter as tk
from tkinter import messagebox
import os

def save_to_file():
    text = text_entry.get("1.0", "end-1c")  # Get the text from the text entry field
    if text.strip():  # Check if the text is not empty
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')  # Get the path to the desktop
        file_path = os.path.join(desktop_path, "text_input.txt")  # Create a file path in the Documents folder
        with open(file_path, "w") as file:
            file.write(text)  # Write the text to the file
        messagebox.showinfo("File Saved", "Text saved to text_input.txt on Documents")
    else:
        messagebox.showwarning("Empty Text", "Please enter some text!")

# Create the main window
root = tk.Tk()
root.title("Text Input")

# Create a text entry field
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack()

# Create a button to save the text to a file
save_button = tk.Button(root, text="Save to File", command=save_to_file)
save_button.pack()

# Run the Tkinter event loop
root.mainloop()