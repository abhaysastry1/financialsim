# Test Variables
pCash = 100000
spend = 100
retStart = 2021
retEnd = 3350


# Function for calculation
def portfolio(port, exp, start, end):
    for x in range(start, end):
        port -= exp
    if port < 0:
        return 'Not enough cash to retire'
    else:
        return 'You have ' + str(port) + ' remaining after death'