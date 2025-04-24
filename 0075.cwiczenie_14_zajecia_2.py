#Napisz program, który zasymuluje rzut dociążoną monetą. Szansa na wylosowanie orła: 70%

import random
rzut = random.random()

ORZEL = 0.7

if rzut < ORZEL:
    print('Orzel')
else:
    print('Reszka')
