#Stwórz pusty plik, następnie poproś użytkownika, żeby podał treść. Sprawdź czy możesz zapisać tę treść do pliku.
#Jeśli tak, to zapisz.
#Na koniec powiedz użytkownikowi ile podał znaków.

def tworzenie():
    kotek = open('kotek.txt', 'x')
    kotek.close()

def podanie_tresci(tresc):
    kotek = open('kotek.txt', 'w')
    if kotek.writable() ==1:
        kotek.write(tresc)
    kotek.close()

def czytanie():
    kotek = open('kotek.txt', 'r')
    dlugosc = len(kotek.read())
    print(f'Dlugosc  pliku to {dlugosc} znakow.')
    kotek.close()

def main():
    tworzenie()
    tresc = 'kotek \npapuzka \nsmuteczek'
    podanie_tresci(tresc)
    czytanie()

main()