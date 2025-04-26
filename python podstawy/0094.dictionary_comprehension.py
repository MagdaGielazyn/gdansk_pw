#Podobnie jak w przypadku list składowych można zastosować dictionary comprehension: 
slownik = {
1:'jeden',
2:'dwa', 
3:'trzy', 
4:'cztery'}
nowy_slownik = {klucz:wartosc for (klucz,wartosc) in slownik.items()} 
print(nowy_slownik)