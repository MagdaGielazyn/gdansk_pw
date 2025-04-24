#Poproś użytkownika o podanie liczby i napisz program, który doda wszystkie liczby od 1 do
#podanej (np.: 5 to 1+2+3+4+5)
#Przykładowy output:
#Podaj liczbę: 5
#Suma to 15


num = int(input(f'Podaj liczbe: '))
sum = 0

for x in range(1, num+1):
    sum +=x

print(f'Suma to {sum}.')