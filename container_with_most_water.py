arr = [2, 1, 8, 6, 4, 6, 5, 5]

def v1(arr):
    n = len(arr)
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            amount = min(arr[i], arr[j]) * (j - i)
            res = max(res, amount)

    return res

def v2(arr):
    left = 0
    right = len(arr) - 1
    res = 0
    while left < right:
        water = min(arr[left], arr[right]) * (right - left)
        res = max(res, water)
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1

    return res

print(v2(arr))