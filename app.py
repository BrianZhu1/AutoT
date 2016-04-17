import requests
import os
import json
from time import sleep
from flask import *
from firebase_abstractions import *
from tropo_webapi_python import Tropo, Session, Choices
from message import *
app = Flask(__name__, static_url_path='')

T = S = None

@app.route("/", methods=["POST"])
def hello():
    # This main endpoint receives the invoking user action: text message.
    # Needs: # of company? are options from company already cached?
    
    # retrieves from cache / tells user to wait while it does / etc. ??
    # sends options to user / some dialogue... 
    
    # calls function to schedule outgoing calls
    # TODO: how cronjob?
    

    S = Session(request.data)
    T = Tropo()
    number = "+18016106014"

    # T.call(to=number)
    # T.say("Welcome to speed therapy!")
    # T.record(say="Tell us how you feel in fifteen minutes or less!", \
    #     beep=False, \
    #     maxTime=8, \
    #     transcription= {"url": "http://autotapp.herokuapp.com/transcribe"}, \
    #     format='json'
    #     )

    init = str(S.initialText)
    # initial = raw_input("").split()
    time = findIndex(["at"], init.split())
    place = findIndex(["call", "with"], init.split())

    say("Welcome to AuTo&T.")

    while not place:
        T.ask(Choices("[ANY]").obj, say="")
        place = T.ask(Choices("[ANY]").obj, say="Who do you want us to call?\n").value
    while not time:
        T.ask( Choices("[ANY]").obj, say="")
        time = T.ask(Choices("[ANY]").obj, say="At what time do you want us to set up the phone call?\n").value
        
    ask( Choices("[ANY]").obj, say="")
    if place in mappings:
        T.ask( Choices("[ANY]").obj, say="What were you looking to do with " + place + " at " + time + "?\n")
        T.on(event="continue", next=answerHandler)
    else:
        say("I've never encountered this company so you might expereince some extra setup time")
    
    # traverse_menu(number, S, T)

    return T.RenderJson()

def traverse_menu(phone, S, T): #it will find the next level of dtmf tones
        
    option_list = ["1","3", "2"] #actual values of dtmf tones
    quadruple_p = "ppppppppp" #four second delay between each dtmf tone

    call_str = ";postd="

    for i in range(3):
        if i != 0:
            call_str = call_str + quadruple_p
        call_str = call_str + option_list[i]

    call_str = call_str + ";pause=4000ms"

    if len(option_list) == 0:
        call_str = ""

    T.call(to=phone + call_str) #call_str = ;postd=1pppp2;pause=2000ms
    T.transfer(to="+14084827871")

    #pushes the data to the server
    # T.record(say="", \
    #     beep=False, \
    #     maxTime=10, \
    #     transcription= {"url": "http://autotapp.herokuapp.com/transcribe"}, \
    #     format='json'
    #     )

    # sleep(3000)

    # optionsCorpus = requests.get('https://autotapp.firebaseio.com/results.json').json()
    # optionList = filter(None, [option.strip(" , or and").split()[1:] \
    #     for option in optionsCorpus.lower().split("press")])



    #somehow find out whether the 

    #find the next level of dtmf tones somehow and append to option_list ()

    # TODO: some logic may be needed extra to authenticate.
def scrape_menu(phone, S, T):
    base_url = "https://autotapp.firebaseio.com/menus/bot"

    rscrape_menu(phone, S, T, base_url, "")

def rscrape_menu(phone, S, T, base_url, seq):
    call_string = phone + "" if not seq else ";postd=" + seq + ";pause=4500ms"
    print call_string
    T.call(to= "+" + call_string)  
    T.record(say="", \
        beep=False, \
        maxTime=10, \
        transcription= {"url": "http://autotapp.herokuapp.com/transcribe"}, \
        format='json'
        )

    sleep(3000)

    T.hangup()

    # split the menu options, push them to fb, or decides it's a leaf.
    # base case
    
    # recursive case
    optionsCorpus = requests.get('https://autotapp.firebaseio.com/results.json').json()
    optionList = filter(None, [option.strip(" , or and").split()[1:] \
        for option in optionsCorpus.lower().split("press")])

    path_url = base_url + '/'.join(seq.split("ppppppp")) + ".json"

    requests.put(path_url, data=json.dumps(optionList))

    for index, _ in enumerate(optionList):
        rscrape_menu(phone, S, T, base_url, seq + "ppppppp" + str(index))




@app.route("/transcribe", methods=["POST"])
def transcribe():
    headers = {'Content-Type': 'application/json'}
    print request.data
    requests.put('https://autotapp.firebaseio.com/results.json', data=json.dumps(request.json["result"]["transcription"]))
    return redirect('/')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
