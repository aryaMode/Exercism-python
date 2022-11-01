def square(number):
    if not(number >=1 and number <=64):
        raise ValueError("square must be between 1 and 64")

    grains_in_tile = 1 * (2**(number-1))
    return grains_in_tile


def total():
    a = 1
    r = 2
    n = 64
    total = int(a * (((r**n)-1)/(r-1))) -1
    return total