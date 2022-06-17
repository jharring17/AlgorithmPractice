# Sorted List 
# Time Complexity: O(nlog(n)), Space Complexity O(1)
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
            currentSum = array[left] + array[right]
            if currentSum == targetSum:
                return [array[left], array[right]]
            elif currentSum < targetSum:
                left += 1                               # Move left pointer 1 position right.
            elif currentSum > targetSum:
                right -= 1                              # Move right pointer 1 position left.
    return []

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
# returns [-1, 11]