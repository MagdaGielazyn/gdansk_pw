#nie jest możliwe nadpisanie pojedynczego znaku (elementu) w ciągu (obiekcie)
#• ciąg znaków jest niezmienny
#• możliwe jest:
#o nadpisanie całej zmiennej (zamiana ciągu na inny)
#o utworzenie nowej zmiennej i manipulacje pomiędzy zmiennymi
#Przykład:
zmienna = 'jakas zmienna'
nowa_zmienna = 'inna ' + zmienna[6:]
print(nowa_zmienna)