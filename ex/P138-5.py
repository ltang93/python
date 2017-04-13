list={}
while 1==1:
    choose=input("Add or look up a word (a/l)?")
    if choose=="a":
        word=input("Type the word:")
        definition=input("Type the definition:")
        list[word]=definition
        print("Word added!")
    elif choose=="l":
        word=input("Type the word:")
        if word in list:
            print(list[word])
        else:
            print("That word isn't in the dictionary yet")
