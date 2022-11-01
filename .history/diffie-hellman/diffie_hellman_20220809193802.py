from random import random


def private_key(p):
    a = random(1 , p-1)

    return a


def public_key(p, g, private):
    A = (g**private)%p

    return A


def secret(p, public, private):
    s = (public**private)%p

    
