#Waga Ziemianina na Marsie wynosi 37,8% ich wagi na Ziemi. Napisz program, który prosi
#Ziemianina o podanie swojej wagi na Ziemi i wyświetla obliczoną wagę na Marsie.
#Przykladowy output:
#Podaj wage na Ziemi: 120
#Ekwiwalent na Marsie: 45.36

MARS = 0.378

weight_e = float(input('Podaj wage na Ziemi:'))
weight_m = weight_e * MARS

print(f'Ekwiwalent na Marsie to {weight_m}.')