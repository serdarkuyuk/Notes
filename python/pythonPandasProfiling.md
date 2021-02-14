
```python
import pandas as pd
from pandas_profiling import ProfileReport
import numpy as np

# on goole colab
! pip install https://github.com/pandas-profiling/pandas-profiling/archive/master.zip

profile = ProfileReport(df, title='Pandas Profiling Report', html={'style':{'full_width':False}})

profile.to_notebook_iframe()
profile.to_file(output_file="REPORT.html")

https://github.com/pandas-profiling/pandas-profiling.git
