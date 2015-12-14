from Tkinter import *
import tkMessageBox
import ttk
import datetime
from Controller.MiddleMan import *
from Classes.Mbox import *
from Classes.FoodPlan import *

class ViewMain(Frame):

    control = MiddleMan()
    #levels taken from: http://www.dietitian.com/calcbody.php
    plan = FoodPlan(1200, 150, 40, 60, 64)
    BreakCal = 0
    LunchCal = 0
    SnackCal = 0
    DinnerCal = 0
    TotalCal = 0
    TotalProtein = 0
    TotalCarbs = 0
    TotalFats = 0
    TotalSugar = 0

    def __init__(self, master = None, date = datetime.datetime.now()):
        Frame.__init__(self, master)
        self.grid(column=0, row=0, sticky=(N,W,E,S))
        self.master.title("Food Journal - " + date.strftime("%x"))
        self.insertDisplayFrames()
        self.insertEntryFrames()
        self.insertButtons()
        self.makeAllPadded()
        self.loadDay()

    def insertDisplayFrames(self):
        self.foodLabel = ttk.Label(self, text="Food Item").grid(column=1, row=0)
        self.amountLabel = ttk.Label(self, text='Amount').grid(column=1, row=1)
        self.timeLabel = ttk.Label(self, text="Time").grid(column=1, row=2)
        self.firstSep = ttk.Separator(self)
        self.firstSep.grid(column=0, row=3, sticky=(W, N, E),columnspan=6)
        self.BreakfastList = Listbox(self, height=3, width=80)
        self.BreakfastList.grid(column=0, row=4, columnspan=4, sticky=W)
        self.breakCals = ttk.Label(self, text="Breakfast Calories: " + str(self.BreakCal))
        self.breakCals.grid(column=4, row=4)
        self.secondSep = ttk.Separator(self).grid(column=0, row=5, sticky=(W, N, E), columnspan=5)
        self.LunchList = Listbox(self, height=3, width=80)
        self.LunchList.grid(column=0, row=6, columnspan=2, sticky=W)
        self.lunchCals = ttk.Label(self, text="Lunch Calories: " + str(self.LunchCal))
        self.lunchCals.grid(column=4, row=6)
        self.thirdSep = ttk.Separator(self).grid(column=0, row=7, sticky=(W, N, E), columnspan=5)
        self.SnackList = Listbox(self, height=3, width=80)
        self.SnackList.grid(column=0, row=8, columnspan=2, sticky=W)
        self.snackCals = ttk.Label(self, text="Snack Calories: " + str(self.SnackCal))
        self.snackCals.grid(column=4, row=8)
        self.fourthSep = ttk.Separator(self).grid(column=0, row=9, sticky=(W, N, E), columnspan=5)
        self.DinnerList = Listbox(self, height=3, width=80)
        self.DinnerList.grid(column=0, row=10, columnspan=2, sticky=W)
        self.dinnerCals = ttk.Label(self, text="Dinner Calories: " + str(self.DinnerCal))
        self.dinnerCals.grid(column=4, row=10)
        self.finalSep = ttk.Separator(self).grid(column=0, row=11, sticky=(W, N, E), columnspan=5)
        self.totalCalories = ttk.Label(self, text="Total calories: " + str(self.TotalCal))
        self.totalCalories.grid(column=0, row=12)
        self.totalProtein = ttk.Label(self, text="Total protein: " + str(self.TotalProtein))
        self.totalProtein.grid(column=1, row=12)
        self.totalCarbs = ttk.Label(self, text="Total carbohydrates: " + str(self.TotalCarbs))
        self.totalCarbs.grid(column=2, row=12)
        self.totalFats = ttk.Label(self, text="Total fats: " + str(self.TotalFats))
        self.totalFats.grid(column=3, row=12)
        self.totalSugar = ttk.Label(self, text="Total sugars: " + str(self.TotalSugar))
        self.totalSugar.grid(column=4, row=12)

    def insertEntryFrames(self):
        eatingList = ['Breakfast', 'Lunch', 'Snack', 'Dinner']
        self.foodEntry = ttk.Entry(self,width=23)
        self.foodEntry.grid(column=0, row=0)
        self.amountEntry = ttk.Combobox(self, values = [])
        self.amountEntry.grid(column=0, row=1)
        self.timeEntry = ttk.Combobox(self, values=eatingList)
        self.timeEntry.grid(column=0, row=2)
        self.quantEntry = ttk.Entry(self)
        self.quantEntry.grid(column=2, row=1)

    def insertButtons(self):
        self.searchButton = ttk.Button(self, text='Search', command=self.clickSearch).grid(column=4, row=0)
        self.addButton = ttk.Button(self, text="Add Item", command=self.addItem).grid(column=4, row=2)
        self.quitButton = ttk.Button(self, text='Quit', command=self.saveDay). grid(column=4, row=13)

    def makeAllPadded(self):
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5, ipadx=5, ipady=5)

    def clickSearch(self):

        searchText = self.foodEntry.get()

        #get dictionary
        self.result = self.control.searchResults(searchText)
        self.window=Mbox(self.master, list=self.result)
        self.master.wait_window(self.window.top)
        self.foodEntry.delete(0,END)
        self.foodEntry.insert(END, self.window.value)
        # result[self.window.value] - food number
        measurements = self.control.measurements(self.result[self.window.value])
        self.amountEntry.config(values=measurements)

        self.makeAllPadded()

    def addItem(self):

        foodObject = self.control.getItem(self.result[self.window.value], self.amountEntry.get(), self.quantEntry.get(), self.timeEntry.get())
        self.findTimeSlot(foodObject)
        self.adjustCaloriesForTime(foodObject)
        self.adjustNutrients(foodObject)
        self.clearEntries()

        # self.mess = tkMessageBox.showinfo("Object info", foodObject.ndbNo + "\n" + foodObject.name + "\n" +  foodObject.group + "\n" +  foodObject.measurement + "\n" +  foodObject.time + "\n" +  str(foodObject.calories) + "\n" + str(foodObject.carbs) + "\n" +  str(foodObject.fats) + "\n" +  str(foodObject.proteins) + "\n" +  str(foodObject.sugars) + "\n" +  str(foodObject.quantity))

    def findTimeSlot(self, object):
        if object.time == "Breakfast":
            self.BreakfastList.insert(END, object.displayName())
        elif object.time == "Lunch":
            self.LunchList.insert(END, object.displayName())
        elif object.time == "Snack":
            self.SnackList.insert(END, object.displayName())
        elif object.time == "Dinner":
            self.DinnerList.insert(END, object.displayName())

    def adjustCaloriesForTime(self, object):
        if object.time == "Breakfast":
            self.BreakCal += object.calMod()
            self.breakCals.config(text="Breakfast Calories: " + str(self.BreakCal))
        elif object.time == "Lunch":
            self.LunchCal += object.calMod()
            self.lunchCals.config(text="Lunch Calories: " + str(self.LunchCal))
        elif object.time == "Snack":
            self.SnackCal += object.calMod()
            self.snackCals.config(text="Snack Calories: " + str(self.SnackCal))
        elif object.time == "Dinner":
            self.DinnerCal += object.calMod()
            self.dinnerCals.config(text="Dinner Calories: " + str(self.DinnerCal))

    def adjustNutrients(self, object):
        self.TotalCal += object.calMod()
        self.totalCalories.config(text="Total Calories: " + str(self.TotalCal))
        if self.TotalCal > self.plan.calorieGoal:
            self.totalCalories.config(foreground='red')
        self.TotalFats += object.fatMod()
        self.totalFats.config(text="Total Fats: " + str(self.TotalFats))
        if self.TotalFats > self.plan.fatsGoal:
            self.totalFats.config(foreground='red')
        self.TotalCarbs += object.carbMod()
        self.totalCarbs.config(text="Total Carbohydrates: " + str(self.TotalCarbs))
        if self.TotalCarbs > self.plan.carbGoal:
            self.totalCarbs.config(foreground='red')
        self.TotalSugar += object.sugMod()
        self.totalSugar.config(text="Total Sugars: " + str(self.TotalSugar))
        if self.TotalSugar > self.plan.sugarGoal:
            self.totalSugar.config(foreground='red')
        self.TotalProtein += object.proMod()
        self.totalProtein.config(text="Total Fats: " + str(self.TotalProtein))
        if self.TotalProtein > self.plan.proteinGoal:
            self.totalProtein.config(foreground='red')

    def loadDay(self):
        foodLoad = self.control.loadDay(datetime.date.today())
        for item in foodLoad:
            food = FoodItem(item[1], item[2], item[3], item[4], item[5],item[6], item[7], item[8], item[9], item[10], item[11])

            # TUPLE: (2, 1001, u'corn', u'starch', u'cup', u'dinner', 100, 100, 90, 90, 80)
            self.findTimeSlot(food)
            self.adjustCaloriesForTime(food)
            self.adjustNutrients(food)

    def saveDay(self):

        if tkMessageBox.askyesno("Save", "Would you like to save all of your data?"):
            self.mess = tkMessageBox.showinfo("object info", self.control.saveDay())
            self.master.destroy()
        else:
            exit()

    def clearEntries(self):
        self.foodEntry.delete(0, END)
        self.amountEntry.delete(0, END)
        self.amountEntry.config(values=[])
        self.timeEntry.delete(0, END)
        self.foodEntry.focus()



