from tkinter import *
from tkinter import ttk
from UI import keybinds

class MainUI:
    def __init__(self, root: Tk):
        root.title("Clipboard Manager")
        root.geometry("500x300")
        MainFrame = ttk.Frame(root)
        MainFrame.grid(column=0, row=0)
        keybinds.Keybinds(MainFrame)



