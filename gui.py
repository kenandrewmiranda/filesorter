import os
import tkinter as tk
from tkinter import filedialog, messagebox
import helpers.helper as helper

class FileManagerApp:
    '''
    This class is responsible for the GUI of the application and the logic of the application
    '''
    def __init__(self, root):
        self.root = root
        self.folderPath = tk.StringVar()
        self.folderPath.set(os.path.join(os.path.expanduser('~'), 'Downloads'))
        self.setup_ui()

    def setup_ui(self):
        self.root.title("File Manager")
        self.root.geometry("250x200")
        self.root.resizable(False, False)
        self.root.configure(bg='white')
        
        self.setup_instructions()
        self.setup_folder_path_display()
        self.setup_buttons()

    def setup_instructions(self):
        instructions = tk.Label(self.root, text='This program will sort files into \n individual folders based on their file type', bg='white')
        instructions.pack(padx=10, pady=10)

    def setup_folder_path_display(self):
        folderPathLabel = tk.Label(self.root, text='Selected Folder', bg='white')
        folderPathLabel.pack(padx=3, pady=3)

        currentFolderPath = tk.Label(self.root, textvariable=self.folderPath, bg='white', borderwidth=1, relief="groove", padx=5, pady=5)
        currentFolderPath.pack(padx=5, pady=5)

    def setup_buttons(self):
        changeFolderBtn = tk.Button(self.root, text="Change Folder Path", command=self.get_folder, bg='white')
        changeFolderBtn.pack(padx=5, pady=5)

        runBtn = tk.Button(self.root, text="Run", command=self.move_files, bg='white')
        runBtn.pack(padx=5, pady=5)

    def get_folder(self):
        folder_selected = filedialog.askdirectory()
        self.folderPath.set(folder_selected)
        
    def move_files(self):
        file_list = helper.get_file_list(self.folderPath.get())
        extensions = helper.get_extension_list(file_list, self.folderPath.get())
        helper.create_folders(extensions, self.folderPath.get())
        for file in file_list:
            helper.move_file(file, self.folderPath.get())
        messagebox.showinfo("Success", "Files moved successfully")
