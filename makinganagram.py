import os, math


def makeAnagram(a, b):

    x = len([i for i in a if i not in b])
    y = len([i for i in b if i not in a])
    print(x, y)
    sum = x + y
    #print(sum)


    print(len(b))

    set_a = set(a)
    print(set_a)

    b_list = list(b)
    print(b_list)

    set_b = set(b_list)
    print(b)
    print(set_b)
    print(len(set_b))

    difference = set_a ^ set_b

    diff = set_b - set_a

    print(diff)

    print(len(difference))


    count = 0
    for i in range(97, 123):
        ia = a.count(chr(i))
        ib = b.count(chr(i))
        count += abs(ia - ib)
    print(count)













    pass




a = "fcrxzwscanmligyxyvym"
b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"

makeAnagram(a, b)