#Zapytaj użytkownika o słowo, następnie jaka to część mowy (rzeczownik, czasownik, przymiotnik)
#Jeśli część mowy to 0, zakładamy że słowo to rzeczownik, zdanie brzmi “Super! Od dawna chciałam dodać _____ do mojej kolekcji”
#Jeśli część mowy to 1, zakładamy że słowo to czasownik, zdanie brzmi: “Jest taka piękna pogoda, że aż się chce _____”
#Jeśli część mowy to 2, zakładamy że słowo to przymiotnik, zdanie brzmi: “Patrząc za okno, niebo jest wielkie I ______”
#Weź pod uwagę przypadek, kiedy słowo podane przez użytkownika nie jest ani rzeczownikiem, ani czasownikiem, ani przymiotnikiem
#Przykładowy output:
#Podaj słowo: kamień
#Jaka to część mowy? (0 – rzeczownik, 1 – czasownik, 2 – przymiotnik): 0 Super! Od dawna chciałam dodać kamień do mojej kolekcji

def czesci_mowy(slowo, czesc_mowy):
    if czesc_mowy == 0:
        print(f'Super! Od dawna chciałam dodać {slowo} do mojej kolekcji.')
    elif czesc_mowy == 1:
        print(f'Jest taka piękna pogoda, że aż się chce {slowo}.')
    elif czesc_mowy == 2:
        print(f'Patrząc za okno, niebo jest wielkie i {slowo}.')
    else:
        print('To nie jest ani rzeczownik ani czasownik ani przymiotnik.')

def main():
    slowo = input('Podaj slowo: ')
    czesc_mowy = int(input('Jaka to czesc mowy? (rzeczownik - 0, czasownik - 1, przymiotnik - 2)')) 
    czesci_mowy(slowo, czesc_mowy)

main()

