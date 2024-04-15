from tkinter import *
from tkinter import ttk
from tkinter import font

class Keybinds:
    def __init__(self, parent):
        KeybindsFrame = ttk.Frame(parent)
        KeybindsFrame.grid(column=0, row=0)
        #set up style for label
        bold_font = font.Font(family="Helvetica", size=12, weight="bold")
        style = ttk.Style()
        style.configure('Bold.TLabel', font=bold_font)
        #create title label
        kbLabel = ttk.Label(KeybindsFrame, text="[ Keybinds ]", style="Bold.TLabel")
        kbLabel.grid(column=0, columnspan=2)
        
