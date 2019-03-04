import os
from itertools import combinations


def string_combination(s):
    print(len(s))
    s_list = list(s)
    print(s_list)

    comb = combinations(s_list, 5)

# Print the obtained combinations
    for i in list(comb):
        print(i)


s = "abcdefghij"

string_combination(s)


