import random
import array as arr
from portfolio.inflation import inflationator

yearlyPort = []
years = []


def portfolio(port, exp, start, end, income):
    for x in range(start, end):
        port -= exp
        print("Port is (  exp change  ): " + str(round(port, 2)) + " in " + str(x))

        port += income
        print("Port is (income change): " + str(round(port, 2)) + " in " + str(x))

        port -= random.uniform(0.0, (0.33) * exp)
        print("Port is (random change): " + str(round(port, 2)) + " in " + str(x) + "\n")

        inflationator(port)

        yearlyPort.append(port)
        years.append(x)

    return yearlyPort, years
    # if port < 0:
    # return 'Not enough cash to retire'
    # else:
    # return 'You have ' + str(port) + ' remaining after death'


# Some num in between 0-1/3 exp
# Some port -= num


def getYearlyPortfolio():
    return yearlyPort


def getYears():
    return years
