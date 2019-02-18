l1 = [1, 2, 4, 6, 10]
l2 = [4, 5, 6, 9, 12]

l1.extend(l2)

print(l1)

l1_sort = sorted(l1)
print(l1_sort)

middle_ele = int(len(l1) / 2)
print(middle_ele)

print("*********")
print(l1_sort[middle_ele - 1])

sum = l1_sort[middle_ele - 1] + l1_sort[middle_ele]

print(sum)

