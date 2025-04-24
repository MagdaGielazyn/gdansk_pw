#get()
#metoda get() pozwala wywołać wartość konkretnego klucza
slownik = {1: 'jeden', 'dwa': 2, 3.5: False}  
print(slownik.get('dwa'))

#wynik: 2

print(slownik.get(3))
#wynik: None
