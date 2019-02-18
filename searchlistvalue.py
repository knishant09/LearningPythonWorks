import math
import os
import random
import re
import sys


# Complete the findNumber function below.
def findNumber(arr, k):
    print(arr)
    print(type(arr))

    if k in arr:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':

    arr_count = int(input().strip())
    print(arr_count)

    arr = []


    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())


    findNumber(arr, k)