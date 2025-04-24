#Sposób na wygenerowanie losowych wartości
#Nie można uzyskać w technice komputerowej prawdziwej losowości, więc używamy liczb
#pseudolosowych
#Aby zastosować wartości losowe, należy zaimportować bibliotekę random:

import random

#Funkcja Działanie
#random.randint(min, max) Zwraca losowy integer z przedziału od min do max, włącznie
#random.random() Zwraca losowy float z przedziału od 0 do 1
#random.uniform(min, max) Zwraca losowy float z przedziału od min do max
#random.seed(x) Ustawia “seed” losowego generatora liczb jako x

print(random.randint(1, 10))
print(random.uniform(1, 10))
print(random.random())
print(random.seed(4))