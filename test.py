# from tkinter import Tk, Label, Button, Frame
import tkinter as tk
import json

data = ["random clip"]

class MyFirstGUI:
    def __init__(self, master):
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

        self.label = tk.Label(dataframe, text="Clipboard: ", bg='gray')
        self.label.pack(padx=5, pady=5)

        # self.label2 = tk.Label(dataframe, text=json.dumps(data), bg='gray', wraplength=500)
        # self.label2.pack(padx=5, pady=5, anchor="w")

        scrollbar = tk.Scrollbar(dataframe)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.mylist = tk.Listbox(dataframe, yscrollcommand=scrollbar.set)
        for index, line in enumerate(data, start=1):
            self.mylist.insert(tk.END, str(index)+" >> "+str(line))

        self.mylist.pack(padx=0, pady=0, side=tk.LEFT, fill=tk.X, expand=1)
        scrollbar.config(command=self.mylist.yview)

        # myentry = tk.Entry(dataframe, textvariable=json.dumps(data), state='readonly')
        # myscroll = tk.Scrollbar(dataframe, orient='vertical', command=myentry.xview)
        # myentry.config(xscrollcommand=myscroll.set)
        #
        #
        # myentry.grid(row=1, sticky='ew')
        # myscroll.grid(row=2, sticky='ew')

        #fill=tk.X,

        self.current = tk.Label(back, text="Your clipboard on: dadadaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", bg='lightgray', wraplength=300)
        self.current.pack(padx=5, pady=5, anchor="w")

        self.newclip = tk.Label(back, text="aaaa", bg='lightgray', wraplength=300)
        self.newclip.pack(padx=5, pady=10, anchor="w")

        self.greet_button = tk.Button(back, text="Greet", command=self.greet)
        self.greet_button.pack(padx=5, pady=2, anchor="se", side=tk.RIGHT)

        self.close_button = tk.Button(back, text="Clear", command=self.clear)
        #self.close_button.grid(row=10, column=7, padx=10, pady=10)
        self.close_button.pack(padx=5, pady=2, anchor="se", side=tk.RIGHT)
        #padx=5, pady=2, anchor="ne"
        #self.label = tk.Label(dataframe, text=json.dumps(data), bg='gray')
        #self.label.pack(padx=5, pady=5, anchor="w")

        #mylist.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.X, expand=1)
        #scrollbar.config(command=mylist.yview)


        print(data)

    def greet(self):
        print("test")
        data.append("waww")
        self.mylist.delete(0, tk.END)
        for index, line in enumerate(data, start=1):
            self.mylist.insert(tk.END, str(index)+" >> "+str(line))

    def clear(self):
        global data
        self.mylist.delete(0, tk.END)
        data = []

root = tk.Tk()

my_gui = MyFirstGUI(root)
root.mainloop()