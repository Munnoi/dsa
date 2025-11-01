arr = [10, 3, 5, 6, 2]

def v1(arr):
    n = len(arr)
    res = [1] * n
    for i in range(n):
        for j in range(n):
            if i != j:
                res[i] *= arr[j]

    return res

def v2(arr):
    n = len(arr)
    res = [1] * n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= arr[i]
    suffix = 1
    for i in range(n-1, -1, -1):
        res[i] *= suffix
        suffix *= arr[i]

    return res

def v3(arr):
    zeros = arr.count(0)
    prod = 1
    n = len(arr)
    for num in arr:
        if num != 0:
            prod *= num
    res = [1] * n
    if zeros == 0:
        for i in range(n):
            res[i] = prod // arr[i]
    elif zeros == 1:
        zero_index = arr.index(0)
        res[zero_index] = prod
    
    return res
print(v3(arr))