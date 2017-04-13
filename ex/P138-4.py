print("Enter 5 names:")
list=[]
for i in range(5):
    list.append(input())
print("The names are ",end="")
for name in list:
    print(name,end=" ")
print("")
sortlist=sorted(list)
print("The sorted names are ",end="")
for name in sortlist:
    print(name,end=" ")
print("")
print("The third name you entered is:",list[2])
print("")
num=int(input("Replace one name. Which one?(1-5):"))
name=input("New name:")
list[num-1]=name
for name in list:
    print(name,end=" ")
print("")
