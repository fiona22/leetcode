# encoding=utf-8
from collections import defaultdict
'''
dict = defaultdict(int)
for str in raw_input():
    if(str.isalpha()):
        dict[str] += 1
        if dict[str] == 3:
            print str
            breaks

'''
frequencies = defaultdict(int)
wordlist = [1,2,3,4,1,2,3,4,1,12]
for word in wordlist:
    frequencies[word]+=1
    print word, frequencies[word]