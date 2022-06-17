# For Loop 
# Time Complexity = O(n), Space Complexity = O(1)
def isValidSubsequence(array, sequence):
    currentNum = 0
    for value in array:
        if currentNum == len(sequence):
            break
        if sequence[currentNum] == value:
            currentNum += 1
    return currentNum == len(sequence)

print(isValidSubsequence([2, 3, 5, 6, 7], [3, 6, 7]))