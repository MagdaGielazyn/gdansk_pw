#Użytkownik powinien wprowadzić temperaturę w stopniach Celsjusza, a program powinien mu
#powiedzieć jaka to temperaturę w stopniach Farenheita.
#Wzór na konwersję:
#F=C*9/5+32
#Przykładowy output:
#Podaj temperaturę [st. C]: 20
#20 stopni Celsjusza to 68 stopni Farenheita

temp_c = int(input('Podaj temperature w st. C: '))
temp_f = int(temp_c * 9 / 5 +32)

print(f'{temp_c} stopni Celsjusza to {temp_f} stopni Farenheita.')