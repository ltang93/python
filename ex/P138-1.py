print("Enter 5 names:")
list=[]
for i in range(5):
    list.append(input())
print("The names are ",end="")
for name in list:
    print(name,end=" ")
