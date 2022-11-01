def steps(number):
    
    counter = 0
    
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
        return

    while not number == 1:
        
        counter+=1

        if number%2 == 0:
            number = number/2
        
        else:
            number = (3*number)+1
    
    return counter

