#   2. Zmodyfikuj projekt Jaka to liczba? z rozdziału 3. przez użycie w nim funkcji
#      ask_number().


import random

gues = random.randint(1, 100)
proba = 0
life = 8

def ask_number(question,low,high,step = 1):
    response = None
    while response not in range(low,high,step):
        response = int(input(question))
    return response





while True:
    number = ask_number("Podaj liczbe od 1 do 100: ",1,100)
    proba += 1
    if life == 0:
        print("Przegrałeś")
        break

    if number == gues:
        print("Udalo ci sie odgadnac liczbe za ", proba, "razem i zostało ci ", life, "zyć")
        break

    elif number > gues:
        print("ta liczba jest mniejsza")

    elif number < gues:
        print("ta liczba jest wieksza")

    life -= 1
    print("Zostało ci ", life, " zyc")