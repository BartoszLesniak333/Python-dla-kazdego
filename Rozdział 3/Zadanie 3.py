#   3. Zmodyfikuj program Jaka to liczba? tak, aby gracz dysponował ograniczoną
#      liczbą prób odgadnięcia wybranej przez komputer liczby. Gdy graczowi nie uda
#      się odgadnąć tej liczby w wyznaczonej liczbie prób, program powinien
#      wyświetlić odpowiedni komunikat z reprymendą.

import random

gues = random.randint(1,100)
proba = 0
life = 8

while True:
    number = int(input("Podaj liczbe od 1 do 100: "))
    proba += 1
    if life == 0:
        print("Przegrałeś")
        break
        
    if number == gues:
        print("Udalo ci sie odgadnac liczbe za ",proba, "razem i zostało ci ",life,"zyć")
        break

    elif number > gues:
        print("ta liczba jest mniejsza")

    elif number < gues:
        print("ta liczba jest wieksza")

    life -= 1
    print("Zostało ci ",life," zyc")