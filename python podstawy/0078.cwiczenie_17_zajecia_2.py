#Napisz program, który pyta użytkownika o liczbę i je dodaje. Program kończy się kiedy
#użytkownik poda 0.

num = int(input('Podaj liczbe: '))
sum = num

while num !=0:
    num = int(input('Podaj liczbe: '))
    sum += num
    print(f'Suma liczba to: {sum}.')