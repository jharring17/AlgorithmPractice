# Single for loop 
# Time Complexity: O(n), Space Complexity O(n)
def sortedSquaredArray(array):
    sortedArray = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedArray[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedArray[idx] = largerValue * largerValue
            largerValueIdx -= 1
    return sortedArray

print(sortedSquaredArray([1, 2, 3, 4, 5, 6, 8, 9]))
