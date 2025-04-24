#2. Napisz program, który rozwiąże w jakim wieku są osoby
#Maciek ma 21 lat
#Ula jest 6 lat starsza niż Maciek
#Czarek jest 20 lat starszy niż Ula
#Antek ma tyle lat co Czarek i Maciek razem
#Kasia ma tyle samo lat co Czarek
#Program powinien wydrukować wiek każdej osoby w oddzielnej linii

age_maciej = 21
age_ula = age_maciej + 6
age_czarek = age_ula + 20
age_antek = age_maciej + age_czarek
age_kasia = age_czarek

print(f'Maciej ma {age_maciej} lat.')
print(f'Ula ma {age_ula} lat.')
print(f'Czarek ma {age_czarek} lat.')
print(f'Antek ma {age_antek} lat.')
print(f'Kasia ma {age_kasia} lat.')