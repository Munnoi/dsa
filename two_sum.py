arr = [0, -1, 2, -3, 1]
target = -2

def v1(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return True

    return False

def v2(arr, target):
    arr.sort()
    def binarySearch(left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    for i in range(len(arr)):
        complement = target - arr[i]
        if binarySearch(i+1, len(arr)-1, complement):
            return True
        
    return False

def v3(arr, target):
    s = set()
    for num in arr:
        complement = target - num
        if complement in s:
            return True
        s.add(num)

    return False

print(v3(arr, target))