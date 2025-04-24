slownik = {1: 'jeden', 'dwa': 2, 3.5: False}  

if slownik.get(3) in słownik.values(): 
    print('Taka wartość jest w słowniku')
else:
    #print(‘Takiej wartości nie ma w słowniku’)
#inna wersja:

if 3 in slownik:
    print('Taka wartość jest w słowniku')
else:
    print('Takiej wartości nie ma w słowniku')