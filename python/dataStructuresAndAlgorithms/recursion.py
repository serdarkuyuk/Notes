import sys

sys.setrecursionlimit(10000)


def recursionMethod(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursionMethod(n - 1)
        print(n)


# recursionMethod(4)


def factorial(n):
    assert n <= 1 and int(n) == n, "The number must be positive integer only!"
    if n in [0, 1]:
        return 1
    else:
        # print(n)
        return n * factorial(n - 1)


# print(factorial(2.2))


def fibonacci(n):

    assert n >= 1 or int(n) == n, "The fibonacci number must be positive integer number"
    if n in [1, 2]:
        return n - 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(6.8))


def sumOfDigits(n):
    assert n > 0 and int(n) == n, "The number should be postive number"
    if n == 0:
        return 0
    else:
        # digit = n % 10
        # n = n // 10
        # return digit + sumOfDigits(n)
        return n % 10 + sumOfDigits(n // 10)


# print(sumOfDigits(1324123412346425635))


def powerOfNumber(number, power):
    assert power >= 0 and int(power) == power, "Power should be positive number"
    if power == 0:
        return 1
    # elif power == 1:
    #     return number
    else:
        return number * powerOfNumber(number, power - 1)


# print(powerOfNumber(4, 1))


def greatestCommonFactor(number1, number2):
    assert (
        int(number1) == number1 and int(number2) == number2
    ), "The numbers must be integer only"
    if number1 < 0:
        number1 = -1 * number1
    if number2 < 0:
        number2 = -1 * number2
    if number2 == 0:
        return number1
    else:
        remainder = number1 % number2
        return greatestCommonFactor(number2, remainder)


# print(greatestCommonFactor(40, -2))


def decimal2binary(n):
    assert int(n) == n, "You should reconsider"
    if n == 0:
        return 0
    else:
        return 10 * decimal2binary(n // 2) + n % 2


# print(decimal2binary(40))


def findMaxNumber(arr):
    # n = length(arr)
    if len(arr) == 1:
        return arr[0]
    else:
        return max(findMaxNumber(arr[1:]), arr[0])


print(findMaxNumber([1, 2, 7, 5]))