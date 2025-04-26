#domyślna wartość
#Otwiera plik tylko do odczytu.
#UWAGA!! Podanie modu, nie powoduje odczytu jego zawartości
#Przykład:
#plik = open('jakis_plik.txt') print(plik)
#wynik:<_io.TextIOWrapper name='def.txt' mode='r' encoding='cp1252’> jeżeli plik o podanej nazwie nie istnieje, otrzymujemy ERR

#Żeby otrzymać zawartość pliku, należy użyć metody read() Przykład:
#plik = open(‘jakis_plik.txt’) print(plik.read())
#wynik: To jest zawartość tego pliku. Żeby odczytać część pliku, w nawiasie metody read() należy podać wartość
#print(plik.read(7))
#wynik: To jest
#Ponieważ plik jest sekwencją linii można na nim zastosować metody jak przy innych
#sekwencjach w tym iteracje

#plik = open(‘jakis_plik.txt’) 
#licznik = 0
#for linia in plik:
#licznik += 1
#print(‘Liczba linii w pliku to: ‘ +str(licznik))
#Dobrą praktyką jest przechowywanie odczytanej zawartości pliku jako zmiennej Przykład:
#plik = open(‘jakis_plik.txt’) odczyt = plik.read()
#powinno się zawsze zamknąć plik, po skończonych operacjach plik.close()
#Zwróccie uwagę, że można użyć innnych metod dla otwartego pliku I dla odczytanego pliku
#plik = open(‘jakis_plik.txt’)
#odczyt =plik.read()
#print(dir(plik))
#print(dir(odczyt)) !!!Tych metod moża użyć do filtrowania tekstu

