import os
import tkinter as tk
from tkinter import simpledialog, filedialog


class FileExplorer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.folder_path = tk.StringVar()
        self.current_path_label = tk.Label(
            self, textvariable=self.folder_path, bg="#f0f0f0")
        self.current_path_label.pack(fill='x')

        self.listbox = tk.Listbox(self)
        self.listbox.pack(expand=True, fill='both')

        self.listbox.bind("<Double-Button-1>", self.on_folder_selected)

        self.update_listbox()

    def update_listbox(self):
        path = self.folder_path.get()
        if not path:
            path = os.getcwd()

        self.listbox.delete(0, tk.END)

        try:
            for item in os.listdir(path):
                self.listbox.insert(tk.END, item)
        except PermissionError:
            self.listbox.insert(tk.END, "Permission Denied")

    def on_folder_selected(self, event):
        selection = self.listbox.curselection()
        if selection:
            selected_item = self.listbox.get(selection)
            path = os.path.join(self.folder_path.get(), selected_item)
            if os.path.isdir(path):
                self.folder_path.set(path)
                self.update_listbox()


class WindowsXPInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Windows XP Interface")
        self.geometry("800x600")

        self.login_frame = tk.Frame(self)
        self.login_frame.pack(expand=True, fill='both')

        username_label = tk.Label(
            self.login_frame, text="Username:", bg="#f0f0f0")
        username_label.grid(row=0, column=0, padx=10, pady=10)

        username_entry = tk.Entry(self.login_frame)
        username_entry.grid(row=0, column=1, padx=10, pady=10)

        password_label = tk.Label(
            self.login_frame, text="Password:", bg="#f0f0f0")
        password_label.grid(row=1, column=0, padx=10, pady=10)

        password_entry = tk.Entry(self.login_frame, show="*")
        password_entry.grid(row=1, column=1, padx=10, pady=10)

        login_button = tk.Button(
            self.login_frame, text="Login", command=self.create_windows_xp_interface)
        login_button.grid(row=2, column=1, pady=10)

    def create_windows_xp_interface(self):
        self.login_frame.destroy()

        self.file_explorer_frame = tk.Frame(self)
        self.file_explorer_frame.pack(expand=True, fill='both')

        self.file_explorer = FileExplorer(self.file_explorer_frame)

        button_frame = tk.Frame(self)
        button_frame.pack()

        new_file_button = tk.Button(
            button_frame, text="New Text File", command=self.create_text_file)
        new_file_button.grid(row=0, column=0, padx=10)

        open_file_button = tk.Button(
            button_frame, text="Open Text File", command=self.open_text_file)
        open_file_button.grid(row=0, column=1, padx=10)

    def create_text_file(self):
        file_name = simpledialog.askstring(
            "Create Text File", "Enter the file name:")
        if file_name:
            file_path = os.path.join(
                self.file_explorer.folder_path.get(), file_name + ".txt")
            with open(file_path, 'w'):
                pass  # Create an empty text file
            self.file_explorer.update_listbox()

    def open_text_file(self):
        file_path = filedialog.askopenfilename(initialdir=self.file_explorer.folder_path.get(
        ), title="Select Text File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_path:
            # You can add logic here to handle opening the selected text file
            print(f"Opening text file: {file_path}")


if __name__ == "__main__":
    app = WindowsXPInterface()
    app.mainloop()
