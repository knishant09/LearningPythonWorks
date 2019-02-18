def reduce(input1, input2):
    index = 1
    sum = 0
    l = []
    for i in input2:
        sum = sum + (i * index)
        if i < 0:
            l.append(index - 1)
        index += 1

    prevMax = sum
    print(l)
    print(prevMax)

    for i in l:
        sum = 0
        index = 1

        for j in range(input1):

            if i == j or j not in l:
                sum = sum + (input2[j] * index)
                index += 1

        if prevMax < sum:
            prevMax = sum

    return prevMax


print(reduce(3, [-1, 3, 4]))
print(reduce(5, [-1, -9, 0, 5, -7]))