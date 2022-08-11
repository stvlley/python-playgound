from numpy import array


array1, array2 = [1,2,3,4,5], [1,3,6]

def getIntersection(array1, array2):
    intersection = []
    for element in array1:
        if element in array2:
            intersection.append(element)

    return intersection

print(getIntersection(array1, array2))

