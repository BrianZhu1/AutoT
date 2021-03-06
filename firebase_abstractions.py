import requests
import json

baseURL = "https://autotapp.firebaseio.com/"

# Helper functions to ease CRUD functions to DB.

def fetchMenu(companyNumber):
	optionData = requests.get(baseURL + "menu.json").json()
	if companyNumber in optionData:
		return optionData[companyNumber]
	else:
		return None

def fetchNumber(companyName):
	optionData = requests.get(baseURL + "directory.json").json()
	if companyName in optionData:
		return optionData[companyName]
	else:
		return None

print fetchNumber('hello')