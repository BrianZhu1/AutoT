import requests
import os
import json
from flask import *
from tropo_webapi_python import Tropo, Session
app = Flask(__name__, static_url_path='')

# app.run(debug=True)

junk = """
@app.route("/")
def hello():
    var callerID = currentCall.callerID;

    say("Welcome to speed therapy!");
    record("Tell us how you feel in fifteen minutes or less!", {
        beep:false,
        maxTime:900,
        transcriptionOutURI: "http://autotapp.herokuapp.com/transcribed_audio",
        transcriptionOutFormat: 'json'
        }   
    );

@app.route("/transcribed_audio")
def transcribed_audio:
    return request.json

"""

@app.route("/", methods=["POST"])
def hello():
    s = Session(request.data)
    t = Tropo()
    t.call(to="14084827871")
    t.say("Welcome to speed therapy!")
    t.record(say="Tell us how you feel in fifteen minutes or less!", \
        beep=False, \
        maxTime=8, \
        transcription= {"url": "http://autotapp.herokuapp.com/transcribe"}, \
        format='json'
        )
    return t.RenderJson()


# THE FOLLOWING RESIDES IN ITS OWN APPLICATION.
@app.route("/transcribe", methods=["POST"])
def transcribe():
    headers = {'Content-Type': 'application/json'}
    requests.put('https://autotapp.firebaseio.com/results.json', data=json.dumps(request.data))
    return redirect('/')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
