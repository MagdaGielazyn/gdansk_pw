#. Napisz program, który powie użytkownikowi czy podany przez niego rok jest przestępny czy nie.
#Aby rok uznać za przestępny muszą być spełnione warunki:
#• jest podzielny przez 4 i niepodzielny przez 100 lub
#• jest podzielny przez 400

'''
Co do zasady rok przestępny wypada raz na cztery lata. 
Zgodnie z obowiązującymi zasadami, by dany rok był rokiem przestępnym, 
musi jednak: być podzielny przez cztery być niepodzielny przez 100 
(jednak z wyjątkiem tych, podzielnych przez 400).'''

year = int(input('Podaj rok: '))

if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
    print(f'{year} jest przestepny')
else:
    print(f'{year} nie jest przestepny')