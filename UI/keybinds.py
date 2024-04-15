from tkinter import *
from tkinter import ttk
from tkinter import font
from clipboard import ClipboardContainer

class Keybinds:
    def __init__(self, parent, cb_container: ClipboardContainer):
        KeybindsFrame = ttk.Frame(parent)
        KeybindsFrame.grid(column=0, row=0)
        #set up style for label
        bold_font = font.Font(family="Helvetica", size=12, weight="bold")
        style = ttk.Style()
        style.configure('Bold.TLabel', font=bold_font)
        #create title label
        kbLabel = ttk.Label(KeybindsFrame, text="[ Keybinds ]", style="Bold.TLabel")
        kbLabel.grid(column=0, columnspan=2, padx=10, pady=10)




        
