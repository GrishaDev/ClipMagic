#import pyperclip
import time
from pynput import keyboard
from multiprocessing import Queue
import threading
from jaraco import clipboard
import re
import tkinter as tk
from tkinter import messagebox
import os

# ==================== Variables ====================

appgui = None

data = []
dataforprint = []

invoker = keyboard.Controller()
COMBINATION = {keyboard.Key.ctrl_l}
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
PASTE = keyboard.Key.alt_l
COPY = 'c'

pastekeys = set()
copykeys = set()

currentsuffix = "Your clipboard is on: "
msgsuffix = ""
msg = ""
current = ""
strlimit = 30

# ==================== waw =========================

print("===== Magic Clip =====")
print("===== Press ESC to see current saved clipboard =====")
print("===== Press Ctrl + alt + number from 0 9 to use the clipboard you need =====")

# ==================== classes ====================

class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()
        print("quit try")
        os._exit(1)

    def run(self):
        global appgui
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        appgui = AppGui(self.root)
        self.root.mainloop()


class AppGui:
    def __init__(self, master):
        global msg, current

        self.master = master
        master.title("ClipMagic")
        master.pack_propagate(0)
        master.geometry("530x350")
        master.resizable(False, False)

        dataframe = tk.Frame(master=master, bg='gray')
        dataframe.pack_propagate(0)
        dataframe.pack(fill=tk.BOTH, expand=1)

        back = tk.Frame(master=master, bg='lightgray')
        back.pack_propagate(0)
        back.pack(fill=tk.BOTH, expand=1)

        self.title = tk.Label(dataframe, text="Clipboard: ", bg='gray')
        self.title.pack(padx=5, pady=5)

        scrollbar = tk.Scrollbar(dataframe)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.mylist = tk.Listbox(dataframe, yscrollcommand=scrollbar.set)
        for index, line in enumerate(data, start=1):
            self.mylist.insert(tk.END, str(index)+" >> "+str(line))

        self.mylist.pack(padx=0, pady=0, side=tk.LEFT, fill=tk.X, expand=1)
        scrollbar.config(command=self.mylist.yview)

        self.current = tk.Label(back, text=currentsuffix+current, bg='lightgray', wraplength=300)
        self.current.pack(padx=5, pady=5, anchor="w")

        self.message = tk.Label(back, text="Hello", bg='lightgray', wraplength=300)
        self.message.pack(padx=5, pady=10, anchor="w")

        self.help_button = tk.Button(back, text="Help", command=self.help)
        self.help_button.pack(padx=5, pady=2, anchor="se", side=tk.RIGHT)

        self.clear_button = tk.Button(back, text="Clear", command=self.clear)
        self.clear_button.pack(padx=5, pady=2, anchor="se", side=tk.RIGHT)

        first = clipboard.paste()
        print(first)

        if len(first) > 0:
            data.append(first)
        else:
            first = "Welcome"
            data.append(first)

        current = (first[:strlimit] + '..') if len(first) > strlimit else first
        msg = "Welcome"
        self.update()

    def help(self):
        print("hello")
        messagebox.showinfo("Help", "Press Ctrl + alt + number from 0 9 to use the clipboard you need")
        # data.append("waww")
        # self.mylist.delete(0, tk.END)
        # for index, line in enumerate(data, start=1):
        #     self.mylist.insert(tk.END, str(index)+" >> "+str(line))

    def clear(self):
        global data
        self.mylist.delete(0, tk.END)
        data = []

    def update(self):
        self.mylist.delete(0, tk.END)
        for index, line in enumerate(data, start=1):
            self.mylist.insert(tk.END, str(index) + " >> " + str(line))

        self.current.config(text=currentsuffix+current)
        self.message.config(text=msg)


# ==================== Methods ====================
def copy():
    global msg, current
    time.sleep(0.2)
    data.insert(0, clipboard.paste())
    if len(data) > 9:
        data.pop()
    print("'"+re.sub(r'[^a-zA-Z1-9 ]', '.', clipboard.paste())+"' added To clipboard list")
    clipo = clipboard.paste()
    content = (clipo[:strlimit] + '..') if len(clipo) > strlimit else clipo
    current = content
    msg = "'"+content+"' added To clipboard list"
    appgui.update()


def clip(num):
    global current
    time.sleep(0.2)
    if len(data) >= num:
        index = num - 1
        print("Your clipboard is on '"+re.sub(r'[^a-zA-Z1-9 ]', '.', data[index])+"'")
        clipboard.copy(data[index])
        content = (data[index][:strlimit] + '..') if len(data[index]) > strlimit else data[index]
        current = content
        appgui.update()


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
            msg=re.sub(r'[^a-zA-Z1-9 ]', '.', word)
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


app = App()
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print("da")
# =================================================================

# trash
# with invoker.pressed(keyboard.Key.ctrl_l):
#     invoker.press('v')
#     invoker.release('v')