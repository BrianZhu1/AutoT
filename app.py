import os
from flask import Flask
app = Flask(__name__)

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
