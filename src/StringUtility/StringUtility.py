class StringUtility:
    # Takes string parameter and stores instance variable.
    def __init__(self, string):
        self.string = string

    # Returns internal string itself.
    def __str__(self):
        return self.string

    # Counts the number of vowels in a string.
    def vowels(self):
        counter = 0
        string = self.string
        for i in range(len(string)):
            if (string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u'):
                counter += 1
        if (counter > 5):
            return "many"
        else:
            return counter

    # Return a string first two and last two characters.
    def bothEnds(self):
        string = self.string
        length = len(string)
        result = ""
        # If string length less or equal two, return empty.
        if (len(string) <= 2):
            return ""
        # Else return the beginning two and last two characters.
        else:
            result = string[0] + string[1] + string[length - 2] + string[length - 1]
            return result

    # Change all occurrences of first char to '*'.
    def fixStart(self):
        string = self.string
        firstChar = string[0]
        newString = ""
        # Return if parameter is less than or equal one.
        if len(string) <= 1:
            return string
        # If word is greater than length one.
        else:
            # Checks the string for instances of firstChar.
            for i in range(len(string)):
                # If firstChar is in array, append to newString.
                if (string[i] == firstChar and i >= 1):
                    newString += '*'
                # If not equal to firstChar, add the character.
                else:
                    newString += string[i]
            return newString

    # Return the ascii sum of the chars.
    def asciiSum(self):
        string = self.string
        sum = 0
        for i in range(len(string)):
             sum += ord(string[i])
        return sum
    
    # Return an ecoded string.
    def cipher(self):
        string = self.string
        offset = len(string)
        result = ""
        # Irerate through the imput array.
        for i in range(len(string)):
            char = string[i]
            # If uppercase.
            if (char.isupper()):
                result += chr((ord(char) + offset - 65) % 26 + 65)
            # If lowercase.
            elif (char.islower()):
                result += chr((ord(char) + offset - 97) % 26 + 97)
            # If a character.
            else:
                result += char
        return result    

test = StringUtility("Binghampton")
vtest = test.vowels()
print(vtest)

test1 = StringUtility("laaaaaaaaa")
vtest1 = test1.bothEnds()
print(vtest1)

test2 = StringUtility("dZz*")
vtest2 = test2.cipher()
print(vtest2)

test3 = StringUtility("hello")
vtest3 = test3.fixStart()
print(vtest3)

test4 = StringUtility("hello")
vtest4 = test4.asciiSum()
print(vtest4)

test5 = StringUtility("hello")
vtest5 = test5.cipher()
print(vtest5)
