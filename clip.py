#import pyperclip
import time
from pynput import keyboard
from multiprocessing import Queue
from jaraco import clipboard
import re


# ==================== Variables ====================

data = ["random clip"]
dataforprint = []

invoker = keyboard.Controller()
COMBINATION = {keyboard.Key.ctrl_l}
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
PASTE = keyboard.Key.alt_l
COPY = 'c'

pastekeys = set()
copykeys = set()

a = 'add new sentence with this word 1234gdfgre'
print(re.sub(r'[^a-zA-Z1-9 ]', '?', a))

# ==================== waw =========================

print("===== Magic Clip =====")
print("===== Press ESC to see current saved clipboard =====")
print("===== Press Ctrl + alt + number from 0 9 to use the clipboard you need =====")


# ==================== Methods ====================

def copy():
    time.sleep(0.2)
    data.insert(0, clipboard.paste())
    if len(data) > 9:
        data.pop()
    print("'"+re.sub(r'[^a-zA-Z1-9 ]', '?', clipboard.paste())+"' added To clipboard list")


def clip(num):
    time.sleep(0.2)
    if len(data) >= num:
        index = num - 1
        print("Your clipboard is on '"+re.sub(r'[^a-zA-Z1-9 ]', '?', data[index])+"'")
        clipboard.copy(data[index])


def on_press(key):
    global dataforprint
    try:
        btn = key.char
    except AttributeError:
        btn = key
    num = 1
    if btn in COMBINATION:
        pastekeys.add(key)
        copykeys.add(key)
    if btn is PASTE or btn in NUMBERS:
        pastekeys.add(key)
        if btn in NUMBERS:
            num = int(btn)
    if btn is COPY:
        copykeys.add(key)
    if len(pastekeys) >= 3:
        clip(num)
        pastekeys.clear()
    elif len(copykeys) >= 2:
        copy()
        copykeys.clear()
    if key == keyboard.Key.esc:
        for word in data:
            msg=re.sub(r'[^a-zA-Z1-9 ]', '?', word)
            dataforprint.append(msg)
        print(dataforprint)
        dataforprint = []


def on_release(key):
    try:
        pastekeys.remove(key)
    except KeyError:
        pass
    try:
        copykeys.remove(key)
    except KeyError:
        pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


# =================================================================

# trash
# with invoker.pressed(keyboard.Key.ctrl_l):
#     invoker.press('v')
#     invoker.release('v')