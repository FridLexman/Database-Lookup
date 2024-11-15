import os
import tkinter as tk
from tkinter import ttk

class DirectorySearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Directory Search App")
        self.root.geometry("600x400")  # Initial window size

        # Configure root window for scalability
        self.root.grid_rowconfigure(1, weight=1)  # Row 1 will expand vertically
        self.root.grid_columnconfigure(0, weight=1)  # Column 0 will expand horizontally

        # Search bar
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(root, textvariable=self.search_var)
        self.search_entry.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
        self.search_entry.bind("<KeyRelease>", self.search_files)

        # Search button (optional if you want instant search on typing)
        self.search_button = tk.Button(root, text="Search", command=self.search_files)
        self.search_button.grid(row=0, column=1, sticky="ew", padx=10)

        # Results display with Listbox inside a Scrollable Frame
        self.results_frame = tk.Frame(root)
        self.results_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)
        self.results_frame.grid_rowconfigure(0, weight=1)
        self.results_frame.grid_columnconfigure(0, weight=1)

        # Listbox and Scrollbar for search results
        self.results_box = tk.Listbox(self.results_frame)
        self.results_box.grid(row=0, column=0, sticky="nsew")

        self.scrollbar = tk.Scrollbar(self.results_frame, orient="vertical", command=self.results_box.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.results_box.config(yscrollcommand=self.scrollbar.set)

    def search_files(self, event=None):
        search_query = self.search_var.get().lower()

        # Clear previous results
        self.results_box.delete(0, tk.END)

        # Search directory and filter results
        directory_path = r"C:\Users"  # Change to your directory
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if search_query in file.lower():
                    self.results_box.insert(tk.END, os.path.join(root, file))

# Run the application
root = tk.Tk()
app = DirectorySearchApp(root)
root.mainloop()