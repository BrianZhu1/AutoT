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
    say(seq)

def answerHandler(ans):
    company = mappings[place]
    path, result = findMatch(0, company, ans)[1]
    say(result)
    choice = ask("found \"" + result + "\", is that useful? Type customer service or choices, if not.\n", {
        "choices":"yes, customer service, choices"})
    if choice.value == "yes":
        inputSequence(result)
    elif choice.value == "customer service":
        inputSequence(company["customer service"])
    else:
        say("Here are your choices:")
def findIndex(words, phrase):
    match = ""
    for word in words:
        if word in phrase:
            match = (phrase.index(word), word)
    return phrase[match[0] + 1] if match else match

init = str(currentCall.initialText)
# initial = raw_input("").split()
time = findIndex(["at"], init.split())
place = findIndex(["call", "with"], init.split())

say("Welcome to AuTo&T.")

while not place:
    ask("", {"choices":"[ANY]"})
    place = ask("Who do you want us to call?\n", {"choices":"[ANY]"}).value
while not time:
    ask("", {"choices":"[ANY]"})
    time = ask("At what time do you want us to set up the phone call?\n", {"choices":"[ANY]"}).value
    
ask("", {"choices":"[ANY]"})
if place in mappings:
    ask("What were you looking to do with " + place + " at " + time + "?\n", {
        "choices":"[ANY]",
        "onChoice": answerHandler
    })
else:
    say("I've never encountered this company so you might expereince some extra setup time")