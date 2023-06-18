import tkinter as tk
from tkinter import filedialog

class DragDropWidget:
    def __init__(self, root):
        self.root = root
        self.widgets = []
        self.current_widget = None
        self.drag_start = None
                
        # Create the drag handle
        self.drag_handle = tk.Label(root, text="Drag and drop widgets to build your interface")
        self.drag_handle.pack(fill=tk.X)
        
        # Create the sidebar
        self.sidebar = tk.Frame(root)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        self.button1 = tk.Button(self.sidebar, text="Button")
        self.button1.pack(fill=tk.X)
        self.button1.bind("<ButtonPress-1>", self.start_drag)
        
        self.label1 = tk.Button(self.sidebar, text="Label")
        self.label1.pack(fill=tk.X)
        self.label1.bind("<ButtonPress-1>", self.start_drag)
        
        self.entry1 = tk.Button(self.sidebar, text="Entry")
        self.entry1.pack(fill=tk.X)
        self.entry1.bind("<ButtonPress-1>", self.start_drag)
        
        self.radio1 = tk.Button(self.sidebar, text="Radio Button")
        self.radio1.pack(fill=tk.X)
        self.radio1.bind("<ButtonPress-1>", self.start_drag)
        
        self.check1 = tk.Button(self.sidebar, text="Check Button")
        self.check1.pack(fill=tk.X)
        self.check1.bind("<ButtonPress-1>", self.start_drag)
        
        self.menu1 = tk.Button(self.sidebar, text="Menu")
        self.menu1.pack(fill=tk.X)
        self.menu1.bind("<ButtonPress-1>", self.start_drag)
        
        self.listbox1 = tk.Button(self.sidebar, text="List Box")
        self.listbox1.pack(fill=tk.X)
        self.listbox1.bind("<ButtonPress-1>", self.start_drag)