from Classes.FoodItem import FoodItem
from API.NdbAPI import *


# this class creates a new API object, and uses the search term to start building our information
class SearchController(object):

    ndbAPI = NdbAPI()

    def searchResults(self, searchText):
        results = SearchController.ndbAPI.getSearchResults(searchText)

        # returns the list of items a user can choose from
        # TODO: Test this so we know the output is correct, include multi-word searches
        return results

    #TODO: Should this be where we put the next portion of our API calls? Take desired search term and create object.
