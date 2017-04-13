def normalize(name):
    name=name.lower()
    return name[0].upper()+name[1:]

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)