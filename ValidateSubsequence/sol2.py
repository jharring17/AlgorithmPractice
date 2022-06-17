# While Loop 
# Time Complexity = O(n), Space Complexity = O(1)
def isValidSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)

print(isValidSubsequence([2, 3, 5, 6, 7], [3, 6, 7]))