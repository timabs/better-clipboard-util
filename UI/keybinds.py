from tkinter import *
from tkinter import ttk
from tkinter import font
from clipboard import ClipboardContainer

class Keybinds:
    def __init__(self, parent, cb_container: ClipboardContainer):
        self.cb_container = cb_container
        self.cb_container.register_callback(self.render_entries)
        self.KeybindsFrame = ttk.Frame(parent)
        self.KeybindsFrame.grid(column=0, row=0)
        #set up style for label
        bold_font = font.Font(family="Helvetica", size=12, weight="bold")
        style = ttk.Style()
        style.configure('Bold.TLabel', font=bold_font)
        #create title label
        self.kbLabel = ttk.Label(self.KeybindsFrame, text="[ Keybinds ]", style="Bold.TLabel")
        self.kbLabel.grid(column=0, columnspan=2, padx=10, pady=10)
        self.render_entries()
    def render_entries(self):
        for label in self.KeybindsFrame.winfo_children():
            if isinstance(label, ttk.Label) and label != self.kbLabel:
                label.destroy()
        for entry in self.cb_container.entries:
            label = ttk.Label(self.KeybindsFrame, text=f'"{entry}"')
            label.grid(padx=12, pady=12)





        
