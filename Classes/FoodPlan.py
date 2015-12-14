
class FoodPlan:

    #Stores all of the goals for nutrient intake

    def __init__(self, cals, carbs, fats, pros, sugars):
        self.calorieGoal = cals
        self.carbGoal = carbs
        self.fatsGoal = fats
        self.proteinGoal = pros
        self.sugarGoal = sugars

    def displayText(self):
        return "Calorie Goal: " + str(self.calorieGoal) + '\nProtein Goal: ' + str(self.proteinGoal) + '\nCarbohydrate Goal: ' + str(self.carbGoal) +\
                '\nFats Goal: ' + str(self.fatsGoal) + '\nSugar Goal: ' + str(self.sugarGoal)