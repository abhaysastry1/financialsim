import random


def inflationator(port):
    inf = random.randint(10, 99) / 10000
    port -= (inf * port)
    return port

