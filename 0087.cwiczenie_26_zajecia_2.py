#Napisz program, który doda pola 3 trójkątów
#Trójkąt 1: a=3
#h=5
#Oczekiwany output:
#Trójkąt 2: a=8
#h=12
#Trójkąt 3: a=7
#h=4
#Pole wszystkich trójkątów to: 69.5

def triangle(a,h):
    pole = a*h/2
    return(pole)

def main():
    triangle_1 = triangle(3,5)
    triangle_2 = triangle(8,12)
    triangle_3 = triangle(7,4)
    triangle_all = triangle_1 + triangle_2 + triangle_3
    print(f'Pole wszystkich trojkatow to {triangle_all}.')

main()

