import os
import tkinter as tk
from tkinter import messagebox, simpledialog


class MovableButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        tk.Button.__init__(self, master, **kwargs)
        self.bind("<B1-Motion>", self.drag)
        self.bind("<Button-1>", self.save_location)
        self.drag_data = {"x": 0, "y": 0}

    def drag(self, event):
        x, y = self.drag_data["x"] + event.x, self.drag_data["y"] + event.y
        self.place(x=x, y=y)

    def save_location(self, event):
        self.drag_data["x"] = self.winfo_x() - event.x
        self.drag_data["y"] = self.winfo_y() - event.y


def open_folder(folder_name):
    messagebox.showinfo("Open Folder", f"Opening Folder: {folder_name}")


def create_windows_xp_interface():
    windows_xp_root = tk.Tk()
    windows_xp_root.title("Windows XP-Like App")
    windows_xp_root.geometry("800x600")
    windows_xp_root.configure(bg="#004080")

    folder_buttons = []  # List to store created folder buttons

    def create_new_folder():
        folder_name = simpledialog.askstring(
            "Create Folder", "Enter folder name:")
        if folder_name:
            # Save the new folder to the file
            with open("folders.txt", "a") as file:
                file.write(folder_name + "\n")

            new_folder_button = MovableButton(windows_xp_root, text=folder_name, command=lambda name=folder_name: open_folder(name),
                                              bg="#0066cc", fg="white", padx=10, pady=5)
            # Adjust the position
            new_folder_button.place(x=50, y=100 + len(folder_buttons) * 50)
            folder_buttons.append(new_folder_button)

    def show_context_menu(event):
        context_menu.post(event.x_root, event.y_root)

    def rename_folder(button):
        new_name = simpledialog.askstring(
            "Rename Folder", f"Enter new name for folder '{button.cget('text')}'")
        if new_name:
            # Rename the folder in the file
            with open("folders.txt", "r") as file:
                lines = file.readlines()
            with open("folders.txt", "w") as file:
                for line in lines:
                    if line.strip() == button.cget('text'):
                        file.write(new_name + "\n")
                    else:
                        file.write(line)
            # Rename the button
            button.config(text=new_name)

    def remove_folder(button):
        confirm = messagebox.askyesno(
            "Remove Folder", f"Do you want to remove the folder '{button.cget('text')}'?")
        if confirm:
            # Remove the folder from the file
            with open("folders.txt", "r") as file:
                lines = file.readlines()
            with open("folders.txt", "w") as file:
                for line in lines:
                    if line.strip() != button.cget('text'):
                        file.write(line)
            # Remove the button
            folder_buttons.remove(button)
            button.destroy()

    # Read folders from the file and create buttons
    with open("folders.txt", "r") as file:
        for line in file:
            folder_name = line.strip()
            if folder_name:
                new_folder_button = MovableButton(windows_xp_root, text=folder_name, command=lambda name=folder_name: open_folder(name),
                                                  bg="#0066cc", fg="white", padx=10, pady=5)
                # Adjust the position
                new_folder_button.place(x=50, y=100 + len(folder_buttons) * 50)
                folder_buttons.append(new_folder_button)

                # Add right-click context menu to each button
                context_menu = tk.Menu(windows_xp_root, tearoff=0)
                context_menu.add_command(
                    label="Rename", command=lambda btn=new_folder_button: rename_folder(btn))
                context_menu.add_command(
                    label="Remove", command=lambda btn=new_folder_button: remove_folder(btn))
                new_folder_button.bind(
                    "<Button-3>", lambda event, menu=context_menu: menu.post(event.x_root, event.y_root))

    # "Poste de Travail" Button
    post_travail_button = MovableButton(windows_xp_root, text="Poste de Travail", command=lambda: open_folder("Poste de Travail"),
                                        bg="#0066cc", fg="white", padx=10, pady=5)
    post_travail_button.place(x=50, y=50)  # Adjust the position
    folder_buttons.append(post_travail_button)

    def open_folder_by_click(button):
        open_folder(button.cget('text'))

    # Add left-click action to each button to open the folder
    for btn in folder_buttons:
        btn.config(command=lambda button=btn: open_folder_by_click(button))

    def on_closing():
        windows_xp_root.destroy()

    # Bind the closing event to save the current folder configuration
    windows_xp_root.protocol("WM_DELETE_WINDOW", on_closing)

    def create_new_folder_button():
        new_folder_button = MovableButton(windows_xp_root, text="New Folder", command=create_new_folder,
                                          bg="#0066cc", fg="white", padx=10, pady=5)
        new_folder_button.place(x=50, y=100 + len(folder_buttons) * 50)
        folder_buttons.append(new_folder_button)

    def create_new_folder():
        folder_name = simpledialog.askstring(
            "Create Folder", "Enter folder name:")
        if folder_name:
            # Save the new folder to the file
            with open("folders.txt", "a") as file:
                file.write(folder_name + "\n")

            new_folder_button = MovableButton(windows_xp_root, text=folder_name, command=lambda name=folder_name: open_folder(name),
                                              bg="#0066cc", fg="white", padx=10, pady=5)
            # Adjust the position
            new_folder_button.place(x=50, y=100 + len(folder_buttons) * 50)
            folder_buttons.append(new_folder_button)

    context_menu = tk.Menu(windows_xp_root, tearoff=0)
    context_menu.add_command(label="New Folder", command=create_new_folder)

    # Bind right mouse button to show context menu
    windows_xp_root.bind("<Button-3>", show_context_menu)

    windows_xp_root.mainloop()

# Function to handle login


def login():
    # Replace this with your actual authentication logic
    username = username_entry.get()
    password = password_entry.get()

    if username == "user" and password == "password":
        root.withdraw()  # Hide the login window
        create_windows_xp_interface()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


# Create the main window for login
root = tk.Tk()
root.geometry("800x600")
root.configure(bg="#004080")

login_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

username_label = tk.Label(login_frame, text="Username:", bg="#f0f0f0")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

password_label = tk.Label(login_frame, text="Password:", bg="#f0f0f0")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

login_button = tk.Button(login_frame, text="Login",
                         command=login, bg="#0066cc", fg="white")
login_button.grid(row=2, columnspan=2, pady=20)

root.mainloop()
