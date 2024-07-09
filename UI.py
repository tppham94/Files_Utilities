import tkinter as tk
from tkinter import filedialog

class FileUtilitiesUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Utilities")
        
        # Determine screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # Calculate center coordinates
        x = (screen_width // 2) - (720 // 2)
        y = (screen_height // 2) - (400 // 2)
        
        # Set initial window size and position
        self.root.geometry('720x400+{}+{}'.format(x, y))
        
        # File path variables
        self.file_path1 = tk.StringVar()
        self.file_path2 = tk.StringVar()
        self.output_file = tk.StringVar()
        
        # Create UI elements
        self.label1 = tk.Label(self.root, text="Select File 1:")
        self.label1.pack()
        
        self.button1 = tk.Button(self.root, text="Browse...", command=self.select_file1)
        self.button1.pack()
        
        self.file_label1 = tk.Label(self.root, textvariable=self.file_path1)
        self.file_label1.pack()
        
        self.label2 = tk.Label(self.root, text="Select File 2:")
        self.label2.pack()
        
        self.button2 = tk.Button(self.root, text="Browse...", command=self.select_file2)
        self.button2.pack()
        
        self.file_label2 = tk.Label(self.root, textvariable=self.file_path2)
        self.file_label2.pack()
        
        self.label_output = tk.Label(self.root, text="Output File Name:")
        self.label_output.pack()
        
        self.entry_output = tk.Entry(self.root, textvariable=self.output_file)
        self.entry_output.pack()
        
        self.generate_button = tk.Button(self.root, text="Generate", command=self.generate_output)
        self.generate_button.pack()
        
    def select_file1(self):
        file_path = filedialog.askopenfilename(initialdir="~/Desktop", title="Select File 1")
        self.file_path1.set(file_path)
        
    def select_file2(self):
        file_path = filedialog.askopenfilename(initialdir="~/Desktop", title="Select File 2")
        self.file_path2.set(file_path)
        
    def generate_output(self):
        file1 = self.file_path1.get()
        file2 = self.file_path2.get()
        output_name = self.output_file.get()
        
        # Need to add logic to get the output name properly 
        #print("File 1:", file1)
        #print("File 2:", file2)
        #print("Output File Name:", output_name)
        

if __name__ == "__main__":
    root = tk.Tk()
    app = FileUtilitiesUI(root)
    root.mainloop()

