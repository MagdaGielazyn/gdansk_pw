#Napisz program, który policzy ile z każdej litery występuje w słowie “rabarbar”

slowo = 'rabarbar'
count_r = 0
count_b = 0 
count_a = 0

for x in slowo:
    if x == 'r':
        count_r +=1
    if x == 'b':
        count_b +=1
    if x == 'a':
        count_a +=1

print(f'W slowie rabarbar jest {count_r} liter r, {count_b} liter b, {count_a} liter a.')