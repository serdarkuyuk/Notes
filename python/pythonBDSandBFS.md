#Comparision of BDS and BFS


In qeue and stack structure as well as recursion



```python
from collections import deque
grid = [["1","1","0","0","1"]]

class Solution:
    def __init__(self, grid):
        self.grid = grid
        self.lengthColumn = len(grid[0]) if self.grid else 0
        self.lengthRow = len(grid) if self.grid else 0
        self.island = 0
        self.possbileMove = [(1,0),(0,1),(-1,0),(0,-1)]

    def legalCoord(self, i, j):
        # lengthColumn, lengthRow
        if i < 0 or i >= self.lengthRow or j < 0 or j >= self.lengthColumn:
            return False
        else:
            return True

    def bfs(self, i, j):
        qeue = deque()
        qeue.append((i, j))
        while qeue:
            i, j = qeue.popleft()
            grid[i][j] = "0"
            for move in self.possbileMove:
                nexti, nextj = i+move[0], j+move[1]
                if self.legalCoord(nexti,nextj) and grid[nexti][nextj] == "1":
                    qeue.append((nexti, nextj))


    def dfsRecursion(self, i, j):
        if grid[i][j] == "0":
            return
        grid[i][j] = "0"
        for move in self.possbileMove:
            nexti, nextj = (i+move[0]), (j+move[1])
            # print(nexti, nextj)
            if self.legalCoord(nexti, nextj) and grid[nexti][nextj] == "1":
                self.dfsRecursion(nexti, nextj)

    def dfsStack(self, i, j):
        stack = [(i,j)]
        while stack:
            i, j = stack.pop()
            grid[i][j] = "0"
            for move in self.possbileMove:
                nexti, nextj = i + move[0], j + move[1]
                if self.legalCoord(nexti, nextj) and self.grid[nexti][nextj] == "1":
                    stack.append((nexti, nextj))


    def numIsland(self):
        for i in range(self.lengthRow):
            for j in range(self.lengthColumn):
                if grid[i][j] == "1":
                    self.island += 1
                    self.dfsStack(i, j)

                    # print(island)
        return self.island


result = Solution(grid)
print(result.numIsland())
# print(result.grid)
```
