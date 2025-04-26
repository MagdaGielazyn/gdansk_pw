#W Pythonie można zdefiniować własne, dowolne funkcje
#def nazwa_funkcji(): UWAGA!! Dwukropek
#zawartość
#zawartość W przypadku funkcji bez argumentów nawias
#zawartość powinien być pusty
#Takie funkcje mogą zwracać jakąś wartość/wynik lub nie (funkcja pusta)
#Przykład:
#nazwy funkcji:
#nazwa funkcji może być dowolnym słowem
#• lub ciągiem słów w formacie snake_case (słowa połączone podkreślnikiem)
#• tak jak przy zmiennych, nazwa funkcji może zawierać litery, cyfry oraz niektóre znaki
#interpunkcyjne
#• nazwa nie może zaczynać się od cyfry
#• nie można używać słowo kluczowego jako nazwy funkcji
#• nie powinno się używać tej samej nazwy funkcji i zmiennej
#Żeby funkcja zadziałała należy ją wywołać
#Funkcje zdefiniowane samodzielnie, wywołujemy w taki sam sposób, co funkcje wbudowane
#Przykład dla funkcji bez argumentów:
def wydruk():
    print('Jest super…')
    print('…albo i nie')
#Niektóre funkcje wymagają jednak argumentów (np.: type(zmienna)
#Przykład dla funkcji z argumentami:
def dodawanie(x,y):
    suma = x+y
    return suma

def main():
    total = dodawanie(4,5)
    print(total)

wydruk()
main()

#control flow:
#W programowaniu ważna jest kolejność wykonywania instrukcji.
#Na początku powiedziano, że instrukcje są wykonywane linijka po linijce.
#Ale…
#Zostały wprowadzone elementy, które powodują obejście niektórych linii lub ich powielanie (if,
#while, for)
#Odnosi się to również do funkcji.
#Dlatego też należy znać zasady kontroli sterownia i upewnić się, że instrukcje wykonywane są w
#odpowiedniej kolejności.
