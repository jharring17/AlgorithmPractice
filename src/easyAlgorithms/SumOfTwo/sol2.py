# Hash Table
# Time Complexity: O(n), Space Complexity O(n)
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = (targetSum - num)
        if potentialMatch in nums: # (targetSum - num = y)
            return [targetSum - num, num]
        else:
            nums[num] = True
    return []

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))