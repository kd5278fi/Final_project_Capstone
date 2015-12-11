
from View.ViewMain import *

db = Database()
db.setupTables()
root = Tk()
viewMain = ViewMain(master=root)
viewMain.mainloop()

#viewMain.destroy()
#root.destroy()