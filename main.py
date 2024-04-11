import tkinter as tk
from tkinter import ttk
import win32clipboard as clip

def main():
    try:
        clip.OpenClipboard()
        if clip.IsClipboardFormatAvailable(clip.CF_TEXT):
            data = clip.GetClipboardData()
            print("Clipboard contains text:",data)
        else:
            print("nope")
    except Exception as e:
        print("An error occured:",e)
    finally:
        clip.CloseClipboard()
    
if __name__ == "__main__":
    main()