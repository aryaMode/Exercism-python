def steps(number):
    
    if number == 0 or number < 0:
        raise ValueError("Number must be positive")
    
    if number % 2 == 0:
        
