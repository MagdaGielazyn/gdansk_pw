'''
STALE:
--> UPPER_CASE_SNAKE
ich wartosc nie zostanie nadpisana
tu nie ma rownan, sa wartosci niezmiennej
zaczynamy od wielkiej litery - da sie je latwo rozpoznac
dajemy je w miare na poczatku kodu
'''
'''
PI = 3.14
INCH_TO_CM = 2.54

inch = float(input('Podaj liczbe cali'))
cm = inch * INCH_TO_CM'

NAME = 'Gosia'
NUMBER = 5
FRUIT = 'truskawki'
VALUE = '30 PLN'
YEARS = 9

print(f'Byl sobie czarodziej o imieniu {NAME} ktory uwielbial jesc {FRUIT}. {NAME} zawsze trzymal zapas {NUMBER} {FRUIT} w swojej lodowce!')

MARS_MULTIPLE = 0.378
weight_on_earth = input('podaj wage na ziemi')
weight_on_mars = float(weight_on_earth)* MARS_MULTIPLE
print(weight_on_mars)


# import bibliotek powinien byc na gorze w kodzie
#import bibl
import pandas as pa 

#import bibl jako alias 
import numpy as np

#import elemnetu
#from bibl import element

import math as mt3



number = float(input('Podaj liczbe'))

print(f'pierwiatek kwadratowy z liczby {number} to {mt3.sqrt(int(number))}')
print('pierwiastek kwadratowy z liczby', number, 'to', mt3.sqrt(int(number)))
'''

import random

'''

random.randint(min,max) #zwraca losowy integer z przedzialu min max, wlacznie
random(random) #zwraca losowy float z przedzialu 0 do 1
random.uniform(min, max) #zwraca losowy float z przedzialu min max
random.seed(x) #ustawia seed losowego generatora



first_number = random.randint(1,6)
second_number = random.randint(1,6)
print(first_number, second_number, first_number + second_number)


NUM_SIDES = 6
die1 = random.randint(1, NUM_SIDES)
die2 = random.randint(1, NUM_SIDES)
total = die1 + die2



and x>2 and x<10
or x<2 or x>10
not not(x>y)  # sprawdzi sie jesli warunek jest falszywy '

if warunek:
    instrukcja'

procent = int(input('Podaj procent: '))
if procent < 100 and procent > 50:
    print('Zdales! Gratulacje!')
elif procent > 0 and procent <50:
    print('Nie zdales. Moze kiedys')
else:
    print('Cos tu poszlo nie tak')


if x == y:
    print('x i y sa rowne')
else:
    if x< y:
        print('x i y sa rowne')
    elif x> y:
        print('x i y sa rowne') 



        

year = int(input('Podaj rok: '))
if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
    print('Rok jest przestepny')
else:
    print('Rok nie jest przestepny')

year = int(input('Podaj rok: '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Rok jest przestepny')
        else:
              print('Rok nie jest przestepny')
    else:
        print('Rok jest przestepny')
else:
    print('Rok nie jest przestepny')
    
while warunek:
    instrukcja
    
x = 0
while True:
    print(x)
    x+=1


num = int(input('Podaj liczbe'))
suma = num

while num !=0:
    print('Suma do tej pory to' + str(suma))
    num = int(input("Podaj liczbe: "))
    suma = suma + num

x=0
while x < 8:
    print(x)
    break
    x+=1


x = 0 
while x < 6:
    x+=1
    if x == 3:
        continue 
    =
    +=
    -=
    *=
    /=
    %=
    //=
    **=

    

LIMIT = 1000

fib1 = 0
fib2 = 1
fib_next = 0

while fib_next <= LIMIT:
    print(fib1)
    fib_next = fib1 + fib2
    fib1 = fib2
    fib2 = fib_next


for x in range(0, 10):
    print(x)

for x in range(0, 3):
    for y in range(0, 2):
        print(x, y)



string = 'llaa'
for x in string:
    print(x)

for x in range (0,10,2):
    print(x)
    '''


num = int(input('Podaj liczbe: '))
cnt_f=0
cnt_b=0
cnt_fb=0
for x in range(1, num+1):
    if (x % 3 == 0) and (x % 5 ==0):
        print('FizzBuzz')
        cnt_fb+=1 # cnt_fb=cnt_fb+1
    elif x % 5 == 0:
        print('Buzz') 
        cnt_b+=1
    elif (x % 3 == 0):
        print('Fizz')
        cnt_f+=1
    else:
        print(x)
    
print(cnt_b,cnt_f, cnt_fb )

'''
def