
class FoodItem:

    #Object to store all information on a food item.

    def __init__(self, ndbNo, name, group, measurement, time, calories, CF, FF, PF, SF, quantity):
        #Primary key, Individual id number
        self.ndbNo = ndbNo
        # food item name
        self.name = name
        #food group, ie: dairy
        self.group = group
        #how this particular item is measured, ie: 1 cup
        self.measurement = measurement
        self.time = time
        # details of nutritional values
        self.calories = calories
        self.carbs = CF
        self.fats = FF
        self.proteins = PF
        self.sugars = SF
        #how many of this item was consumed, to use for multiplying nutritional values
        self.quantity = quantity

    def displayName(self):
        return self.measurement + " " + self.name

#TODO: create methods for controlling object.