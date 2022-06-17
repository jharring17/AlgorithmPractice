# Two For Loop Method
# Time Complexity: O(n^2), Space Complexity O(1)
def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                    return [firstNum, secondNum]
    return []

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
