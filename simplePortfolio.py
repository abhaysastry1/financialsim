import random

# Test Variables
pCash = 100000
spend = 100
retStart = 2021
retEnd = 3350
income = 410000

# Function for calculation
def portfolio(port, exp, start, end, income):
    for x in range(start, end):
        port -= exp
        print("Port is (  exp change  ): " + str(round(port, 2)) + " in " + str(x))

        port += income
        print ("Port is (income change): " + str(round(port, 2)) + " in " + str(x))

        port -= random.uniform(0.0, (0.33) * exp)
        print ("Port is (random change): " + str(round(port, 2)) + " in " + str(x) + "\n")

    if port < 0:
        return 'Not enough cash to retire'
    else:
        return 'You have ' + str(port) + ' remaining after death'

#Some num in between 0-1/3 exp 
#Some port -= num