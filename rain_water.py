arr = [3, 0, 1, 0, 4, 0, 2]

def v1(arr):
  res = 0
  for i in range(1, len(arr)-1):
    left = arr[i]
    for j in range(i):
      left = max(left, arr[j])
    right = arr[i]
    for j in range(i+1, len(arr)):
      right = max(right, arr[j])
    res += min(left, right) - arr[i]

  return res

def v2(arr):
  n = len(arr)
  if n == 0:
    return 0
  left_max = [0] * n
  right_max = [0] * n

  left_max[0] = arr[0]
  for i in range(1, n):
    left_max[i] = max(left_max[i-1], arr[i])

  right_max[n-1] = arr[n-1]
  for i in range(n-2, -1, -1):
    right_max[i] = max(right_max[i+1], arr[i])

  res = 0
  for i in range(n):
    res += min(left_max[i], right_max[i]) - arr[i]

  return res

print(v2(arr))