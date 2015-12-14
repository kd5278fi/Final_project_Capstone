
import requests
from Classes.FoodItem import *
from API.keys import *

# this class will initialize and control the primary API object
class NdbAPI:

    def __init__(self):
        self.secret = key

    # My project will have a feature that allows a person to search for a term and see a list of choices that
    #are closest to their search term. The following method uses the API's search function to make this list
    def getSearchResults(self, search):
        #stores the results in a dictionary so when the user chooses the one they want, we also get the items
        #corresponding database identifier
        resultsDict = {}
        #To correctly use a search term with multiple words, we use Requests parameter ability to take a
        #term and turn it into usable URL strings. Because the parameter must include ALL parameters instead
        #of one, we include all options for this method only.
        parameters = {"format":"json", "q":search, "sort":"r", "max":20, "offset":0, "api_key": self.secret}
        #Rewuest module takes the url and the parameters and stores the Json response. If we queried what
        #data is right now, it would only give us a code with a response from the web server
        #TODO: use the web response to try/catch for error handeling
        data = requests.get("http://api.nal.usda.gov/ndb/search/", params=parameters)
        #take the results from json and turn into dictionary
        results = data.json()
        #runs through dictionary and pulls all the names and their database numbers
        for item in results['list']['item']:
            #adds to resultsDictionary
            resultsDict[item['name']] = item['ndbno']
        #returns Dictionary Object
        return resultsDict


    #Once an item is selected, a drop down menu will be populated with the measurement types included in the web
    #database for that item. This method calls the API to look up the selected food item, search for the measurement
    #types, and return a list with those strings.
    def getFoodMeasurements(self, ndbno):
        #Blank list
        measurementList = []
        data = requests.get("http://api.nal.usda.gov/ndb/reports/?ndbno=" + ndbno + "&type=b&format=json&api_key=" + self.secret)
        results = data.json()
        #takes the first occurrence of the nutrient break down (index 0) and reads all the measurements included. These
        #measurements are the exact same for all indexes, so we only read one to get the list.
        for item in results['report']['food']['nutrients'][0]['measures']:
            #Adds label of measurement to measurementList
            measurementList.append(item['label'])
        #returns list object
        return measurementList


    #After all fields are complete and the ADD button is pushed, we make one last call to the API using the database
    #number to get all relevant information and create a food object to store on the SQL database
    def getFoodItem(self, ndbno, measurement, quantity, time):
        data = requests.get("http://api.nal.usda.gov/ndb/reports/?ndbno=" + ndbno + "&type=f&format=json&api_key=" + self.secret)
        results = data.json()
        # Eac time we call .get on a dictionary, it returns a new dictionary from the first dictionary's children. Each
        #time we make a dictionary, we keep traveling down the chain until we have a base dictionary we call pull
        #nutritonal info from.
        nutrients = results.get('report').get('food').get('nutrients')
        #  slice of nutrients is dictionary
        # print nutrients[0] #{u'group': u'Proximates', u'name': u'Water', u'nutrient_id': u'255', u'measures': [{u'eqv': 132.0, u'qty': 1.0, u'value': u'48.87', u'label': u'cup, diced'}, {u'eqv': 244.0, u'qty': 1.0, u'value': u'90.33', u'label': u'cup, melted'}, {u'eqv': 113.0, u'qty': 1.0, u'value': u'41.83', u'label': u'cup, shredded'}, {u'eqv': 28.35, u'qty': 1.0, u'value': u'10.50', u'label': u'oz'}, {u'eqv': 17.0, u'qty': 1.0, u'value': u'6.29', u'label': u'cubic inch'}, {u'eqv': 28.0, u'qty': 1.0, u'value': u'10.37', u'label': u'slice (1 oz)'}], u'value': u'37.02', u'unit': u'g'}
        # #get list
        # print nutrients[0]['measures'] # [{u'eqv': 132.0, u'qty': 1.0, u'value': u'48.87', u'label': u'cup, diced'}, {u'eqv': 244.0, u'qty': 1.0, u'value': u'90.33', u'label': u'cup, melted'}, {u'eqv': 113.0, u'qty': 1.0, u'value': u'41.83', u'label': u'cup, shredded'}, {u'eqv': 28.35, u'qty': 1.0, u'value': u'10.50', u'label': u'oz'}, {u'eqv': 17.0, u'qty': 1.0, u'value': u'6.29', u'label': u'cubic inch'}, {u'eqv': 28.0, u'qty': 1.0, u'value': u'10.37', u'label': u'slice (1 oz)'}]
        # #get value
        # print nutrients[0]['nutrient_id'] # 255 AS STRING!!!!!!!

        #setting up variables for our food object
        name = results.get('report').get('food')['name']
        group = results.get('report').get('food')['fg']
        calories = 0
        carbs = 0
        fats = 0
        proteins = 0
        sugars = 0


        #this portion runs through our nutrients dictionary, looks at the nutrient ID's, selects the ones we want then
        #assings the corresponding variable with the value from the dictionary.
        for i in range(0, len(results.get('report').get('food').get('nutrients'))):
            if results.get('report').get('food').get('nutrients')[i].get('nutrient_id') == 208:
                for b in range(0,len(results.get('report').get('food').get('nutrients')[i].get('measures'))):
                    if results.get('report').get('food').get('nutrients')[i].get('measures')[b].get('label') == measurement:
                       calories = results.get('report').get('food').get('nutrients')[i].get('measures')[b].get("value")
            if results.get('report').get('food').get('nutrients')[i].get('nutrient_id') == 203:
                for b in range(0,len(results.get('report').get('food').get('nutrients')[i].get('measures'))):
                    if results.get('report').get('food').get('nutrients')[i].get('measures')[b].get('label') == measurement:
                       proteins = results.get('report').get('food').get('nutrients')[i].get('measures')[b].get("value")
            if results.get('report').get('food').get('nutrients')[i].get('nutrient_id') == 204:
                for b in range(0,len(results.get('report').get('food').get('nutrients')[i].get('measures'))):
                    if results.get('report').get('food').get('nutrients')[i].get('measures')[b].get('label') == measurement:
                       fats = results.get('report').get('food').get('nutrients')[i].get('measures')[b].get("value")
            if results.get('report').get('food').get('nutrients')[i].get('nutrient_id') == 205:
                for b in range(0,len(results.get('report').get('food').get('nutrients')[i].get('measures'))):
                    if results.get('report').get('food').get('nutrients')[i].get('measures')[b].get('label') == measurement:
                       carbs = results.get('report').get('food').get('nutrients')[i].get('measures')[b].get("value")
            if results.get('report').get('food').get('nutrients')[i].get('nutrient_id') == 269:
                for b in range(0,len(results.get('report').get('food').get('nutrients')[i].get('measures'))):
                    if results.get('report').get('food').get('nutrients')[i].get('measures')[b].get('label') == measurement:
                       sugars = results.get('report').get('food').get('nutrients')[i].get('measures')[b].get("value")



        #Builds new food object
        foodStuff = FoodItem(ndbno, name, group, measurement, time, calories, carbs, fats, proteins, sugars, quantity)

        #returns food object
        return foodStuff






