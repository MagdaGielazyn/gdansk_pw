#Będziemy liczyć do 10, chyba że po drodze nam się odechce
#Napisz funkcję, która wydrukuje liczby od 1 do 10 oraz fukncję, która zadecyduje czy chce jej się to liczyć.
#Prawdopodobieństwo wydruku każdej z kolejnych liczb to 30%.
#Na końcu zawsze musi wyskoczyć napis: “No to tyle”
#Przykladowy output:
#Będę liczyć do 10, chyba że mi się odechce. 1
#2
#No to tyle

import random
PRAWDOPODOBIENSTWO = 0.3

def liczenie():
    for x in range(10):
        liczba = x+1
        if decyzja():
            return
        print(liczba)

def decyzja():
    if random.random() < PRAWDOPODOBIENSTWO:
        return True
    return False

def main():
    print('Będziemy liczyć do 10, chyba że po drodze nam się odechce')
    liczenie()
    print('No to tyle.')

main()