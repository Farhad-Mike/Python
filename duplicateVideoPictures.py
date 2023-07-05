import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import imagehash

# Function to calculate the perceptual hash of an image
def calculate_image_hash(image_path):
    try:
        with Image.open(image_path) as img:
            hash_value = imagehash.average_hash(img)
            return str(hash_value)
    except (IOError, OSError):
        return None

# Function to scan a folder for duplicate pictures and videos
def scan_duplicates():
    folder_path = filedialog.askdirectory(title="Select Folder to Scan")

    if not folder_path:
        return

    image_hashes = {}
    video_files = []
    duplicate_files = []

    # Iterate over all files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file_path)[1].lower()

            if file_extension in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']:
                # Calculate and store the perceptual hash of the image
                hash_value = calculate_image_hash(file_path)
                if hash_value:
                    if hash_value in image_hashes:
                        duplicate_files.append(file_path)
                        duplicate_files.append(image_hashes[hash_value])
                    else:
                        image_hashes[hash_value] = file_path
            elif file_extension in ['.mp4', '.avi', '.mov', '.mkv']:
                video_files.append(file_path)

    if not duplicate_files:
        messagebox.showinfo("Scan Complete", "No duplicate files found!")
    else:
        delete_duplicates(duplicate_files)

# Function to delete selected duplicate files
def delete_duplicates(duplicate_files):
    root = tk.Tk()
    root.title("Delete Duplicate Files")
    root.geometry("600x400")

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(root, yscrollcommand=scrollbar.set)
    listbox.pack(fill=tk.BOTH, expand=True)

    scrollbar.config(command=listbox.yview)

    for file_path in duplicate_files:
        listbox.insert(tk.END, file_path)

    def delete_selected():
        selected_indices = listbox.curselection()
        if selected_indices:
            selected_files = [duplicate_files[index] for index in selected_indices]
            confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete the selected files?")
            if confirm:
                for file_path in selected_files:
                    try:
                        os.remove(file_path)
                    except OSError:
                        messagebox.showerror("Deletion Error", f"Failed to delete file: {file_path}")
                messagebox.showinfo("Deletion Complete", "Selected files deleted successfully!")
                root.destroy()

    delete_button = tk.Button(root, text="Delete Selected", command=delete_selected)
    delete_button.pack(pady=10)

    root.mainloop()

# Create the main window
root = tk.Tk()
root.title("Duplicate File Scanner")
root.geometry("300x150")

# Create a button to initiate the scan
scan_button = tk.Button(root, text="Scan Duplicates", command=scan_duplicates)
scan_button.pack(pady=30)

# Start the main loop
root.mainloop()
