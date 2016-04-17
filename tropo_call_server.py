result_one = ask("Press one for English or press two for Spanish", { "choices":"1, 2","attempts":3,"mode":"dtmf"})
if (result_one.value == "1"):
    say("You have chosen English")
    result_two = ask("Press one if you want to check the balance of your account or press two if you would like to help yourself or press three for other options", { "choices":"1, 2, 3","attempts":3,"mode":"dtmf"})
    if(result_two.value == "1"):
        say("You currently have one hundred and five dollars in your account. Have a nice day!")
    elif(result_two.value == "2"):
        say("If you want to help yourself, please go to Google dot com and look up the answer.")
    elif(result_two.value == "3"):
        say("You have chosen other options")
        result_three = ask("Press one if you want to check the status of the companys servers or press two if you would like to speak with a customer support representitive or press three if you would like to exit", { "choices":"1, 2, 3","attempts":3,"mode":"dtmf"})
        if(result_three.value == "1"):
            say("The company's servers are up and fully operational")
        elif(result_three.value == "2"):
            say("Please wait while we transfer you to a customer support representitive")
            transfer("+16086952116")
        elif(result_three.value == "3"):
            say("Have a nice day!")
elif (result_one.value == "2"):
    say("You have chosen Spanish. Unfortunately, we don't have Spanish options for the hotline. Sorry!")