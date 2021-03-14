#detect dates in the DD/MM/YYYY format
    #days: 01-31
    #mon: 01-12
    #year: 1000-2999
import re

text = 'this is a sample 01/01/1990, 29/37/2008, 29/02/2001, 31/04/2008'

#create regex for the dates
dateRegex = re.compile(r'''(
([0-2]\d|30|31)    #DD
/    #/
(0\d|10|11|12)    #MM
/    #/
([1-2]\d{3})    #YYYY
    )''', re.VERBOSE)

#store the dates into strings named month, day, and year
dates = dateRegex.findall(text)
print('Dates found: ' + str(dates))
shortMonths = ('04', '06', '09', '11')

for item in dates:
    day, mon, year = item[1], item[2], item[3]
    #detect if invalid date
    if mon in shortMonths and day == '31':
        print(str(item[0]) + ' is not a valid date.')
    elif day == '29' and mon == '02':
        if int(year)%4 != 0:
            print(str(item[0]) + ' is not a valid date.')
    elif day == '30' and mon == '02':
        print(str(item[0]) + ' is not a valid date.')
    else:
        print(str(item[0] + ' is a valid date.'))
