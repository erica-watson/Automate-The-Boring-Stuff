#! python3

'''
Randomly generates 10 multiplication questions, ranging from 0 × 0 to 9 × 9.
User gets three tries and a maximum of 8 seconds to guess correctly.
'''

import pyinputplus as pyip
import random, time

score = 0
numOfQuestions = 10

#generate ten random questions, using regexes to validate answer
for i in range(numOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    try:
        response = pyip.inputStr(f'{i}. {num1} x {num2} = \n', timeout = 8, limit = 3, allowRegexes = [f'^{num1*num2}$'], blockRegexes = ['.*'])
    except pyip.RetryLimitException:
        print('Incorrect. Took more than three attempts.')
    except pyip.TimeoutException:
        print('Incorrect. Took too long to guess.')
    else:
        print('Correct!')
        score += 1
    time.sleep(1)

print(f'You scored {score} points out of a possible {numOfQuestions} points.')
