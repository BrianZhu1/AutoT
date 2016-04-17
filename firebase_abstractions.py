import requests
import json

baseURL = "https://autotapp.firebaseio.com/"

# Helper functions to ease CRUD functions to DB.

def fetchMenu(companyName):
	return requests.get(baseURL + "menu.json").json()[companyName]

def fetchNumber(companyName):
	optionData = requests.get(baseURL + "directory.json").json()[companyName]
	if not optionData:
		return None
	else:
		return optionData

print fetchNumber('A T and T')