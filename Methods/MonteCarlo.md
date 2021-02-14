

```python
# -------------------------------------------------------------
# Required Packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# -----------------------------------------------------
# this 1st functions is done by Lukas and I built upon it
# to get the round average value at each probablity between (0,1)


def mc(n=10**6, p=0.5):
    rounds = []
    for _ in range(n):
        r, losses = 0, 0
        while losses != 2:
            r += 1
            if np.random.random() <= p:
                losses = 0
            else:
                losses += 1
        rounds.append(r)
    return np.mean(rounds)
```
