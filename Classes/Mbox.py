from Tkinter import *
import sys

class Mbox(object):

    def __init__(self, master, list=None):
        top=self.top=Toplevel(master)
        self.label = Label(top, text="Please pick a food item:")
        self.label.pack()
        self.scroll = Scrollbar(top, orient=VERTICAL)
        self.listObj = Listbox(top, width=40, selectmode=SINGLE, yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.listObj.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.listObj.pack(side=LEFT, fill=BOTH, expand=1)
        for key in list:
            self.listObj.insert(END, key)
        self.button = Button(top, text="ok", command=self.cleanup)
        self.button.pack()

    def cleanup(self):
        self.value=self.listObj.get(self.listObj.curselection())
        self.top.destroy()