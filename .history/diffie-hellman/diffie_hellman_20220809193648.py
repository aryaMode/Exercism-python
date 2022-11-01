from random import random


def private_key(p):
    a = random(1 , p-1)

    return a


def public_key(p, g, private):
    A = (g**a)%p
    B = (g**b)%p

    return A, B, a, b


def secret(p, public, private):
    pass
