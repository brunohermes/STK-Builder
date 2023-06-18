import tkinter as tk
from tkinter import filedialog

class DragDropWidget:
    def __init__(self, root):
        self.root = root
        self.widgets = []
        self.current_widget = None
        self.drag_start = None