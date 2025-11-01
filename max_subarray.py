arr = [2, 3, -8, 7, -1, 2, 3]

def v1(arr):
    res = arr[0]
    n = len(arr)
    for i in range(n):
        currSum = 0
        for j in range(i, n):
            currSum += arr[j]
            res = max(res, currSum)

    return res

def v2(arr):
    res = arr[0]
    maxEnding = arr[0]
    for i in range(1, len(arr)):
        maxEnding = max(maxEnding+arr[i], arr[i])
        res = max(res, maxEnding)

    return res

print(v2(arr))