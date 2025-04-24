#• możliwe jest wycięcie określonego kawałka tekstu za jednym razem
#• w tym celu do ideksu wstawiamy dwukropek
#Przykład:
zmienna = 'jakas zmienna'
wycinek1 = zmienna[:5] # -> ‘jakas’
wycinek2 = zmienna[6:] # -> ‘zmienna’
wycinek3 = zmienna[3:8] # -> ‘as zm’
print(wycinek1, wycinek2, wycinek3)
#• wycinek jest w granicach od n do m-1