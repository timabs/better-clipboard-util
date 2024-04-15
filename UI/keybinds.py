from tkinter import *
from tkinter import ttk

class Keybinds:
    def __init__(self, parent):
        KeybindsFrame = ttk.Frame(parent)
        KeybindsFrame.grid(column=0, row=0)
        kbLabel = ttk.Label(KeybindsFrame, text="[ Keybinds ]")
        kbLabel.grid(column=0, columnspan=2) 