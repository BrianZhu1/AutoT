import os
from flask import Flask
from tropo import *

app = Flask(__name__)

@app.route("/")
def hello():
	# callerID = currentCall.callerID

	say("Welcome to speed therapy!")
	record("Tell us how you feel in fifteen minutes or less!", {
	    "beep":False,
	    "maxTime":900,
	    "transcriptionOutURI": "http://autotapp.herokuapp.com/transcribed_audio",
	    "transcriptionOutFormat": 'json'
	    }
	)

	return 'Hello World!'

@app.route("/transcribed_audio", methods=["POST"])
def transcribed_audio():
	return request.json

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
