def missingElement(array):

    """
    finds missing element in O(n)
    """

    lastElement = array[-1]
    trueSummation = lastElement * (lastElement + 1) / 2
    actualSummation = sum(array)

    return trueSummation - actualSummation


mylist1 = list(range(1, 53))
mylist2 = list(range(54, 1000))
# print(missingElement(mylist1 + mylist2))

import numpy as np
from random import random

# myArray = np.array(range(21))
# print(myArray)


def findNumber(inputArray, inputNumber):
    for number in myArray:
        if number == inputNumber:
            return number
    else:
        return "there is no number"


# print(findNumber(myArray, 90))
myArray2 = np.random.randint(57, size=20)
# print(myArray2)


def findMaxProduct(inputNumber):

    firstMax, secondMax = float("-inf"), float("-inf")

    for number in inputNumber:
        if number > firstMax:
            firstMax, secondMax = number, firstMax
        elif firstMax > number and number > secondMax:
            secondMax = number

    return firstMax, secondMax


# print(findMaxProduct(myArray2))


def isUnique(inputArray):
    uniqueList = []
    for number in inputArray:
        if number not in uniqueList:
            uniqueList.append(number)
        else:
            return number


# print(myArray2)
# print(isUnique(myArray2))

# myArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
myArray = np.array([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
print(myArray)


def rotate90(myArray):

    left, right = 0, len(myArray) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right

            temp = myArray[top][left + i]
            myArray[top][left + i] = myArray[bottom - i][left]
            myArray[bottom - i][left] = myArray[bottom][right - i]
            myArray[bottom][right - i] = myArray[top + i][right]
            myArray[top + i][right] = temp
        left += 1
        right -= 1

    return myArray


print(rotate90(myArray))
