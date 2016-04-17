import requests
import os
from flask import Flask, request
from firebase import firebase as fb
# from tropo_webapi_python import Tropo as t
app = Flask(__name__)

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

@app.route("/")
def hello():
    my_token = "436c63746752724667426b4f4476635275426c614763666a5774724776504e4f6c4a41514c56544246527248"
    my_num_to_dial = "16086952116"
    my_name = "Brian+Zhu"
    my_message = "the+sky+is+falling"
    base_string = "https://api.tropo.com/1.0/sessions?action=create&"
    http_string = base_string + "token=" + my_token + "&numberToDial=" + my_num_to_dial + "&customerName=" + my_name + "&msg=" + my_message
    return "Hello from Python!"


# THE FOLLOWING RESIDES IN ITS OWN APPLICATION.
@app.route("/transcribe", methods=["POST"])
def transcribe():
    #fb = fb.FirebaseApplication("https://autotapp.firebaseio.com", None)
    #posted = fb.post('/transcriptions', request.get_json(), {'print': 'pretty'}, {'Content-Type': 'application/json'})
    return render_template('testout.html', jsoncode = request.get_json())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
