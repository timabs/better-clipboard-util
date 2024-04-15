import clipboard
import keyboard as kb
from tkinter import *
from tkinter import ttk
import UI.ui as ui

def main(): 
    try:
        cb = clipboard.ClipboardContainer()
        root = Tk()
        ui.MainUI(root, cb)
        clipboard.init_keybinds(cb)
        root.mainloop()
    except Exception as e:
        print("An error occured:",e)
    finally:
        kb.wait('esc')
    
if __name__ == "__main__":
    main()