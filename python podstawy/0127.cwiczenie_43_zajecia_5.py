#Stwórz tablicę, a następnie zamień wszystkie liczby nieparzyste na wartość -1
import numpy as np
tab = np.arange(10)
tab[tab%2 !=0] = -1
print(tab)

