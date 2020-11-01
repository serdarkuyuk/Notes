##Comparision of BDS and BFS 
in qeue and stack structure as well as recursion



```python
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
```


```python
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
```
