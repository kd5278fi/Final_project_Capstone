
class FoodItem:

    #Object to store all information on a food item.

    def __init__(self, ndbNo, name, group, measurement, time, calories, CF, FF, PF, SF, quantity):
        #Primary key, Individual id number
        self.ndbNO = ndbNo
        # food item name
        self.name = name
        #food group, ie: dairy
        self.group = group
        #how this particular item is measured, ie: 1 cup
        self.measurement = measurement
        self.time = time
        # details of nutritional values
        self.calories = int(calories)
        self.carbs = int(CF)
        self.fats = int(FF)
        self.proteins = int(PF)
        self.sugars = int(SF)
        #how many of this item was consumed, to use for multiplying nutritional values
        self.quantity = int(quantity)

    def displayName(self):

        if self.quantity == 1:
            return self.name + " - " + str(self.quantity) + " " + self.measurement
        else :
            return self.name + " - " + str(self.quantity) + " " + self.measurement + "s"

    def calMod(self):
        return self.quantity * self.calories

    def carbMod(self):
        return self.quantity * self.carbs

    def fatMod(self):
        return self.quantity * self.fats

    def proMod(self):
        return self.quantity * self.proteins

    def sugMod(self):
        return self.quantity * self.sugars