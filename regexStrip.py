'''
Write a function that does the same thing as the strip() method.
-if one argument is passed:
    -remove whitespace characters from the beginning and end of the string
-if two arguments are passed:
    -the characters in the second argument will be removed from the string
'''
import re

def strip(string, remove = ''):
    #remove whitespace from beginning and end
    if remove == '':
        spaceRegex = re.compile(r'^(\s*)(.*?)(\s*)$', re.DOTALL)
        stripped = spaceRegex.search(string)
        return stripped.group(2)
    else:
        charRegex = re.compile('^([{s}]*)(.*?)([{s}]*)$'.format(s = remove), re.DOTALL)
        stripped = charRegex.search(string)
        return stripped.group(2)



test = '   _ i\'ve got a_lovely bunch of coconuts!'
print(test)
print(strip(test, '!stun'))


