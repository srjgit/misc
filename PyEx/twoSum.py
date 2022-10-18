def twoSum(nums, target):
    seen = {}
    for i in nums:
        if target-i in seen:
            return [i, target-i]
        else:
            seen[i] = 1

    return []

nums = [2, 7, 8, 1, 4]
target = 9
print(twoSum(nums, target))
