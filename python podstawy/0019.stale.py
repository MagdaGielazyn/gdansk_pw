PI = 3.14
INCH_TO_CM = 2.54

#Stałe pozwalają na zachowanie “czystości” kodu (są dobrze czytelne)
#Opisowe nazwy, w formacie UPPER_SNAKE_CASE
#Podobieństwo do zmiennych; nie zmieniają wartości podczas egzekucji kodu
#Definiujemy stałe w sposób ogólny, żeby wciąż działały w przypadku, gdy zmienimy wartość
#stałej
#Przykład:
INCH_TO_CM = 2.54
inch = float(input('Podaj liczbę cali'))
cm = inch * INCH_TO_CM
print(inch, 'cali to', cm, 'centymetrów')