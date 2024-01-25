import tkinter as tk
from tkinter import messagebox

def display_message():
    messagebox.showinfo("Message", "Button Clicked!")

def open_file_explorer():
    messagebox.showinfo("File Explorer", "Opening File Explorer...")

# Create the main window
root = tk.Tk()
root.title("Windows XP-Like App")

# Configure window dimensions
root.geometry("800x600")

# Menu Bar
menu_bar = tk.Menu(root, bg="#004080", fg="white", activebackground="#0066cc", activeforeground="white")
root.config(menu=menu_bar)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0, bg="#004080", fg="white", activebackground="#0066cc", activeforeground="white")
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=display_message)
file_menu.add_command(label="Open", command=open_file_explorer)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Help Menu
help_menu = tk.Menu(menu_bar, tearoff=0, bg="#004080", fg="white", activebackground="#0066cc", activeforeground="white")
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Windows XP-Like App\nVersion 1.0"))

# Create a label in the main window
label = tk.Label(root, text="Hello, Windows XP-Like App!", font=("Arial", 16), bg="#f0f0f0")
label.pack(pady=10)

# Create a button in the main window
button = tk.Button(root, text="Click me!", command=display_message, bg="#0066cc", fg="white", padx=10, pady=5)
button.pack()

# Taskbar
taskbar = tk.Frame(root, bd=1, relief=tk.SUNKEN, bg="#1c1c1c")
taskbar.pack(side=tk.BOTTOM, fill=tk.X)

# Start Menu Button
start_button = tk.Button(taskbar, text="Start", command=lambda: messagebox.showinfo("Start Menu", "Opening Start Menu..."), bg="#1c1c1c", fg="white", padx=10, pady=5)
start_button.pack(side=tk.LEFT)

# Status Bar
status_bar = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W, bg="#1c1c1c", fg="white")
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Start the Tkinter event loop
root.mainloop()
