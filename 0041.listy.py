#• listy są kolejnym przykładem sekwencji
#Przykłady list:
#[7, 8, 4, 67]
#[‘jakas’, ‘sobie’, ‘lista’]
#[‘lista’, 7, 8.4, [9, 78]] <- lista zagnieżdżona
#[] <- pusta lista
#• listy można przypisać do zmiennych
#UWAGA!! W przeciwieństwie do ciągu znaków listy są zmienne
#• tak samo jak przy stringach, indeksy liczymy od 0
#• można podmieniać pojedyncze elementy list

#Przykład:
num_list = [8, 56, 73, 79]
num_list[2] = 23
#• indeksy działają tak samo jak przy stringach
#• najczęstszą metodą poruszania się po listach jest pętla for
#• można odczytać kolejno każdy element listy
#Przykład:
for element in num_list:
    print(element)