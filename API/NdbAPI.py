
import requests


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
        data = requests.get("http://api.nal.usda.gov/ndb/reports/?ndbno=" + ndbno + "&type=b&format=json&api_key=" + self.secret)









