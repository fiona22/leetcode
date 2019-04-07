# coding=utf-8

def extend_list(val, list=[]):
    list.append(val)
    return list


list1 = extend_list(10)
list2 = extend_list(123, [])
list3 = extend_list('a')

print list1  # list1 = [10, 'a']
print list2  # list2 = [123]
print list3  # list3 = [10, 'a']

X = "1,2,3"
Y = X.split(',')
print Y

