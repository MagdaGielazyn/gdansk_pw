#Funkcja print drukuje tekst w terminalu.
#Można użyć kilku komend print, żeby wydrukować kilka linii tekstu:
#print(„jeden”) print(“jeden”, “dwa”, “trzy”)
#print(„dwa”)
#print(„trzy”)
#…
#…
#print(„n”)
#Mozna uzyc kilku wersji printa:

liczba_rzeczywista = 17.3
liczba_calkowita = 580
tekst = 'chomik'

print(tekst + ' ma ' + str(liczba_rzeczywista) + ' lat i wazy ' + str(liczba_calkowita) + ' gram.') #1
print(tekst+' ma '+str(liczba_rzeczywista)+' lat i wazy '+str(liczba_calkowita)+' gram.') #2
print(tekst, 'ma', liczba_rzeczywista, 'lat i wazy', liczba_calkowita, 'gram.') #3
print(tekst,'ma',liczba_rzeczywista,'lat i wazy',liczba_calkowita,'gram.') #4
print(f'{tekst} ma {liczba_rzeczywista} lat i wazy {liczba_calkowita} gram.') #5
print(f"{tekst} ma {liczba_rzeczywista} lat i wazy {liczba_calkowita} gram.") #6