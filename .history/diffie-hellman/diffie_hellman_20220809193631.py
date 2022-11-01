from random import random


def private_key(p):
    a = random(1 , p-1)

    return a, b


def public_key(p, g, private):
    a, b = private_key(p)
    A = (g**a)%p
    B = (g**b)%p

    return A, B, a, b


def secret(p, public, private):
    pass
