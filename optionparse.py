# optionCorpus = requests.get('https://autotapp.firebaseio.com/results.json').json()
optionsCorpus = "Press one for English, Press 2 for spanish and press 3 for French"

optionList = filter(None, [option.strip(" , or and").split()[1:] for option in optionsCorpus.lower().split("press")])
print optionList