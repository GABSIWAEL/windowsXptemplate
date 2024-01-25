import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog


class InternalFileEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Internal File Editor")

        # Create a Text widget for text input
        self.text_editor = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, width=40, height=10)
        self.text_editor.pack(expand=True, fill="both")

        # Create a button to save the text to an internal file
        self.save_button = tk.Button(
            root, text="Save File", command=self.save_text_to_file)
        self.save_button.pack()

        # Create a button to add content from an existing file
        self.add_file_button = tk.Button(
            root, text="Add File", command=self.add_content_from_file)
        self.add_file_button.pack()

        # Internal file content
        self.internal_file_content = ""

    def save_text_to_file(self):
        # Save the text to the internal file content
        self.internal_file_content = self.text_editor.get("1.0", tk.END)

        # Prompt user for a file name
        file_name = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            title="Save As"
        )

        # If the user selected a file name, save the content to the file
        if file_name:
            with open(file_name, 'w') as new_file:
                new_file.write(self.internal_file_content)

            print("File saved:", file_name)

            # Clear the text editor
            self.text_editor.delete("1.0", tk.END)

    def add_content_from_file(self):
        # Prompt user to select a file
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            title="Select a Text File"
        )

        # If the user selected a file, add its content to the internal editor
        if file_path:
            with open(file_path, 'r') as selected_file:
                file_content = selected_file.read()
                self.text_editor.insert(tk.END, file_content)


if __name__ == "__main__":
    root = tk.Tk()
    app = InternalFileEditor(root)
    root.mainloop()
