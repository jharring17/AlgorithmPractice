# Three Largest Numbers
# Time Complexity O(N) / Space Complexity O(1)
def findThreeLargestNumbers(array):
    largest_tuple = []
    for element in range(len(array)):
        # Checks for the correct length of tuple.
        if len(largest_tuple) < 3:
            largest_number = max(array)
            largest_tuple.append(largest_number)
            array.remove(largest_number)
        # Exits the loop when tuple length is 3.
        else:
            largest_tuple.sort()
            exit
    return largest_tuple

array = [141, 1, 17, -1, -17, 18, 541, 8, 7, 7, 541]
print(findThreeLargestNumbers(array))