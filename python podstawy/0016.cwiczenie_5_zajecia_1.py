# 5. Poproś użytkownika o wprowadzenie długości każdego z boków trójkąta, a następnie wydrukuj
#wartość obwodu
#Przykładowy output:
#Jaka jest długość pierwszego boku? 1
#Jaka jest długość drugiego boku? 2
#Jaka jest długość trzeciego boku? 3
#Odwód trójkąta to 6!

side_a = float(input('Jaka jest dlugosc pierwszego boku trojkata?'))
side_b = float(input('Jaka jest dlugosc pierwszego boku trojkata?'))
side_c = float(input('Jaka jest dlugosc pierwszego boku trojkata?'))
perimeter = side_a + side_b + side_c

print(f'Obwod trojkata to {perimeter}.')