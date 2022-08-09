


list = [1, 2, 5, 7, 3, 9]

def bubble_sort(list):
    # create the right pointer at the end or the list
    unsorted_until_index = len(list) - 1
    # establish sorted to be false
    sorted = False
    # while loop that continue to run while the list is not sorted
    while not sorted:
        # priliminarily establish sorted to be true
        sorted = True
        # for loop which we point to each pair of values
        for i in range(unsorted_until_index):
            # compare the values if left is less than right
            if list[i] > list[i+1]:
                # if they are swap them
                list[i], list[i+1] = list[i+1], list[i]
                # and sinse we had to swap we change sorted to equal false
                sorted = False
        # decrement sinse the pointer it was pointing to is now sorted
        unsorted_until_index -= 1
    # return list
    return list

print(bubble_sort(list))