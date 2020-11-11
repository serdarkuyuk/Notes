# Bitwise operation notes

to convert number to bin, returns string
y = 4
ny = bin(4)

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
