from Classes.FoodItem import FoodItem
from API.NdbAPI import *


# this class creates a new API object, and uses the search term to start building our information
class SearchController(object):

    ndbAPI = NdbAPI()

    def searchResults(self, searchText):
        results = SearchController.ndbAPI.getSearchResults(searchText)
        return results

    #TODO: Should this be where we put the next portion of our API calls? Take desired search term and create object.

    def measurements(self, number):
        results = SearchController.ndbAPI.getFoodMeasurements(number)
        return results