def total(five,two,one):
    sum=int(five)*5+int(two)*2+int(one)
    return sum/100
five=input("多少个5分钱？")
two=input("多少个2分钱？")
one=input("多少个1分钱？")
print(total(five,two,one),"元")
