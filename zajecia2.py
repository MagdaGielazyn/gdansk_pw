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

'''
import math as mt3



number = input('Podaj liczbe') 

print(f'pierwiatek kwadratowy z liczby {number} to {mt3.sqrt(int(number))}')
print('pierwiastek kwadratowy z liczby', number)