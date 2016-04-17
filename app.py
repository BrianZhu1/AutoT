import requests
import os
import json
from flask import *
from firebase_abstractions import *
from tropo_webapi_python import Tropo, Session
app = Flask(__name__, static_url_path='')

S = T = None

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
    T.call(to="14084827871")
    T.say("Welcome to speed therapy!")
    T.record(say="Tell us how you feel in fifteen minutes or less!", \
        beep=False, \
        maxTime=8, \
        transcription= {"url": "http://autotapp.herokuapp.com/transcribe"}, \
        format='json'
        )
    return t.RenderJson()

def scrape_menu(phone, s, t):
    T.call(to=phone)
    # TODO: some logic may be needed extra to authenticate.
    # 

@app.route("/transcribe", methods=["POST"])
def transcribe():
    headers = {'Content-Type': 'application/json'}
    requests.put('https://autotapp.firebaseio.com/results.json', data=json.dumps(request.data))
    return redirect('/')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
