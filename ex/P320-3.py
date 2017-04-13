import pickle
name=input("what's your name?")
age=input("your age?")
color=input("which color?")
food=input("food?")
list=[]
list.extend([name,age,color,food])
txt=open('P310-2.pickle','wb')
pickle.dump(str(list),txt)
txt.close()

