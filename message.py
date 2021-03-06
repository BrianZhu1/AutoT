mappings = {
    "att": {
        "customer service": ("123", "customer service"),
        "bill": {
            "pay": ("12", "pay bill"),
            "status": ("12", "get status")
        }
    }, "americanairlines": {
        "customer service": ("123", "customer service"),
        "flight": {
            "book": ("12", "book flight"),
            "status": ("3", "flight status"),
            "cancel": ("4", "cancel flight")
        }
    }
}

# class dotdict(dict):
#     """dot.notation access to dictionary attributes"""
#     def __getattr__(self, attr):
#         return self.get(attr)
#     __setattr__= dict.__setitem__
#     __delattr__= dict.__delitem__

# def say(string):
#     print string;

# def ask(string, rest):
#     if string != "":
#         val = raw_input(string)
#         if "onChoice" in rest:
#             rest["onChoice"](val)
#         return dotdict({"value": val})

def findMatch(cnt, dct, strng):
    if not isinstance(dct, dict): return (cnt, dct)
    return max(map(lambda (key, val): findMatch(cnt + 1, val, strng) if key in strng else (0, None), dct.iteritems()), key = lambda v: v[0])

def inputSequence(seq):
    T.say(seq)

def answerHandler(ans):
    company = mappings[place]
    path, result = findMatch(0, company, ans)[1]
    T.say(result)
    choice = T.ask(Choices("['yes', 'customer service', 'choices']").obj, say="found \"" + result + "\", is that useful? Type customer service or choices, if not.\n")
    if choice.value == "yes":
        inputSequence(result)
    elif choice.value == "customer service":
        inputSequence(company["customer service"])
    else:
        T.say("Here are your choices:")
def findIndex(words, phrase):
    match = ""
    for word in words:
        if word in phrase:
            match = (phrase.index(word), word)
    return phrase[match[0] + 1] if match else match

def sleep_till_future(f_minute):
    t = datetime.datetime.today()
    future = datetime.datetime(t.year,t.month,t.day,t.hour,f_minute)

    if future.minute <= t.minute:
        print("ERROR! Enter a valid minute in the future.")
    else:
        print "Current time: " + str(t.hour)+":"+str(t.minute)
        print "Sleep until : " + str(future.hour)+":"+str(future.minute)

        seconds_till_future = (future-t).seconds
        time.sleep( seconds_till_future )
        print "I slept for "+str(seconds_till_future)+" seconds!"

# init = str(S.initialText)
# # initial = raw_input("").split()
# time = findIndex(["at"], init.split())
# place = findIndex(["call", "with"], init.split())

# say("Welcome to AuTo&T.")

# while not place:
#     T.ask(Choices("[ANY]"), say="")
#     place = T.ask( Choices("[ANY]"), say="Who do you want us to call?\n").value
# while not time:
#     T.ask(Choices("[ANY]"), say="")
#     time = T.ask( Choices("[ANY]"), say="At what time do you want us to set up the phone call?\n").value
    
# ask(Choices("[ANY]"), say="")
# if place in mappings:
#     T.ask( Choices("[ANY]"), say="What were you looking to do with " + place + " at " + time + "?\n")
#     T.on(event="continue", next=answerHandler)
# else:
#     say("I've never encountered this company so you might expereince some extra setup time")