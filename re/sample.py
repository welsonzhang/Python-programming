import re

m=re.match('foo','foo')
if m is not None:
   print m.group()

print re.match('foo','food on the table').group()

print re.search('food','seafood').group()

bt='bat|bet|bit'
print re.match(bt,'bat').group()

print re.match(bt,'he bit me!')

print re.search(bt,'he bit met!').group()

print re.findall('car','carry the car')

print re.sub('[ae]','X','abcdef')
print re.subn('[ae]','X','abcdef')

print re.split(':','str1:str2:str3')

f=open('whodata.txt','r')
for eachLine in f.readlines():
    print re.split('\s\s+|\t',eachLine)
f.close()


