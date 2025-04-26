#Napisz program, który zasymuluje “magic 8-ball”. Użytkownik zadaje pytanie, na które
#odpowiedź jest tak lub nie. Magiczna kula pokazuje mu odpowiedź.
#Możliwe odpowiedzi kuli:
#1) Tak
#2) Nie ma mowy
#3) Tylko kula wie
#4) Bezwzględnie
#5) Zapytaj później
#Przykładowy output:
#Czy dostanę awans?
#Tylko kula wie

import random

odp1 = 'Tak'
odp2 = 'Nie ma mowy'
odp3 = 'Tylko kula wie'
odp4 = 'Bezwzględnie'
odp5 = 'Zapytaj później'
question = input('Zadaj mi pytanie: ')

while question != '':
    odp = random.randint(1,5)
    if odp == 1:
        print(odp1)
    elif odp == 2:
        print(odp2)
    elif odp == 3:
        print(odp3)
    elif odp == 4:
        print(odp4)
    elif odp == 5:
        print(odp5)
    question = input('Zadaj mi pytanie: ')