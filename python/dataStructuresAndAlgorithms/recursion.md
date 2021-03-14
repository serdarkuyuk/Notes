```python
def openRussianDoll(doll):
    if doll == 1:
        print("base condition")
    else:
        openRussianDoll(doll-1):
```

- if problem can be dividable to subproblems,
- if the subproblem is similar to main problem in nature
- trees and graphs
- it is used in many algorithms (divide and conquer, greedy and dynamic programming)

- cons and pros
  all recursive algorithms can be written iteratively
  iteration is better in space and time complexity
  Iteration no stack memory require
  Recursion pop and push elements in stack memory
- use cases
  Recursion is easy to code
  if the input is large, do not use recursion
  when traverse a tree use recursion
  when we use memoization in recursion
  recursion can be slow
  do not use if time and space complexity matters

how to write recustion in 3 steps

Step 1. Recursive case - the flow
n! = n \* (n-1)!
Step 2. Base case - the stopping criterion
0! = 1 or 1! = 1
Step 3. Unintentional case - the constraint
