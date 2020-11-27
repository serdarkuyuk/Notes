# Bitwise operation notes

to convert number to bin, returns string
y = 4
ny = bin(4)

## Counting ones in binary
```python
#approach 1, O(logn)
n=8
count = 0
while n:
    count += (n&1)
    n >>= 1

#approach 2, O(logn)
n=8
count = 0
while n:
    n &= (n-1)
    count += 1
```




## Hamming distance Log(n)
Brian Kernighan's Algorithm
```python
count = 0
number = x ^ y
while number != 0:
    number = number & number-1
    count += 1

#second Solution
return bin(x^y).count('1')
```

y=4
print(y << 1)
100 becomes 1000
y >> 1
100 becomes 10


## XOR operation in python

!()[http://www.bristolwatch.com/pport/pics/logic_table.gif]

return True if the numbers are different
return False if the numbers are same

```python
# 010   - 2 1st number
# 100   - 4 2nd number
# 110   - 6 result
```
print(2^4)
##

```python
print(1&1) #true
print(1&0) #False
print(0&1) #False
print(0&0) #False

print(1|1) #True
print(1|0) #True
print(0|1) #True
print(0|0) #False

print(1^1) #False
print(1^0) #True
print(0^1) #True
print(0^0) #False
```

```python
number = (1 << 2 | 1)   #100 + 1  = 5
```
