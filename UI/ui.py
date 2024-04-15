from tkinter import *
from tkinter import ttk
from UI import keybinds

class MainUI:
    def __init__(self, root):
        root.title("Clipboard Manager")
        MainFrame = ttk.Frame(root)
        MainFrame.grid(column=0, row=0)
        keybinds.Keybinds(MainFrame)



