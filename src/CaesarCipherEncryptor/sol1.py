# Simple For Loop
# Time Complexity: O(n), Space Complexity O(n)
def caesarCipherEncryptor(string, key):
    # Take an input string and shift every letter by key.
    result = []
    for i in range(len(string)):
        converted = chr((((ord(string[i]) - 97) + key) % 26) + 97)
        result.append(converted)
    return "".join(result)


