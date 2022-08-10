


from turtle import pos
from numpy import positive


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

def selectionSort(array):
    size = len(data)
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]
selectionSort(data)
print('Sorted Array in Ascending Order:')
print(data)


def insertionSort(array):
    for index in range(1, len(array)):
        temp_value = array[index]
        position = index - 1

        while position >= 0:
            if array[position] > temp_value:
                array[position + 1] = array[position]
                position = position - 1
            else:
                break
        array[position + 1] = temp_value
    return array

print(insertionSort(list))