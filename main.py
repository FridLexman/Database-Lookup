import os
import tkinter as tk
from tkinter import ttk

class DirectorySearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Directory Search App")
        
        # Search bar
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(root, textvariable=self.search_var, width=50)
        self.search_entry.pack(pady=5)
        self.search_entry.bind("<KeyRelease>", self.search_files)  # Trigger search on key release

        # Search button (optional if you want instant search on typing)
        self.search_button = tk.Button(root, text="Search", command=self.search_files)
        self.search_button.pack(pady=5)

        # Results display
        self.results_box = tk.Listbox(root, width=80, height=20)
        self.results_box.pack(pady=5)

    def search_files(self, event=None):
        search_query = self.search_var.get().lower()  # Get current search query
        directory_path = r"C:/DIRECTORY/HERE"  # Change to your directory

        # Clear previous results
        self.results_box.delete(0, tk.END)

        # Search directory and filter results
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if search_query in file.lower():
                    self.results_box.insert(tk.END, os.path.join(root, file))

# Run the application
root = tk.Tk()
app = DirectorySearchApp(root)
root.mainloop()
