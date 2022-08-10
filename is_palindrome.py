import re

string = 'race, car'

def is_palindrome(string):
    # create two pointers for the left and right
    string = string.lower()
    string = re.sub('[^0-9a-zA-Z]+', '', string)
    left = 0
    print(string)
    right = len(string) - 1
    # interate till left reaches the middle of the array
    while left < len(string) / 2:
        # if char on left doesnt equal char on right it is not a palindrome
        if string[left] != string[right]:
            return False
        # move left and right
        left += 1
        right -= 1
    return True

print(is_palindrome(string))