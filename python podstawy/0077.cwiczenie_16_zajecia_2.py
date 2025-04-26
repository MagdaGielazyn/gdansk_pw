#Napisz program, który wypisze ciąg Fibbonacciego do określonego limitu (np.: 1000)

LIMIT = 1000

fib1 = 0
fib2 = 1

while fib1 <= LIMIT:
    print(fib2)
    fib_next = fib1 + fib2
    fib1 = fib2
    fib2 = fib_next

t