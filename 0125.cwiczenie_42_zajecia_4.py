#Napisz program, który przeczyta zawartość pliku linijka po linijce in wydrukuje treść w taki sam sposób.

madziulek = open('madziulek.txt', 'r')
zawartosc = madziulek.readlines()
for linia in zawartosc:
    print(linia)
madziulek.close()


