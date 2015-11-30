from Tkinter import *



top = Tk()
top.geometry('250x150')
label = Label(top, text='Hello World', font='Helvetica -12 bold')
label.pack(fill=Y, expand=1)

def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())

scale = Scale(top, from_=10, to=40, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=1)

# activeforeground is the set up color, active background shows when the button is pushed.
quit=Button(top, text='Quit', command=top.quit, activeforeground='white', activebackground='red')
quit.pack()

mainloop()