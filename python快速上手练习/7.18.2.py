import re
def mystrip(words,de=''):
    print(words)
    if de=='':
        print('1')
        wordsre=re.compile(r'^\s*|\s*$')
        print('your string is:'+wordsre.sub(r'', words))
    else:
        print('2')
        wordsre=re.compile(r'^'+de+r'|'+de+r'$')
        print('your string is:'+wordsre.sub(r'',words))

words=input('input your string:')
de=input('input your delete string:')
mystrip(words,de)