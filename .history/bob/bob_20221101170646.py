def response(hey_bob):
    if hey_bob.isUpper():
        return 'Whoa, chill out!'
    elif hey_bob == "How are you?":
        return 'Sure.'
    elif hey_bob.isUpper() and ("?" in hey_bob):
        return 'Calm down, I know what I\'m doing!'
    elif hey_bob == "" or hey_bob == " ":
        return 
