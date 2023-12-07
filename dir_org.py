import os
import shutil
import tkinter as tk
from tkinter import filedialog

def choose_dir(return_directory):
    directory = filedialog.askdirectory()
    return_directory.set(directory)

def choose_dir_dialog():
    # Create the main window
    root = tk.Tk()
    root.title("Directory Chooser")
    # set size of the window
    root.geometry("400x200")

    # set return directory
    chosen_directory = tk.StringVar();

    # Create a button to trigger the file dialog
    button = tk.Button(root, text="Choose File", command=choose_dir(chosen_directory))
    button.pack(pady=20)

    chosen_path = os.path.normpath(chosen_directory.get())

    return chosen_path

file_extensions = [
    ['doc', 'docx', 'txt'],
    ['xls', 'xlsx', 'xlsm', 'xltx', 'xltm'],
    ['ppt', 'pptx'],
    ['html'],
    ['jpg','png','gif'],
    ['zip','tar.gz', 'rar'],
    ['pdf'],
    ['mp4','mov', 'wmv', 'avi', 'mkv'],
    ['exe', 'msi', 'com', 'cmd', 'inf', 'run'],
    ['bat', 'sh'],
    ['py'],
    ['ipynb'],
    ['json']
]
# subdirectory names according to file extension
sub_folders = ['word', 'excel', 'ppt', 'html', 'image', 'zipfile', 'pdf', 'video','exec', 'scriprt', 'python', 'jupyter', 'json']

def get_sub_folder(extension):
    # if can't find extesion in file_extensions, return 'others'
    sub_folder_name = 'others'
    for i, extensions in enumerate(file_extensions):
        if extension in extensions:
            sub_folder_name = sub_folders[i]
            break
    return sub_folder_name

def organize_files(source_folder):
    # Iterate through files in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Check if it's a file
        if os.path.isfile(source_path):
            # Extract file extension
            _, extension = os.path.splitext(filename)

            # Remove the dot from the extension
            extension = extension[1:].lower()

            # Get subfolder name
            sub_fd_name = get_sub_folder(extension)

            # Create a folder for the extension if it doesn't exist
            extension_folder = os.path.join(source_folder, sub_fd_name)
            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)

            # Move the file to the corresponding folder
            destination_path = os.path.join(extension_folder, filename)
            shutil.move(source_path, destination_path)
            print(f"Moved {filename} to {extension_folder}")


# choose and orginize a directory
organize_files(choose_dir_dialog())