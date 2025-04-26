#Napisz program, który przyjmie liczbę i wypisze wszystkie możliwe dzielniki tej liczby.
#Przykładowy output:
#Podaj liczbę: 8 1
#2
#4
#8



def dzielniki(num):
    for x in range(num):
        dzielnik = x+1
        if num % dzielnik == 0:
            print(dzielnik)

def main():
    num = int(input('Podaj liczbe: '))
    dzielniki(num)  

main()
