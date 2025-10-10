nums = [1, 2, 3, 4, 2]

def v1(nums):
    visited = [False] * (len(nums) - 1)
    for i in nums:
        if visited[i-1]:
            return i
        visited[i-1] = True

    return -1

def v2(nums):
    duplicate = -1
    for i in range(len(nums)):
        val = -nums[i] if nums[i] < 0 else nums[i]
        if nums[val] >= 0:
            nums[val] = -nums[val]
        else:
            duplicate = val
            break
    # Restoring the original list
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = -nums[i]

    return duplicate

def v3(nums):
    xor = 0
    for x in nums:
        xor ^= x
    for i in range(1, len(nums)):
        xor ^= i

    return xor

def v4(nums):
    actual_sum = sum(nums)
    expected_sum = len(nums) * (len(nums) - 1) // 2

    return actual_sum - expected_sum

print(v4(nums))