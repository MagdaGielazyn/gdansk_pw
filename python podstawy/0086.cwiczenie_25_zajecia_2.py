#Napisz program, który policzy ile jest elementów w liście (bez użycia funkcji len())

lista = [1,2,3,4,5]
count_lista = 0

for x in lista:
    count_lista +=1

print(f'Liczba elementow w liscie to {count_lista}.')