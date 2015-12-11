from Classes.FoodItem import FoodItem
from API.NdbAPI import *
from Database.Database import *

# this class creates a new API object, and uses the search term to start building our information
class MiddleMan(object):

    ndbAPI = NdbAPI()
    db = Database()
    foodList = []

    def searchResults(self, searchText):
        results = MiddleMan.ndbAPI.getSearchResults(searchText)
        return results


    def measurements(self, number):
        results = MiddleMan.ndbAPI.getFoodMeasurements(number)
        return results

    def getItem(self, ndbno, measurement, quantity, time):
        results = MiddleMan.ndbAPI.getFoodItem(ndbno, measurement, quantity, time)
        self.foodList.append(results)
        return results

    def saveDay(self):
        MiddleMan.db.save(self.foodList)

    def loadDay(self, date):
        results = MiddleMan.db.selectAllFromDate(date)
        return results
