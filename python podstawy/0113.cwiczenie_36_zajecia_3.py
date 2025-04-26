#Poproś użytkownika, żeby podał string oraz integer. Program powinien wydrukować podany string podaną ilość razy.
#Przykładowy output:
#Podaj string: Cześć! Podaj liczbę: 3 Cześć!
#Cześć!
#Cześć!


def wydruk(string, num):
    for x in range(num):
        print(string)

def main():
    string = input('Podaj string: ')
    num = int(input('Podaj num: '))
    wydruk(string, num)

main()