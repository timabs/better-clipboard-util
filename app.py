import clipboard as cb
import keyboard as kb
from tkinter import *
from tkinter import ttk
import UI.ui as ui

def main(): 
    try:
        cb.init_keybinds()
        root = Tk()
        ui.MainUI(root)
        root.mainloop()
    except Exception as e:
        print("An error occured:",e)
    finally:
        kb.wait('esc')
    
if __name__ == "__main__":
    main()