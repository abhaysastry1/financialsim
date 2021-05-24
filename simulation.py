pcash = 100000
spend = 1000
retStart = 2021
retEnd = 2058
count = 0
simulation = 'fail'
simulationList = []

for x in range(retStart,retEnd):
    #money = pcash - spend
    #pcash = money
    pcash -= spend
    count += 1
    if pcash <= 0:
        break
    print ('After '+ str(count) + ' cycles, there is '+ str(pcash) + ' remaining.')



if pcash > 0:
    print ('Simulation PASSED. '+ str(pcash) + ' remaining after '+ str(count) + ' simulations.')
    simulation = 'pass'
else:
    print('Simulation FAILED. After ' + str(count) + ' simulations. There was not enough money to retire.')


simulationList = [simulationList, simulation]



