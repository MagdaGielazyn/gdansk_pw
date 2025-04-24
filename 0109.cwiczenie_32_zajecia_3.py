#Napisz program, który policzy ile z każdej litery występuje w słowie “rabarbar”
#Oczekiwany output:
#W slowie "rabarbar" występuja 3 litery "r“ W slowie "rabarbar" występuja 3 litery "a“ W slowie "rabarbar" występuja 2 litery "b"

slowo = input('Podaj slowo:')

slownik = {}

for x in slowo:
    if x not in slownik:
        slownik[x] = 1
    else:
        slownik[x] += 1

for i in slownik:
    print(f'W slowie {slowo} jest {slownik[i]} liter {i}.')

