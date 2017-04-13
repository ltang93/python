def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2
    elif number%2==1:
        print(3*number+1)
        return 3*number+1

while(True):
    number=input('输入一个整数:')
    try:int(number)
    except ValueError:
        print('输入了一个非整数')
    else:
        end=collatz(int(number))
    if(end==1):
        break