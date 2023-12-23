
import tkinter as tk
import subprocess

def open_gui(language):
    if language == 'English':
        subprocess.Popen(['python', 'eng_gui.py'])
    elif language == 'Hindi':
        subprocess.Popen(['python', 'hindi_gui.py'])

root = tk.Tk()
root.title("MedBay - Select Language")

# Set the size of the main window to 400x400 pixels
root.geometry("350x350")

# Set the background color to black
root.configure(bg="black")

# Create a frame to center the buttons
frame = tk.Frame(root, bg="black")
frame.pack(expand=True)

label = tk.Label(frame, text="Select a language:", fg="white", bg="black")
label.pack()

english_button = tk.Button(frame, text="English", command=lambda: open_gui('English'), bg="black", fg="white")
english_button.pack()

hindi_button = tk.Button(frame, text="हिंदी", command=lambda: open_gui('Hindi'), bg="black", fg="white")
hindi_button.pack()

root.mainloop()
