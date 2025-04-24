#podobnie jak w przypadku listy indeksy zapisujemy w nawiasch kwadratowych
#• indeksy zaczynają się od 0
krotka = (1, 'numer')
print(krotka[1]) #wynik: ‘numer’
#Można stosować również funkcje takie jak:
#• type()
#• len()
#• indeksy ujemne
#oraz operacje na krotkach:
#• wycinki
print(krotka[:5])
print(krotka[5:])
print(krotka[2:5])
print(krotka[-3:-2])
#• sprawdzenie czy element istnieje
if 'numer' in krotka:
    print('istnieje')