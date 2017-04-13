import re
def StrongKey(key):
    keyre1=re.compile(r'.{8}.*')
    keyre2=re.compile(r'[a-zA-Z]')
    keyre3=re.compile(r'(\d)+')
    if keyre1.search(key)!=None and keyre2.search(key)!=None and keyre3.search(key)!=None:
        print('True')
    else:
        print('False')

value=input('print your key:')
StrongKey(value)