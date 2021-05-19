# Test Variables
pCash = 100000
spend = 100
retStart = 2021
retEnd = 3350


# Function for calculation
def portfolio(port, exp, start, end):
    for x in range(start, end):
        port -= exp
    return port


# Test entries
if portfolio(pCash, spend, retStart, retEnd) < 0:
    print('Not enough cash to retire')
else:
    print('You have ' + str(portfolio(pCash, spend, retStart, retEnd)) + ' remaining after death.')
