#można zastosować ciągi znaków zarówno w pętli while I for
#• wiele obliczeń polega na przetwarzaniu sekwencji znak po znaku
#Przykłady:
#Pętla while pętla for
zmienna='kot' 
indeks = 0
while indeks < len(zmienna): 
    litera = zmienna[indeks]
    print(litera)
    indeks += 1

#pętla for
zmienna='kot'
for litera in zmienna:
    print(litera)
  