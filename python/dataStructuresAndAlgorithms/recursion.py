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


print(powerOfNumber(4, 1))