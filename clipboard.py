import keyboard
import win32clipboard as winclip
import time
from collections import deque

clipboard = deque(maxlen=10)
def add_to_clipboard():
    time.sleep(0.1)
    winclip.OpenClipboard()
    try:
        entry =  winclip.GetClipboardData()
        clipboard.append(entry)
        print(clipboard)
    except Exception as e:
        print("error reading clipboard:",e)
    finally:
        winclip.CloseClipboard()

def open_clipboard():
    print("opened clipboard")

def init_keybinds():
    def handle_ctrl_c():
        keyboard.send('ctrl+c')
        add_to_clipboard()

    keyboard.add_hotkey('ctrl+c', handle_ctrl_c, suppress=True)
    keyboard.add_hotkey('ctrl+v', open_clipboard, suppress=True)