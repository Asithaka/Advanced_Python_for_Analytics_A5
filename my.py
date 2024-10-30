import pandas as pd

import random

list1 = [random.randrange(1,10) for i in range(0,101)]

s = pd.Series(list1)
print(s)

result = s.value_counts()
print(result)

