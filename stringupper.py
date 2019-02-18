import sys


def stringUpper(name):
    print(name)
    print(len(name))
    l1 = list(name)
    print(l1)
    l2 = []
    for i in range(len(l1)):
        if i == 0 or i == 3:
            l2.append(l1[i].upper())
        else:
            l2.append(l1[i])
    print(l2)
    str1 = ''.join(l2)
    print(str1)



name = "hello"
stringUpper(name)