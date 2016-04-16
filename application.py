from itty import *

@get('/')
def simple_post(request):
    return open('testout.html', 'r').read()

run_itty()