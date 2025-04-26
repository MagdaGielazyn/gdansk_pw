#Napisz program, który wygeneruje 2 losowe liczby z zakresu od 0 do 99 i je dodać. Użytkownik
##próbuje zgadnąć odpowiedź. Program mu mówi czy zgadł dobrze
#Oczekiwany output:
#Jaka jest suma 58+45? Jaka jest suma 58+45?
#Twoja odpowiedź: 103 Twoja odpowiedź: 130
#Odpowiedź prawidłowa! Źle! Poprawna odpowiedź to 103

import random
MIN = 0
MAX = 99

num1 = random.randint(MIN, MAX)
num2 = random.randint(MIN, MAX)

sum = num1 + num2

user = int(input(f'Jaka jest suma {num1} i {num2}?'))
if user == sum:
    print('Odpowiedz prawidlowa')
else:
    print(f'Źle! Poprawna odpowiedź to {sum}')