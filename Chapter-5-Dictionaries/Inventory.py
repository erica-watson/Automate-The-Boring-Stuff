stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total = item_total + int(v)
    print("Total number of items: " + str(item_total))

#displayInventory(stuff)


'''
write a function named addToInventory(inventory, addedItems)
    inventory is a dictionary
    added items is a list
    add to inventory updates the dictionary
'''


def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i] = inventory[i] + 1
        else:
            inventory[i] = 1
    return inventory

dragonLoot = ['gold coin', 'gold coin', 'dagger', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
