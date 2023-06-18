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

                # Create the window size widgets
        self.window_size_label = tk.Label(self.sidebar, text="Window Size WxH")
        self.window_size_label.pack(fill=tk.X)
        
        self.width_frame = tk.Frame(self.sidebar)
        self.width_frame.pack(fill=tk.X)
        self.width_label = tk.Label(self.width_frame, text="Width:")
        self.width_label.pack(side=tk.LEFT)
        self.width_entry = tk.Entry(self.width_frame)
        self.width_entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)
        self.width_entry.insert(0, str(root.winfo_width()))
        
        self.height_frame = tk.Frame(self.sidebar)
        self.height_frame.pack(fill=tk.X)
        self.height_label = tk.Label(self.height_frame, text="Height:")
        self.height_label.pack(side=tk.LEFT)
        self.height_entry = tk.Entry(self.height_frame)
        self.height_entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)
        self.height_entry.insert(0, str(root.winfo_height()))
        
        # Create the workspace
        self.workspace = tk.Canvas(root, bg="white")
        self.workspace.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.workspace.bind("<ButtonPress-1>", self.place_widget)
        self.workspace.bind("<B1-Motion>", self.drag_widget)
        self.workspace.bind("<ButtonRelease-1>", self.drop_widget)
        
        # Create the finish button
        self.finish_button = tk.Button(root, text="Finish", command=self.generate_code)
        self.finish_button.pack(fill=tk.X, side=tk.TOP)
        
        # Update the window size label when the window is resized
        root.bind("<Configure>", self.update_window_size_label)
        
    def start_drag(self, event):
        self.current_widget = event.widget
        self.drag_start = (event.x, event.y)
        
    def place_widget(self, event):
        if self.current_widget is not None:
            widget_type = str(self.current_widget["text"]).lower()
            if widget_type == "button":
                widget = tk.Button(self.workspace, text="Button")
            elif widget_type == "label":
                widget = tk.Label(self.workspace, text="Label")
            elif widget_type == "entry":
                widget = tk.Entry(self.workspace)
            elif widget_type == "radio button":
                widget = tk.Radiobutton(self.workspace, text="Radio Button")
            elif widget_type == "check button":
                widget = tk.Checkbutton(self.workspace, text="Check Button")
            elif widget_type == "menu":
                widget = tk.Menubutton(self.workspace, text="Menu")
                widget.menu = tk.Menu(widget, tearoff=0)
                widget["menu"] = widget.menu
                widget.menu.add_command(label="Option 1")
                widget.menu.add_command(label="Option 2")
            elif widget_type == "list box":
                widget = tk.Listbox(self.workspace)
                widget.insert(1, "List Item 1")
                widget.insert(2, "List Item 2")
                
            widget.place(x=event.x, y=event.y)
            self.widgets.append(widget)
            self.current_widget = None
            
    def drag_widget(self, event):
        if self.drag_start is not None:
            dx = event.x - self.drag_start[0]
            dy = event.y - self.drag_start[1]
            self.workspace.move(tk.CURRENT, dx, dy)
            self.drag_start = (event.x, event.y)
            
    def drop_widget(self, event):
        self.drag_start = None
        
    def update_window_size_label(self, event):
        self.width_entry.delete(0, tk.END)
        self.width_entry.insert(0, str(self.root.winfo_width()))
        self.height_entry.delete(0, tk.END)
        self.height_entry.insert(0, str(self.root.winfo_height()))
        
    def generate_code(self):
        code = "# Generated Python tkinter code\n\n"
        
        # Generate code for widgets
        for widget in self.widgets:
            if isinstance(widget, tk.Button):
                code += f"{widget._name} = tk.Button(root, text=\"{widget.cget('text')}\")\n"
            elif isinstance(widget, tk.Label):
                code += f"{widget._name} = tk.Label(root, text=\"{widget.cget('text')}\")\n"
            elif isinstance(widget, tk.Entry):
                code += f"{widget._name} = tk.Entry(root)\n"
            elif isinstance(widget, tk.Radiobutton):
                code += f"{widget._name} = tk.Radiobutton(root, text=\"{widget.cget('text')}\")\n"
            elif isinstance(widget, tk.Checkbutton):
                code += f"{widget._name} = tk.Checkbutton(root, text=\"{widget.cget('text')}\")\n"
            elif isinstance(widget, tk.Menubutton):
                code += f"{widget._name} = tk.Menubutton(root, text=\"{widget.cget('text')}\")\n"
                menu_items = []
                for item in widget.menu.get(0, tk.END):
                    menu_items.append(f"\"{item}\"")
                code += f"{widget._name}.menu = tk.Menu({widget._name}, tearoff=0)\n"
                for item in menu_items:
                    code += f"{widget._name}.menu.add_command(label={item})\n"
                code += f"{widget._name}[\"menu\"] = {widget._name}.menu\n"
            elif isinstance(widget, tk.Listbox):
                code += f"{widget._name} = tk.Listbox(root)\n"
                for i in range(widget.size()):
                    code += f"{widget._name}.insert({i+1}, \"{widget.get(i)}\")\n"
            code += f"{widget._name}.place(x={widget.winfo_x()}, y={widget.winfo_y()})\n\n"
        
        # Generate code for window size
        code += f"root.geometry(\"{self.root.winfo_width()}x{self.root.winfo_height()}\")\n"
        
        # Display the generated code
        print(code)

        # Save the generated code as a Python file using a save dialog
        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
        if file_path:
            with open(file_path, "w") as f:
                f.write(code)
            
        
root = tk.Tk()
app = DragDropWidget(root)
root.mainloop()