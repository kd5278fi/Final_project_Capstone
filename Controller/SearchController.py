from Classes.FoodItem import FoodItem
from API.NdbAPI import *


# this class creates a new API object, and uses the search term to start building our information
class SearchController(object):

    ndbAPI = NdbAPI()

    def searchResults(self, searchText):
        results = SearchController.ndbAPI.getSearchResults(searchText)
        return results


    def measurements(self, number):
        results = SearchController.ndbAPI.getFoodMeasurements(number)
        return results

    def getItem(self, ndbno, measurement, quantity, time):
        results = SearchController.ndbAPI.getFoodItem(ndbno, measurement, quantity, time)
        return results