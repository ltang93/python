'''
The ADJECTIVE panda walked to the NOUN and then VERB.A nearby NOUN was unaffected by these events.
'''
import re
def MadLibs(newList):
    txt=open('D://1.txt','r')
    text = txt.read()
    adjectivere=re.compile(r'ADJECTIVE')
    text=adjectivere.sub(newList[0],text)
    nounre = re.compile(r'NOUN')
    text=nounre.sub(newList[1], text)
    verbre = re.compile(r'VERB')
    text =verbre.sub(newList[2], text)

    redelete=re.compile(r'^.*?'+newList[1])
    textdelete =redelete.search(text)
    textdeletestr=textdelete.group() #leftstring
    text=re.compile(textdeletestr).sub('',text) #rightstring

    nounre1 = re.compile(newList[1])
    text =nounre1.sub(newList[3], text)
    txtnew=open('D://2.txt','w')
    txtnew.write(textdeletestr+text)
    txt.close()
    txtnew.close()
L=[]
L.append(input('Enter an adjective:'+'\n'))
L.append(input('Enter an noun:'+'\n'))
L.append(input('Enter an verb:'+'\n'))
L.append(input('Enter an noun:'+'\n'))
MadLibs(L)


