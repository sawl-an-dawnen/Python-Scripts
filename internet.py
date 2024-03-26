import tkinter as tk

def toggle_button():
    if button.cget("text") == "ON":
        button.config(text="OFF", bg="darkgray")
    else:
        button.config(text="ON", bg="SystemButtonFace")

# Create the main window
root = tk.Tk()
root.title("Internet")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size and position it in the center of the screen
window_width = 200
window_height = 150
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create a label for the heading
label = tk.Label(root, text="Internet", font=("Helvetica", 16))
label.pack(pady=10)

# Create a button
button = tk.Button(root, text="ON", bg="SystemButtonFace", command=toggle_button)
button.pack(expand=True)

# Run the Tkinter event loop
root.mainloop()