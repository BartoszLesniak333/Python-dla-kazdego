#   3. Zmodyfikuj nową wersję gry Jaka to liczba?, którą utworzyłeś w ramach
#      poprzedniego zadania, tak aby kod programu znalazł się w funkcji o nazwie
#      main(). Nie zapomnij o wywołaniu funkcji main() w celu uruchomienia gry.


#biblioteka
import random

#zmienne
gues = random.randint(1, 100)
proba = 0
life = 8

#funkcje
def ask_number(question,low,high,step = 1):
    response = None
    while response not in range(low,high,step):
        response = int(input(question))
    return response

def main(proba,life,gues):
    while True:
        number = ask_number("Podaj liczbe od 1 do 100: ", 1, 100)
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

#wywołanie funkcji głownej
main(proba,life,gues)




