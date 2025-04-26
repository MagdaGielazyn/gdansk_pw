#Napisz program, który zapyta użytkownika o wiek, a następnie powie mu czy może głosować w 3
#fikcyjnych krajach: Etgidi (15), Siqira (57), Gmis (25).
#Przykładowy output:
#Ile masz lat? 21
#Możesz głosować w Etgidi, gdzie wiek wyborczy to 15
#Nie możesz głosować w Siqiri, gdzie wiek wyborczy to 57
#Nie możesz głosować w Gmis, gdzie wiek wyborczy to 25

ETGIDI = 15
SIQIRA = 57
GMIS = 25

age = int(input('Ile masz lat?'))
if age >= ETGIDI:
    print(f'Możesz głosować w Etgidi, gdzie wiek wyborczy to {ETGIDI}.')
else:
    print(f'Nie możesz głosować w Etgidi, gdzie wiek wyborczy to {ETGIDI}.')
if age >= SIQIRA:
    print(f'Możesz głosować w Siqira, gdzie wiek wyborczy to {SIQIRA}.')
else:
    print(f'Nie możesz głosować w Siqira, gdzie wiek wyborczy to {SIQIRA}.')
if age >= GMIS:
    print(f'Możesz głosować w Gmis, gdzie wiek wyborczy to {GMIS}.')
else:
    print(f'Nie możesz głosować w Gmis, gdzie wiek wyborczy to {GMIS}.')