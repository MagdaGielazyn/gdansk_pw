#Utwórz słownik, a następnie podnieś jego wszystkie wartości do kwadratu jeśli wartość jest liczbą całkowitą
#slownik = {1:1, 2:2.5, 3:3.9, 4:4, 5:4.3,6:4.5}

slownik = {1:1, 2:2.5, 3:3.9, 4:4, 5:4.3,6:4.5}
nowy_slownik = {klucz:wartosc**2 for (klucz,wartosc) in slownik.items() if wartosc == int(wartosc)}

print(nowy_slownik)