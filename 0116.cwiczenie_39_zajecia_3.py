#Napisz program, który powie Ci czy liczba, którą podał użytkownik jest parzysta czy nieparzysta
#Przykładowy output:
#Podaj liczbę: 43
#43 o liczba nieparzysta

def parzystosc(num):
    if num % 2 == 0:
        return True

def main():
    num = int(input('Podaj liczbe: '))
    if parzystosc(num):
        print(f'Liczba {num} jest parzysta.')
    else:
        print(f'Liczba {num} jest nieparzysta.')

main()