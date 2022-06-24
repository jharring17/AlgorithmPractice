# Single for loop (sorted at the end)
# Time Complexity: O(nlogn), Space Complexity O(n)
def sortedSquaredArray(array):
    squaredArray = [0 for i in array]
    for i in range(len(array)):
        squaredArray[i] = array[i] * array[i]
        print(squaredArray[i])
    squaredArray.sort()         # This is the reason for the nlog(n) time.
    return squaredArray
    
print(sortedSquaredArray([1, 2, 3, 4, 5, 6, 8, 9]))