from portfolio.simplePortfolio import portfolio


def askVals():
    start = input("When does retirement start?")
    end = input("When does retirement end?")
    assets = input("How much money do you have?")
    spending = input("How much do you spend?")
    income = input("How much money do you earn")
    portfolio(int(assets), int(spending), int(start), int(end), int(income))

