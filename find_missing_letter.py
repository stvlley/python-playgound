
string = 'abcdefghijklmnopqrstuvwyz'

def find_missing_letter(string):
    # strore all encountered letters in a hash table
    hashMap = {}
    for letter in string:
        hashMap[letter] = True
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in hashMap:
            return letter
       

print(find_missing_letter(string))