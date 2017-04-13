def fenge(li):
    for i in range(len(li)):
        if i==len(li)-1:
            print('and '+li[i])
        else:
            print(li[i] + ',', end='')

fenge(['apples','bananas','tofu','cats'])