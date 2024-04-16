from tkinter import *
from tkinter import ttk
from tkinter import font
from clipboard import ClipboardContainer

class Keybinds:
    def __init__(self, parent, cb_container: ClipboardContainer):
        self.cb_container = cb_container
        self.cb_container.register_callback(self.render_entries)
        self.cb_length = 10
        self.KeybindsFrame = ttk.Frame(parent)
        self.KeybindsFrame.grid(column=0, row=0)
        self.clipboard_labels = []
        self.keybindSelectors=[]
        #set up style for label
        bold_font = font.Font(family="Helvetica", size=12, weight="bold")
        style = ttk.Style()
        style.configure('Bold.TLabel', font=bold_font)
        #create title label
        self.kbLabel = ttk.Label(self.KeybindsFrame, text="[ Keybinds ]", style="Bold.TLabel")
        self.kbLabel.grid(column=0, columnspan=2, padx=10, pady=10)
        #set up labels
        for i in range(self.cb_length):
            self.entryLabel = ttk.Label(self.KeybindsFrame, text='" "', width=20)
            self.entryLabel.grid(padx=6, pady=6, column=0, row=i+1)
            self.clipboard_labels.append(self.entryLabel)
            self.keybindSelector = ttk.Entry(self.KeybindsFrame, width=10)
            self.keybindSelector.grid(column=1, row=i+1)
            self.keybindSelectors.append(self.keybindSelector)
    def render_entries(self):
        clipboard_entries = self.cb_container.entries
        for i, entry in enumerate(clipboard_entries):
            self.clipboard_labels[i].config(text=f'"{entry}"')

            









        
