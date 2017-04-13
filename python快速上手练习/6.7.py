def printTable(data):
    lenth = {}
    hang = len(data)
    number = 0
    for x in data:
        lie = len(x)
        for i in range(lie):
            lenth.setdefault(number,0)
            if len(x[i])>lenth[number]:
                lenth[number]=len(x[i])
        number=number+1

    print(lenth)

    for y in range(lie):
        for num in range(hang):
            print(data[num][y].rjust(lenth[num])+' ',end='')
        print()


tableData=[['apples','oranges','cherries','banana'],
           ['Alice','Bob','Carol','David'],
           ['dogs','cats','moose','goose']]
printTable(tableData)