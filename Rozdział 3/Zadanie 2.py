#  2. Napisz program, który „rzuca” 100 razy monetą, a następnie podaje
#     użytkownikowi liczbę orzełków i reszek.

import random

count = 0
orzel = 0
reszka = 0

while count < 100:
    count += 1
    money = random.randint(1, 2)
    if money == 1 :
        orzel +=1

    else:
        reszka +=1

print("Orzeł: ",orzel,"\nReszka", reszka)