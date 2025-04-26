import numpy as np
#tablica jednowymiarowa
tablica_int = np.array([1, 2, 5, 3, 7], dtype=int)
tablica_float = np.array([1, 4.5, 3, 2])
tablica_str = np.array(['dog', '3', 'rower', '3.5'])
tablica_bool = np.array([True, False, True, True], dtype=bool)
#tablica wielowymiarowa
tablica2d = np.array([[1, 2, 8],[5, 3, 7]]) #tablica2d = np.array([[1, 2, 8],
# [5, 3, 7]])

wymiar_tablicy = tablica_int.ndim
rozmiar_tablicy = tablica_int.shape

print(tablica_int)
print(tablica_float)
print(tablica_str)
print(tablica_bool)
print(tablica2d)
print(wymiar_tablicy)
print(rozmiar_tablicy)


# tablica z wartościami z danego zakresu z krokiem #(początek zakresu, koniec zakresu, krok) tablica_zakres = np.arange(10)
tablica_zakres_krok = np.arange(1, 10, 2)
# tablica z konkretną ilością wartości
# (początek zakresu, koniec zakresu, ilość punktów) 
tablica_ilosc = np.linspace(0, 10, 8)
# reshaping
# (ilość wierszy, ilość kolumn) 
zmiana_wymiaru = tablica_ilosc.reshape(4, -1)
# flattening
wyplaszczanie_tablicy = tablica2d.reshape(-1)

print(tablica_zakres_krok)
print(tablica_ilosc)
print(zmiana_wymiaru)
print(wyplaszczanie_tablicy)

# tablica zer
zera = np.zeros(8)
zera2d = np.zeros((5, 4), dtype=int)
# tablica jedynek
jedynki = np.ones(8) 
jedynki2d = np.ones((4, 3))
# jedynki na przekątnej
przekatna = np.eye(8)

print(zera)
print(zera2d)
print(jedynki)
print(jedynki2d)
print(przekatna)

tabelka= np.array([[[1,2,3],[4,5,6],[7,8,9]],
                  [[10,11,12],[13,14,15],[16,17,18]],
                  [[19,20,21],[22,23,24],[25,26,27]]])

srodkowy_obiekt_3_wymiaru = tabelka[2, 1, 1]
trzeci_rzad_1_wymiaru = tabelka[0,-1]
druga_kolumna_2_wymiaru =  tabelka[1,:,1]
trzeci_wymiar = tabelka[2]

print(tabelka)
print(srodkowy_obiekt_3_wymiaru)
print(trzeci_rzad_1_wymiaru)
print(druga_kolumna_2_wymiaru)
print(trzeci_wymiar)
tab_1 = np.array([[3, 5, 7, 2], [4, 2, 7, 1]])
tab_2 = np.array([[4, 2, 6, 7], [3, 2, 1, 8]])
tab_3 = np.array([2, 1, 3, 4]) 
tab_4 = np.array([2, 1])

# dodawanie/odejmowanie wartości do wszysktich elementów
plus1 = tab_1 + 1 
minus3 = tab_2 - 3
# suma wartości tablic
suma = tab_1 + tab_2
inna_suma = np.add(tab_1, tab_3)
tab_1[0] += tab_3 
tab_2[:, 0] += tab_4
# suma wszystkich wartości w tablicy
total = tab_1.sum()

print(plus1)
print(minus3)
print(suma)
print(inna_suma)
print(tab_3)
print(tab_4)
print(total)


tablica2d = ([[3, 5, 2], [5, 2, 7]])
# dostęp do elementów tablicy
for element in tablica2d: 
    print(element)
#dostęp do poszczególnych wartości tablicy
print('przerwa')
for element in tablica2d: 
    for wartosc in element:
        print(wartosc)

for wartosc in np.nditer(tablica2d): print(wartosc)

# szukanie wartości
tab_1 = np.array([[3, 5, 7, 2], [4, 2, 7, 1]])
print(tab_1)
szukaj = np.where(tab_1 == 5)
print(tab_1==2)

szukaj_parzyste = np.where(tab_1%2 == 0)
print(szukaj)
print(szukaj_parzyste)


# łączenie tablic
tablica_lacz = np.concatenate((tab_1, tab_2))
print(tablica_lacz)
# rozdzielanie
tab_1 = np.array([[3, 5, 7, 2], [4, 2, 7, 1]])
tablica_dziel = np.array_split(tab_1, 4, axis=1) 
print(tablica_dziel[0], tablica_dziel[1]) 
czesc1, czesc2, czesc3, czesc4 = tablica_dziel


#filtrowanie
tab_3 = np.array([2, 1, 3, 4]) 
filtr = [True, False, False, True] 
nowa_tab = tab_3[filtr]
print(nowa_tab)

#tworzenie filtra dynamicznego
#filtr = []
#for element in tab_1: 
#    if element>5:
#        filtr.append(True) 
#    else:
#        filtr.append(False)
#print(tab_1)

#maskowanie danych

tablica = np.arange(1,20,2).reshape(2, 5)
maska = tablica>10
zamaskowane = np.ma.masked_where(maska, tablica)
maska2 = np.array([[False, True, False, False, True],[True, True, True, False, True]]) 
zamaskowane2 = np.ma.masked_array(tablica, maska2)

print(tablica)

#Maski stosuje się:
#• kiedy chcemy zachować oryginalne dane, ale nie chcemy kopiować tablicy
#• W przypadku, gdy pracujemy na wielu tablicach, żeby uniknąć bugów I skompresować
#kod
#• Gdy dane są brakujące lub nieprawidłowe
#• Nie możemy uniknąć operacji na błędnych danych, ale nie chcemy radzić sobie z
#obiektami typu NaN
#Zapisywanie i wczytywanie plików
#np.savetxt('plik_testowy.csv', tablica, delimiter=',’) np.load('plik_testowy.csv')
'''Reprezentacja nieznanych wartości
NaN (Not a Number) – zmiennoprzecinkowe wartości, reprezentujące niezdefiniowane wartości lub wartości, których Python nie jest w stanie rozpoznać
• NaN często reprezentuje brakujące lub błędne dane
• NaN nie mają specyficznej wartości
• Operacje zawierające NaN dają rezultat NaN
None – stała, która sygnalizuje brak wartości
• Używana jako placeholder, jeżeli wartość nie jest podana
• Używana, żeby zasygnalizować brak wartości zwotnej w funkcjach
• Ma swój własny typ: NoneType
N/A lub NA (Not Available) – reprezentuje brakujące, niedostępne lub wartości, których nie można zastosować
• Pliki CSV, Excela, bazy danych mogą zwrócić wartości NA
• Niektóre obiekty w Pythonie traktują NA I NaN naprzemiennie
• Głównie traktowany jako string
Operatory bitowe
& AND 
| OR
~
• • • •
NOT
Operatowy działające na bitach
Pozwalają na operacje w oparciu o element, zamiast o wartości skalarne Używane w logice Pandas i NumPy
Mają większy priorytet niż “and”, “or” i “not”
'''