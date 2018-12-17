# coding=utf-8

import re

str1 = "eello world"
print "match", re.match(r'e', str1).group(0)  # group(0)返回整个匹配的整个字符
print "serach", re.search(r'e', str1).group(0)
print "findall", re.findall(r'e', str1)
