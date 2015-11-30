from Tkinter import *
import ttk
import datetime

def add(*args):
    try:
        foodstring = food_item.get()
        timestring = time.get()
        amountstring = amount.get()
        entry.set(amountstring + " " +foodstring + " " +timestring)
    except ValueError:
        pass

now = datetime.datetime.now()
root = Tk()
#Add current date
root.title("Food Journal - " + now.strftime('%x'))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame = ttk.Frame(root, padding=(3, 3, 12, 12))
frame.grid(column=0, row=0, sticky=(N, W, E, S))
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.rowconfigure(3, weight=1)
frame.rowconfigure(4, weight=1)

food_item = StringVar()
amount = StringVar()
time = StringVar()
entry = StringVar()
food_amounts = ['1 cup', '1 slice', '3 grams']
eating_times = ['Breakfast', 'Lunch', 'Snack', 'Dinner']

food_entry = ttk.Entry(frame, textvariable=food_item, width=23)
food_entry.grid(column=0, row=0, sticky=(N, W), pady=5, padx=5)

food_amount_box = ttk.Combobox(frame, textvariable=amount, values=food_amounts)
food_amount_box.grid(column=0, row=1, pady=5, padx=5)

food_time_box = ttk.Combobox(frame, textvariable=time, values=eating_times)
food_time_box.grid(column=0, row=2, pady=5, padx=5)

ttk.Button(frame, text='Add Item', command=add).grid(column=2, row=2)

ttk.Label(frame, text="Food Item").grid(column=1, row=0, sticky=N)
ttk.Label(frame, text='Amount').grid(column=1, row=1)
ttk.Label(frame, text='Time').grid(column=1, row=2)
ttk.Label(frame, textvariable = entry).grid(column=0, row=4)
ttk.Separator(frame).grid(column =0, row=3, sticky=(W, N, E), columnspan=3)


for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)
food_entry.focus()
root.bind('<Return>', add)
root.mainloop()


