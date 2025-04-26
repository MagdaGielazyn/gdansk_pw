#Jeżeli liczba wartości w krotce przewyższa liczbę zmiennych, można użyć znaku *
#• Może wystąpić tylko jeden asterisk na wyrażenie!!!
#Przykład:
warzywa = ('marchew', 'pomidor', 'cebula', 'pietruszka', 'kalafior')
(pomaranczowy, czerwony, *bialy) = warzywa
print(pomaranczowy) #wynik: marchew
print(czerwony) #wynik: pomidor
print(bialy) #wynik: [‘cebula’, ‘pietruszka’, ‘kalafior’]