#take a list as an argument and return a string with the items separated with a comma and space. add "and" before the last item

def listify(list):
    output = ''
    if len(list) > 0:
        for x in range(len(list)-1):
            x = str(list[x]) + ', '
            output = output + x
        output = output + 'and ' + list[-1]
        return output
    else: #list is empty
        return 'No list provided.'


fruits = ['apples', 'bananas', 'oranges']
another_list = [3.14, 'pennies', 'tangerines']
list_of_lists = ['hello', 'i', 'am', 'a', ['list', 'of', 'lists'], '!']
veg = []

print(listify(another_list))
print(listify(fruits))
print(listify(veg))
print(listify(list_of_lists))

