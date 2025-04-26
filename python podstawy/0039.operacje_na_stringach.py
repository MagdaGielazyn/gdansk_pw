#• można sprawdzić czy dana litera występuje w ciągu znaków
#• ‘f’ in ‘jakas zmienna’ -> rozwiązaniem będzie bool
#Przykład:
if 'b' in 'abrakadabra':
    print('W słowie "abrakadabra" znajduje się litera "b".')
#• można porównać ciągi (np.: porządkowanie alfabetyczne)
#• ‘slowo’ > ’litera’ !!! Litery z początku alfabetu mają mniejszą
#wartość
#Przykład:
warzywo = input('Podaj warzywo: ')
if warzywo < 'cebula':
    print('Twoje warzywo będzie przed słowem cebula')
elif warzywo > 'cebula':
    print('Twoje warzywo będzie po słowie cebula')
else:
    print('Twoje warzywo to cebula')
#• można przyrównać 2 ciągi
#• ‘slowo’ == ‘slowo’
#Przykład:
warzywo = input('Podaj warzywo: ')
if warzywo == 'cebula':
    print('Tak, chodziło o cebulę!')
else:
    print('Nie, chodziło o inne warzywo')
#Istnieją jednak pewne ograniczenia:
#• Wielkie litery będą miały pierszeństwo przed małymi