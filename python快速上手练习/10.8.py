#调试已有程序
import random,logging
logging.disable(logging.CRITICAL)
guess=''
while guess not in ('0','1'):
    print('Guess the coin toss!Enter heads or tails:')
    guess=input()
toss=random.randint(0,1) #0 is tails,1 is heads

logging.basicConfig(level=logging.DEBUG,format='%(message)s')
logging.debug('toss is:'+str(toss)+' guess is:'+str(guess))

if str(toss)==str(guess):
    print('You got it!')
else:
    print('Nope!Guess again!')
    guess=input()
    logging.debug('toss is:'+str(toss))
    if str(toss)==str(guess):
        print('You got it!')
    else:
        print('Nope.You are really bad at this game.')