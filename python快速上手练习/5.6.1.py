def displayInventory(diction):
    count=0
    print('Inventory:')
    for m in diction:
        print(str(diction[m])+' '+str(m))
        count=count+diction[m]
    print('Total number of items:'+str(count))

things={'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
displayInventory(things)