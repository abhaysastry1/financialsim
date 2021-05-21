from simplePortfolio import portfolio

start = input("When does retirement start?")
end = input("When does retirement end?")
assets = input("How much fricking money do you have?")
income = input ("How much do u make per year?")
spending = input("How much do you spend?")

print(portfolio(int(assets), int(spending), int(start), int(end), int(income)))