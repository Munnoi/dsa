A = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]

def v1(A):
    zeros = A.count(0)
    k = 0
    while zeros:
        A[k] = 0
        zeros -= 1
        k += 1
    for k in range(k, len(A)):
        A[k] = 1

    return A

def v2(A):
    j = 0
    for i in range(len(A)):
        if A[i] == 0:
            A[i], A[j] = A[j], A[i]
            j += 1
    
    return A
    
print(v2(A))