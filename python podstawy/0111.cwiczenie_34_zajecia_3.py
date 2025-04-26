#Napisz program, który wypisze liczbę elementów, które są unikalne na liście. lista = [‘k’, 2, 5, 2, ‘mop’, 5.4, ‘k’, 8, False]
#Oczekiwany output:
#Liczba unikalnych elementów to 7


lista = ['k', 2, 5, 2, 'mop', 5.4, 'k', 8, False, False, True]
nowa_lista = []
count_l = 0
for x in lista:
    if x not in nowa_lista:
        nowa_lista.append(x)
        count_l +=1
 
print(f'Liczba unikalnych elementow na liscie to {count_l}')

