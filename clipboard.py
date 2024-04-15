import keyboard
import win32clipboard as winclip
import time
from collections import deque

#store in a .txt or something

class ClipboardContainer():
    def __init__(self):
        self.entries=deque(maxlen=9)
        self.callbacks=[]
    def add_to_clipboard(self):
        time.sleep(0.1)
        winclip.OpenClipboard()
        try:
            entry =  winclip.GetClipboardData()
            print(entry)
            self.entries.append(entry)
            self.notify_observers()
        except Exception as e:
            print("error reading clipboard:",e)
        finally:
            winclip.CloseClipboard()
    def notify_observers(self):
        for callback in self.callbacks:
            callback()
    def register_callback(self, callback):
        self.callbacks.append(callback)




def init_keybinds(clipboard_container: ClipboardContainer):
    def handle_ctrl_c():
        keyboard.send('ctrl+c')
        clipboard_container.add_to_clipboard()
    def open_clipboard():
        print("opened clipboard")

    keyboard.add_hotkey('ctrl+c', handle_ctrl_c, suppress=True)
    keyboard.add_hotkey('ctrl+v', open_clipboard, suppress=True)