#Napisz program, który przyjmie liczbę i zwróci jej dwukrotność
#Przykładowy output:
#Podaj liczbę: 8 Dwukrotność 8 to 16


def dwukrotnosc(num):
    return num*2

def main():
    num = int(input('Podaj liczbe: '))
    num_2 = dwukrotnosc(num)
    print(f'Dwukrotnosc {num} to {num_2}.')

main()
