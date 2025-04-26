#Poproś użytkownika o podanie liczby, następnie napisz program, który policzy od 1 do tej liczby
#oraz wypisze je. Jeśli liczba jest podzielna przez 3 zastąp ją tekstem “Fizz”, jeśli jest podzielna
#przez 5 – zastąp ją napisem “Buzz”, natomiast jeśli jest podzielna przez 3 i 5 zastąp ją tekstem
#“FizzBuzz”. Na koniec podlicz numer “Fizz”, “Buzz” i “FizzBuzz” 
#Oczekiwany output:
#1
#2
#Fizz
#4
#Buzz

num = int(input('Podaj liczbe: '))
count_fizz = 0
count_buzz = 0
count_fizzbuzz = 0

for x in range (1, num+1):
     if x % 5 == 0 and x % 3 == 0:
        count_fizzbuzz +=1
        print('FizzBuzz')
     elif x % 5 == 0:
        count_buzz +=1
        print('Buzz') 
     elif x % 3 == 0:
        count_fizz +=1
        print('Fizz')
     else:
         print(x)

print(f'Liczba wszystich Fizz to {count_fizz}, liczba wszystkich Buzz to {count_buzz}, a liczba wszytskich FizzBuzz to {count_fizzbuzz}.') 