# Stwórz tablicę, która będzie posiadała tylko element wspólne poniższych tablic 
#tab1=[0 1 2 3 4 5 6 7 8 9]
#tab2=[3 1 13 557 92 0 6 80 43 9]


import numpy as np
tab1 = np.arange(10)
tab2 = np.array([3, 1, 13 ,557, 92, 0, 6, 80, 43, 9]) 
tab3 = np.where(tab1==tab2)
print(tab3)
