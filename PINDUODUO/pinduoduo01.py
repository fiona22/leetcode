#import sys
#cards = sys.stdin.readline().strip()
#listcard = list(cards)
#newcard = sorted(listcard, key=str.lower)

# print newcard


import sys
cards = sys.stdin.readline().strip()

newcards = ""
for i in cards:
    if i>='A' and i<='Z':
        newcards += chr(ord(i)+ord('a')-ord('A'))
    else:
        newcards += i
res = list(newcards)
res.sort()
tmp = []
for i in res:
    if i not in tmp:
        tmp.append(i)

print tmp[0]

