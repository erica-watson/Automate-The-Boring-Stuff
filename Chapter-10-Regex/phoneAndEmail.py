#! python3

import re, pyperclip

#TODO: create a regex object for phone numbers
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

#TODO: Create a regex object for email addresses
emailRegex = re.compile(r'''
#some.+_thing@something.com


[a-zA-Z_.+0-9]+    #email handle
@    #@ symbol
[a-zA-Z_.+0-9]+    #domain name


''', re.VERBOSE)



#TODO:Get the text off the clipboard
text = pyperclip.paste()

#TODO: Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhones = []
for phone in extractedPhone:
    allPhones.append(phone[0])

print(extractedEmail)
print(allPhones)

#TODO: Copy the extracted phone/email to the clipboard
results = '\n'.join(allPhones) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
