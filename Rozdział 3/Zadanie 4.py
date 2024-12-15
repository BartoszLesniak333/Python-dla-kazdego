#   4. Tym razem trudniejsze wyzwanie. Napisz pseudokod do programu, w którym
#      gracz i komputer zamienią się rolami w grze z odgadywaniem liczby. To znaczy
#      gracz wybiera losowo liczbę z przedziału od 1 do 100, a komputer ma ją
#      odgadnąć. Zanim rozpoczniesz tworzenie algorytmu, pomyśl, w jaki sposób
#      sam byś zgadywał. Jeśli wszystko się uda, spróbuj napisać kod gry.

##################################################### PSEUDOKOD #####################################################
# podaj lososwa liczbe do odgadniecia
# zaimplementuj probe, zakres dolny i zakres gorny losowanych liczb przez komputer
# funkcja while
# komputer wybiera losowa liczbe od zakresu dolnego do zakresu gornego
# logika wypisywania wiadomoci
# zmienne wieksza lub mnijesza sprwdzajce podpowiedz
# jezeli liczba mniejsza to zmieniamy zakres gorny o number - 1
# jezeli liczba wieksza to zmieniamy zakres dolny o number + 1
# komputer wybiera losowa liczbe od zakresu dolnego do zakresu gornego
# z kazdym wykonaniem funkcji programu proba o jeden wieksza

import random

gues =  int(input("Podaj liczbe od 1 do 100: "))
proba = 0
gorny = 1000
dolny = 1


while True:
    number = random.randint(dolny, gorny)
    proba += 1
    if number == gues:
        print("Brawo odgadles za",proba)
        break

    elif number > gues:
        print("ta liczba jest mniejsza od ", number)
        gorny = number - 1


    elif number < gues:
        print("ta liczba jest wieksza od ", number)
        dolny = number + 1




