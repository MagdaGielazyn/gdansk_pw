#if warunek: <- uwaga na dwukropek
#komenda UWAGA!! Zwróćcie uwagę na wcięcie
#warunek musi być typu boolean (True/False)
#warunek musi być prawdziwy, żeby została wykonana komenda
#Przykład:
x = 7
y = 5
if x>y:
    print('x jest większe od y')

#if-else
#if warunek: <- uwaga na dwukropek
#komenda
#else: <- uwaga na dwukropek
#inna komenda
#Przykład:
x = 7
y = 9
if x>y:
    print('x jest większe od y')
else:
    print('x nie jest większe od y')

#if-elif
#Przykład:
#if warunek: if x==5:
#komenda print(‘to jest cyfra 5')
#elif inny_warunek: elif x==3:
#inna_komenda print (‘to jest cyfra 3')
#elif jeszcze_inny_warunek: elif x==9:
#następna_komenda print (‘to jest cyfra 9')


#if-elif-else
#Przykład:
#if warunek: if x < y:
#komenda print ('x jest mniejsza niż y')
#elif inny_warunek: elif x > y:
#inna_komenda print ('x jest większa niż y')
#else: else:
#następna_komenda print ('x i y są równe ')

#warunki zagnieżdżone
#Przykład:
#if warunek: if x == y:
#komenda print ('x i y sa równe ‘)
#else: else:
#if inny_warunek if x < y:
#inna_komenda print ('x jest mniejsza niż y’)
#else: else:
#następna_komenda print ('x jest większa niż y')