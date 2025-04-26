#Napisz program, który przyjmuje integer i drukuje jego cyfrę jedności 748
#Przykładowy output: Podaj liczbę: 748 Cyfra jedności to 8

def jednosci(num):
    cyfra = num % 10
    print(f'Cyfra jednosci to: {cyfra}.')

def main():
    num = int(input('Podaj liczbe calkowita: '))
    jednosci(num)

main()