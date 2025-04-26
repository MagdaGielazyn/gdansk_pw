#zamień krotki:
#krotka1 = (0, 45, 67) krotka2 = (99, 65, 32)
#Oczekiwany output: krotka1: (99, 65, 32) krotka2: (0, 45, 67)

krotka1 = (0, 45, 67) 
krotka2 = (99, 65, 32)
krotka1, krotka2 = krotka2, krotka1

print(f'Krotka1: {krotka1}, krotka2: {krotka2}.')