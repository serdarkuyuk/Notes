# Linked List

head -> node -> tail
node (value, reference2nextNode)
tail(value, None)

linked list vs Arrays

- if we delete an element in array, the space in memory is not deleted. all values are moved to the left but allocated memory will be same
- there is no restriction in memory you need to declare with linkedlist
- insertion and removels in linked list are very efficient
- but it is not indexed so finding is time consume
- random access is very easy in arrays

Four type of linked list

1. singly
2. cicular singly
   last node gives the first node
3. doubly
   (referenceBefore, Value, referenceNext)
4. circular doubly
   tail
   (referenceBefore, Value, firstNode)


|-|Time|Space|
|---|---|---|
|creation|O(1)|O(1)|
|Insertion|O(n)|O(1)|
|searching|O(n)|O(1)|
|traversing|O(n)|O(1)|
|deletion of a node|O(n)|O(1)|
|deletion of linked list|O(1)|O(1)|
#

# Comparison

|Time Complexity|Array|Linked List|
|---|---|---|
|creation|O(1)|O(1)|
|Insertion at first position|O(n)|O(1)|
|Insertion at last position|O(1)|O(1)|
|Insertion at n position|O(n)|O(n)|
|searching unsorted|O(n)|O(n)|
|searching sorted|O(logn)|O(n)|
|traversing|O(n)|O(n)|
|deletion at first position|O(n)|O(1)|
|deletion at last position|O(1)|O(1)|
|deletion at n position|O(n)|O(n)|
|deletion of array/linked list|O(1)|O(1)|
|access nth element|O(1)|O(n)|