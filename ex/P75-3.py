size=input("Size of tank:")
full=input("Percent full:")
per=input("Km per liter:")
km=float(size)*float(full)/100*float(per)
print("You can go another",km,"km")
print("The next gas station is 200km away")
if km <200:
    print("Get gas now!")
else:
    print("You can wait for the next station")
