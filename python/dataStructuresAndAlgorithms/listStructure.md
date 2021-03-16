```python
mylist.insert(locationIndex, value)
mylist.append(value)
mylist.extend(newlist)
mylist.pop(index) # delete the element in index
del mylist[index:index]
mylist.remove(element)
mylist1 + mylist2 # like extend
mylist1 * 4 # 4 time repeats
max(mylist)
min(mylist)
sum(mylist)
a = 'spam'
b = list(a)
b = string.split()
'a'.join(mylist)


mylist = mylist.sort() # avoid return none
mylist = mylist + [10]
```

# list vs arrays

## Similarities

- both data structures are mutable
- both can be indexed and iterated
- can sliced

## Differences

- array for arithmatic operations
  np.array(mylist)/2 can be done
- np.array([1,2,2,4,'a']) all converted to string
