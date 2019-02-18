



def solution(A):

    smallest = 1
    A = list(dict.fromkeys(A))


    #for i in range(len(A)):
    while (smallest in A):


       smallest += 1
    return smallest






A = [-1, -3]
smallest=solution(A)
print(smallest)
