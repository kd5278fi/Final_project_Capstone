
from View.ViewMain import *

#establish database and create tables if need be
db = Database()
db.setupTables()
#create root for Tkinter
root = Tk()
viewMain = ViewMain(master=root)
#starts main loop methods
viewMain.mainloop()

#exit errors occur when destroying in Main
#viewMain.destroy()
#root.destroy()