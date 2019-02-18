

def solution(A):
    ans = -1000
    for i in range(1, len(A)):
        if A[i] < ans:
            ans = A[i]
    return ans

A = range(-1000,1000)
print(solution(A))