#   3. Popraw program Wymieszane litery tak, żeby każdemu słowu towarzyszyła
#      podpowiedź. Gracz powinien mieć możliwość zobaczenia podpowiedzi, jeśli
#      utknie w martwym punkcie. Dodaj system punktacji, który nagradza graczy
#      rozwiązujących anagram bez uciekania się do podpowiedzi.

import random

WORDS = ("myszka","monitor","klawiatura","słuchwki")

word = random.choice(WORDS)
correct = word
tumble = ""
answer = None
podpowiedz = None

points = 10

while word:
    possition = random.randrange(len(word))
    tumble += word[possition]
    word = word[:possition]+word[possition+1:]

print(tumble)

while answer != correct and answer != "" :
    answer = input("Podaj swoją odpowiedz: ")
    if answer == correct:
        print("Dobra odpowiedz\n")
        print("Udało ci sie zdobyć ",points," punktow")

    else:
        print("ZLa odpowiedz\n")
        print("Jeżeli chcesz zobaczyć podpowiedz wciśnij: \n")
        print("1 - Pierwsza litera wyrazu\n ")
        print("2 - Dwie pierwsza litery wyrazu \n")
        print("3 - Trzy pierwsza litery wyrazu \n")
        print("4 - Wszystkie litery wyrazu \n")

    podpowiedz = int(input("Wybieram: "))

    if podpowiedz == 1:
        print(correct[0:1])
        points -= 1

    elif podpowiedz == 2:
        print(correct[0:2])
        points -= 2

    elif podpowiedz == 3:
        print(correct[0:3])
        points -= 3

    elif podpowiedz == 4:
        print(correct[:])
        points -= 4

    else:
        print("Nie wybrałes odpowiedzi sprobuj odgadnac wyraz jeszcze raz")

    if points <= 0:
        print("\nNiestety przegrałeś")
        break
