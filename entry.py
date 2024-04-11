import tkinter as tk
from tkinter import ttk
import clipboard as cb
import keyboard as kb

def main():
    try:
        cb.init_keybinds()
    except Exception as e:
        print("An error occured:",e)
    finally:
        kb.wait('esc')
    
if __name__ == "__main__":
    main()