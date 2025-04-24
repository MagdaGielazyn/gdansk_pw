#metoda pozwala na aktualizację słownika
slownik = {1: 'jeden', 'dwa': 2, 3.5: False}  
slownik.update({3: 'trzy'})
print(slownik)
#update()
#wynik: {1: ‘jeden’, ‘dwa’: 2, 3.5: False, 3: ‘trzy’}
slownik.update({1: 'niespodzianka'})
print(slownik)
#wynik: {1: ‘niespodzianka’, ‘dwa’: 2, 3.5: False, 3: ‘trzy’}