def equilateral(sides):
    a, b, c = sides
    con1 = a + b >= c
    con2 = b + c >= a
    con3 = a + c >= b

    if not(con1 and con2 and con3):
        return False

    for side in sides:
        if not side  > 0:
            return False
            
    if a == b == c:
        return True

    return False

def isosceles(sides):
    a, b, c = sides
    con1 = a + b >= c
    con2 = b + c >= a
    con3 = a + c >= b

    if not(con1 and con2 and con3):
        return False

    for side in sides:
        if not side > 0:
            return False
    
    if a == b or b == c or a == c:
        return True

    return False


def scalene(sides):
    a, b, c = sides
    con1 = a + b >= c
    con2 = b + c >= a
    con3 = a + c >= b
    
    if not(con1 and con2 and con3):
        return False
        
    return True if not(a == b or b == c or a == c) else False

    return False
