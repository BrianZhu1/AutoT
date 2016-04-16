from itty import *
from tropo import Tropo

@get('/')
def index(request):

    t = Tropo()
    t.say("Welcome to Tropo!")
    return t.RenderJson()

run_itty(server='wsgiref', host='0.0.0.0', port=8888)