#workaround for pyperclip's copy function not working

import pyperclip
import os

def copy(s):
    os.system(f"echo -n '{s}' | xclip -selection clipboard")

def paste():
    return pyperclip.paste()
