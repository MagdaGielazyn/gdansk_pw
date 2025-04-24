def wydruk():
    print('Madzia')
    print('Marcin\n')

def podwojny_wydruk():
    wydruk()
    wydruk()

podwojny_wydruk()


def ocena():
    procent = int(input('jaki procent'))
    if procent > 50:
        print('zdales')
    elif procent <50:
        print('nie zdales')


def main():
    studenci = 30
    for kazdy in range(1, studenci+1):
        ocena()

main()