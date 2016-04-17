emulated = ["press 1 to do this, press 2 to do that, or press 3 to do both", \
    "press 1 to make up something, press 2 to make up something else, or press 3 to do something weird",
    "press 1 to speak spanish, press 2 to speak english", "press 1 to do this, press 2 to do that, or press 3 to do both", \
    "press 1 to make up something, press 2 to make up something else, or press 3 to do something weird",
    "press 1 to speak spanish, press 2 to speak english", "press 1 to do this, press 2 to do that, or press 3 to do both", \
    "press 1 to make up something, press 2 to make up something else, or press 3 to do something weird",
    "press 1 to speak spanish, press 2 to speak english", "press 1 to do this, press 2 to do that, or press 3 to do both", \
    "press 1 to make up something, press 2 to make up something else, or press 3 to do something weird",
    "press 1 to speak spanish, press 2 to speak english", "press 1 to do this, press 2 to do that, or press 3 to do both", \
    "press 1 to make up something, press 2 to make up something else, or press 3 to do something weird",
    "press 1 to speak spanish, press 2 to speak english"]

emin = 0

def scrape_menu(phone, S, T):
    base_url = "https://autotapp.firebaseio.com/menus/bot"

    _scrape_menu(phone, S, 0, base_url, "")

def _scrape_menu(phone, S, T, base_url, seq):
    # T.call(to=phone +  seq + ";pause=4500ms")
    # T.record(say="", \
    #     beep=False, \
    #     maxTime=10, \
    #     transcription= {"url": "http://autotapp.herokuapp.com/transcribe"}, \
    #     format='json'
    #     )

    # sleep(3000)

    # T.hangup()

    # split the menu options, push them to fb, or decides it's a leaf.
    # base case
    
    # recursive case
    # optionsCorpus = requests.get('https://autotapp.firebaseio.com/results.json').json()
    if T > 2: return
    optionsCorpus = emulated[T]
    optionList = filter(None, [option.strip(" , or and").split()[1:] \
        for option in optionsCorpus.lower().split("press")])

    path_url = base_url + '/'.join(seq.split("ppppppp")) + ".json"
    print path_url
    # requests.put(path_url, data=json.dumps(optionList))
    print len(optionList)
    for index, _ in enumerate(optionList):
        _scrape_menu(phone, S, T + 1, base_url, seq + "ppppppp" + str(index))

scrape_menu("4084827871", None, None)
