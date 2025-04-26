# Napisz program, który poprosi użytkownika o 5 słów i
#  powie mu które z nich jest najdłuższe oraz ile ma liter

lenght = 0

for x in range(5):
    word = input('Podaj slowo: ')
    new_lenght = len(word)
    if new_lenght > lenght:
        longest_word = word

print(f'Najduzsze slowo to {longest_word}, a jego dlugosc to {new_lenght}.')