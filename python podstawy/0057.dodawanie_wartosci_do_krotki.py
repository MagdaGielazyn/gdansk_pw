#krotka nie posiada metody append, należy zastosować inne metody
#1. Konwersja do listy 
#Przykład: 
krotka = (1, 2, 3) 
lista = list(krotka) 
lista.append(4) 
krotka = tuple(lista)

#2. Dodanie kilku krotek
#Przykład: 
krotka1 = (1, 2, 3)
krotka2 = (4,)
krotka1 += krotka2

