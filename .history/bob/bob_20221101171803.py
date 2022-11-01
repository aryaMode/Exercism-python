def response(hey_bob):
    if hey_bob.isupper():
        return 'Whoa, chill out!'
    elif hey_bob[-1] == "?":
        return 'Sure.'
    elif hey_bob.isupper() and (hey_bob[-1]=="?"):
        return 'Calm down, I know what I\'m doing!'
    
    else:
        return 'Whatever.'
