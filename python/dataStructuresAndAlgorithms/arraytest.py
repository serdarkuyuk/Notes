from array import *

my_array = array("i", [1, 2, 3, 4, 5])

for i in my_array:
    print(i)

print(my_array[0])

my_array.append(6)

my_array.insert(2, 100)


my_array.extend([3, 2, 1])
templist = [20, 21, 22]

my_array.fromlist(templist)

my_array.remove(1)
my_array.pop()

# gives the index of given number
my_array.index(100)

# reverse the array
my_array.reverse()

# shows the memory information and number of elements
print(my_array.buffer_info())

# how many of this element occur
print(my_array.count(3))
# tempstring = my_array.tostring()
# print(tempstring)

# convert array to list
my_array.tolist()

# slice

print(my_array)

import numpy as np

twoArray = np.array([[1, 2, 3, 4], [6, 3, 5, 4], [8, 5, 3, 1], [9, 6, 4, 2]])

newtwoArray = np.insert(twoArray, 2, [[2, 2, 2, 2]], axis=0)

newtwoArray = np.append(twoArray, [[2, 2, 2, 2]], axis=0)
print(twoArray)
print(newtwoArray)


def accessElement(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print("incorrect index")
    else:
        return array[rowIndex][colIndex]


# print(accessElement(twoArray, 1, 2))


def traverseArray(array):

    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


# print(traverseArray(twoArray))
def linearSearchArray(array, element):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if (array[i][j]) == element:
                return (i, j)
    return "There is no number"


# print(linearSearchArray(twoArray, 40))

# delete

newtdArray = np.delete(twoArray, 0, axis=1)
print(newtdArray)