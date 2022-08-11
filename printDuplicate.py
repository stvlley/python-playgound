from numpy import arange, array2string


array = ['a', 'b', 'c', 'd', 'c']

def printDuplicate(array):
    # declare list store duplicated
    n = len(array)
    dup = []
    for i in range(n):
        k = i + 1
        for j in range(k, n):
            if array[i] == array[j] and array[i] not in dup:
                dup.append(array[i])

    return dup

print(printDuplicate(array))