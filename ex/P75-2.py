sex=input("Sex?")
while sex!="f" and sex!="m":
    sex=input("Please enter sex..f or m?")
if sex=="m":
    print("No")
elif sex=="f":
    age=input("Age?")
    if 10<=int(age)<=12:
        print("Yes")
    else:
        print("No")
