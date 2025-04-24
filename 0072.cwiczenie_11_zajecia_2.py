#Napisz program, który symuluje rzut dwiema kostkami i drukuje wyniki każdego rzutu, jak
#również sumę.
#Przykładowy output:
#Każda z kości ma 6 ścianek
#Pierwsza kość: 3
#Druga kość: 5
#Suma kości: 8

import random

SIDE = 6

dice1 = random.randint(1, SIDE)
dice2 = random.randint(1, SIDE)
sum = dice1 + dice2

print(f'Kazda z kosci ma {SIDE} scianek.')
print(f'Pierwsza kosc: {dice1}')
print(f'Druga kosc: {dice2}')
print(f'Suma kosci: {sum}')