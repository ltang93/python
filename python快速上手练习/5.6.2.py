def addTolnventory(inventory,addedItems):
    for thing in addedItems:
        inventory.setdefault(thing,0)
        inventory[thing]=inventory[thing]+1
    return inventory

def displayInventory(diction):
    count=0
    print('Inventory:')
    for m in diction:
        print(str(diction[m])+' '+str(m))
        count=count+diction[m]
    print('Total number of items:'+str(count))

inv={'gold coin':42,'rope':1}
dragonLoot=['gold coin','dagger','gold coin','gold coin','ruby']
inv=addTolnventory(inv,dragonLoot)
displayInventory(inv)