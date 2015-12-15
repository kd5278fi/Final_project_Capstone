from Classes.FoodItem import FoodItem
from API.NdbAPI import *
from Database.Database import *

# this class creates a new API object, and uses the search term to start building our information
class MiddleMan(object):

    ndbAPI = NdbAPI()
    db = Database()
    foodList = []

    #takes search texts and uses ndbAPI to find all related food items. Returns list.
    def searchResults(self, searchText):
        results = MiddleMan.ndbAPI.getSearchResults(searchText)
        return results

    #takes ndbNumber of selected item and gives it to the ndbAPI to find the types of measurements associated with the item
    def measurements(self, number):
        results = MiddleMan.ndbAPI.getFoodMeasurements(number)
        return results

    #uses ndbNumber to search for info on food item, and builds a food object with nutrient info.
    def getItem(self, ndbno, measurement, quantity, time):
        results = MiddleMan.ndbAPI.getFoodItem(ndbno, measurement, quantity, time)
        #adds food item to Middleman list so it can be saved later
        self.foodList.append(results)
        return results

    #If user chooses to save info, takes the food list and sends it to the database class which saves all the info
    def saveDay(self):
        MiddleMan.db.save(self.foodList)
        #test to see ndbNumber
        # list = []
        # for food in self.foodList:
        #     list.append(food.ndbNO)
        # return list

    #pulls all info from table if it exists for the current date
    def loadDay(self, date):
        results = MiddleMan.db.selectAllFromDate(date)
        return results
