#żeby dodać element do słownika wystarczy odnieść się do jego klucza
slownik = {1: 'jeden', 2: 'dwa', 3: 'trzy'}
slownik['nowy'] = 'element'
print(slownik)
#wynik: {1: ‘jeden’, 2: ‘dwa’, 3: ‘trzy’, ‘nowy’: ‘element’}
#Element słownika jest dodawany na końcu nie ma to natomiast znaczenia ponieważ w słownikach
#nie odnosimy się do indeksu. Nie obchodzi nas czy dany klucz znajduje się w jakiejś konkretnej
#lokalizacji.