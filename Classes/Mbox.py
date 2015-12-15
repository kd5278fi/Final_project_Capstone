from Tkinter import *
import sys

#Derived class for a message box which takes list of items and displays for user choice
class Mbox(object):

    def __init__(self, master, list=None):
        #new frame pop-up
        top = self.top = Toplevel(master)
        #add label
        self.label = Label(top, text="Please pick a food item:")
        self.label.pack()
        #add scrollbar
        self.scroll = Scrollbar(top, orient=VERTICAL)
        #add listbox and connect to scroll bar
        self.listObj = Listbox(top, width=40, selectmode=SINGLE, yscrollcommand=self.scroll.set)
        #configure scroll bar actions
        self.scroll.config(command=self.listObj.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.listObj.pack(side=LEFT, fill=BOTH, expand=1)
        #inserts all objects to list
        for value in list:
            self.listObj.insert(END, value)
        #add ok button, connect to clean up method
        self.button = Button(top, text="ok", command=self.cleanup)
        self.button.pack()

    def cleanup(self):
        #saves selection for use in main frame
        self.value = self.listObj.get(self.listObj.curselection())
        # self.value2 = list["'" + self.listObj.get(self.listObj.curselection()) + "'"]
        self.top.destroy()
