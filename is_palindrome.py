string = 'racecar'

def is_palindrome(string):
    # create two pointers for the left and right
    left = 0
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