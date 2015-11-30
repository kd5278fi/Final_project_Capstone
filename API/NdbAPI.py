
import requests
from Classes import FoodItem

class NdbAPI:

    def __init__(self):
        self.secret = "f9xkUkjirn4BIMQVyPczFkfvXWPU188r78wfVZdU"

    def getSearchResults(self, search):
        resultsDict = {}
        parameters = {"format":"json", "q":search, "sort":"r", "max":20, "offset":0, "api_key": self.secret}
        data = requests.get("api.nal.usda.gov/ndb/search/", params=parameters)
        results = data.json()
        for item in results['list']['item']:
            resultsDict[item['name']] = item['ndbno']

        return resultsDict

    def getFoodMeasurements(self, ndbno):
        measurementList = []
        data = requests.get("http://api.nal.usda.gov/ndb/reports/?ndbno=" + ndbno + "&type=b&format=json&api_key=" + self.secret)
        results = data.json()
        for item in results['report']['food']['nutrients'][0]['measures']:
            measurementList.append(item['label'])

        return measurementList

    def getFoodItem(self, ndbno, measurement, quantity):
        data = requests.get("http://api.nal.usda.gov/ndb/reports/?ndbno=" + ndbno + "&type=f&format=json&api_key=" + self.secret)
        results = data.json()
        # nutrients is list
        nutrients = results.get('report').get('food').get('nutrients')
        #  slice of nutrients is dictionary
        # print nutrients[0] #{u'group': u'Proximates', u'name': u'Water', u'nutrient_id': u'255', u'measures': [{u'eqv': 132.0, u'qty': 1.0, u'value': u'48.87', u'label': u'cup, diced'}, {u'eqv': 244.0, u'qty': 1.0, u'value': u'90.33', u'label': u'cup, melted'}, {u'eqv': 113.0, u'qty': 1.0, u'value': u'41.83', u'label': u'cup, shredded'}, {u'eqv': 28.35, u'qty': 1.0, u'value': u'10.50', u'label': u'oz'}, {u'eqv': 17.0, u'qty': 1.0, u'value': u'6.29', u'label': u'cubic inch'}, {u'eqv': 28.0, u'qty': 1.0, u'value': u'10.37', u'label': u'slice (1 oz)'}], u'value': u'37.02', u'unit': u'g'}
        # #get list
        # print nutrients[0]['measures'] # [{u'eqv': 132.0, u'qty': 1.0, u'value': u'48.87', u'label': u'cup, diced'}, {u'eqv': 244.0, u'qty': 1.0, u'value': u'90.33', u'label': u'cup, melted'}, {u'eqv': 113.0, u'qty': 1.0, u'value': u'41.83', u'label': u'cup, shredded'}, {u'eqv': 28.35, u'qty': 1.0, u'value': u'10.50', u'label': u'oz'}, {u'eqv': 17.0, u'qty': 1.0, u'value': u'6.29', u'label': u'cubic inch'}, {u'eqv': 28.0, u'qty': 1.0, u'value': u'10.37', u'label': u'slice (1 oz)'}]
        # #get value
        # print nutrients[0]['nutrient_id'] # 255 AS STRING!!!!!!!

        name = results.get('report').get('food')['name']
        group = results.get('report').get('food')['fg']
        calories = ""
        carbs = ""
        fats = ""
        proteins = ""
        sugers = ""


        for item in nutrients:
            if item['nutrient_id'] == "208":
                for nut in item['measures']:
                    if nut['label'] == measurement:
                        calories = nut['value']
            elif item['nutrient_id'] == "203":
                for nut in item['measures']:
                    if nut['label'] == measurement:
                        proteins = nut['value']
            elif item['nutrient_id'] == "204":
                for nut in item['measures']:
                    if nut['label'] == measurement:
                        fats = nut['value']
            elif item['nutrient_id'] == "205":
                for nut in item['measures']:
                    if nut['label'] == measurement:
                        carbs = nut['value']
            elif item['nutrient_id'] == "269":
                for nut in item['measures']:
                    if nut['label'] == measurement:
                        sugers = nut['value']

        foodStuff = FoodItem(ndbno, name, group, measurement, calories, carbs, fats, proteins, sugers, quantity)

        return foodStuff






