#• tak jak przy stringach I listach można użyć funkcji dir() oraz help()
#• żeby odnieść się do kluczy w słowniku należy użyć metody keys()
#• żeby odnieść się do wartości w słowniku używamy metody values()
#• żeby odnieść się do i wartości w słowniku używamy metody items()
#Przykład:
slownik = {1: 'jeden', 'dwa': 2, 3.5: False}    
for i in slownik.keys(): 
    print(i)   

for i in slownik.values(): 
    print(i)

#można użyć tylko nazwę slownika (bez metody), wtedy Python potraktuje to jako metodę
#keys():
for i in slownik.keys():
    print(i) 


for i in slownik: 
    print(i)