#Każda wartość typu string to sekwencja/ciąg znaków, np.: zmienna = ‘jakas zmienna’
#• Indeksy ciągów zaczynają się od 0
#j a k a s z m i e n n a
#0 1 2 3 4 5 6 7 8 9 10 11 12
#• indeksy podajemy w nawiasach kwadratowych []
#• indeksy zawsze muszą być liczbą całkowitą (int)
#• można używać indeksów wstecz (-1, -2…)
#Przykład:
zmienna = 'inna zmienna'
litera = zmienna[5]
print(litera) #wynikiem zmiennej o nazwie litera będzie “ ”.
#• indeks musi być liczbą mniejszą lub równą ilości znaków w sekwencji
#• można zastosować funkcję len(), która zwraca długość stringa
#• funkcję len() można zastosować jako parametr określający miejsce w ciągu
#Przykład:
zmienna = 'to jest jakiś ciąg znaków'
ostatnia_litera = zmienna[len(zmienna)-1]
print(ostatnia_litera) #wynik: ‘w’