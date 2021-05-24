import random

portfolio = 100000
retLength = 40
inflation = random.randint(10, 99) / 100


def inflationator(port, inf, retDur):
    for x in range(retDur):
        port -= (inf * port)
        return port

