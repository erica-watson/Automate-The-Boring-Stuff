'''
A strong password contains:
    -at least 8 characters
    -both upper and lower
    -at least one digit
'''
import re
import pyperclip

def passChecker(password):
    pwLenRegex = re.compile(r'.{8,}', re.DOTALL)
    pwUpperRegex = re.compile(r'[A-Z]+')
    pwLowerRegex = re.compile(r'[a-z]+')
    pwDigitRegex = re.compile(r'\d+')

    if not pwLenRegex.findall(password):
        return False
    elif not pwUpperRegex.findall(password):
        return False
    elif not pwLowerRegex.findall(password):
        return False
    elif not pwDigitRegex.findall(password):
        return False
    else:
        return True

print('Enter the password:')
pw = input()
print(passChecker(pw))
