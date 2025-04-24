#• ponieważ krotki są niezmienne, trzeba sobie poradzić inaczej
#Przykład:
krotka = (1, 2, 3)
lista = list(krotka)
lista[1] = 8
krotka = tuple(lista)
print(krotka)