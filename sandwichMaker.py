#! python 3

#asks users for their sandwich preferences and returns the total price

import pyinputplus as pyip

breadChoices = {'white':1, 'wheat':1.5, 'sourdough':2}
proteinChoices = {'chicken':5, 'turkey':4, 'ham':4, 'tofu':3}
cheeseChoices = {'cheddar':1, 'Swiss':2, 'mozzarella':1}
condimentChoices = {'mayo' : .50, 'mustard':.50, 'lettuce':0, 'tomato':0}

sandwich = {} #will store ingredients and prices

#request and store ingredient preferences
bread = pyip.inputMenu(list(breadChoices.keys()))
sandwich[bread] = breadChoices[bread]
protein = pyip.inputMenu(list(proteinChoices.keys()))
sandwich[protein] = proteinChoices[protein]
if pyip.inputYesNo('Would you like to add cheese?\n') == 'yes':
    cheese = pyip.inputMenu(list(cheeseChoices.keys()))
    sandwich[cheese] = cheeseChoices[cheese]
for i in condimentChoices:
    if pyip.inputYesNo(f'Would you like {i}?\n'):
        sandwich[i] = condimentChoices[i]

#return the total cost of the sandwich
price = 0
for j in sandwich:
    price += sandwich[j]

print(f'The total price for your sandwich is ${price:.2f}. Thank you for your order.')
