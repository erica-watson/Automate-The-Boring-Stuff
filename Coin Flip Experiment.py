#Coin Flip Experiment

import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    #Create list of 100 'heads' or 'tails' values
    flips = []
    for i in range(100):
        flips.append(random.randint(0, 1))

    #Check if there is a streak of 6 heads or tails in a row
    currentStreak = 0
    for x in range(len(flips)):
        if flips[x-1] == flips[x]: #two adjacent flips are identical
            currentStreak +=1
            if currentStreak == 5: #5 comparisons represents 6 total values
                numberOfStreaks += 1
                break
        else: #reset the counter
            currentStreak = 0

#print the probability
print('In 10,000 experients, there is a ' + str(numberOfStreaks/100) + '% chance of a streak of six.')
