# ############################################## NAJLEPSZY WYNIK #######################################################
# choice = None
# scores = []
#
# while choice != "0":
#     print(
#         """
#         Najlepsze wyniki
#         0 - zakończ
#         1 - pokaż wyniki
#         2 - dodaj wynik
#         3 - usuń wynik
#         4 - posortuj wyniki
#         """
#     )
#     choice = input("Wybierasz: ")
#
#     if choice == "0":
#         print("Do widzenia")
#
#     elif choice == "1":
#         for i in scores:
#             print(i)
#
#     elif choice == "2":
#         score = int(input("Wynik: "))
#         scores.append(score)
#
#
#     elif choice == "3":
#         score = int(input("Wynik do usuniecia: "))
#         if score in scores:
#             scores.remove(score)
#         else:
#             print("Nie ma takiego wyniku ")
#
#
#     elif choice == "4":
#         scores.sort(reverse=True)
#
#     else:
#         print("Wybrano zła opcje")

############################################## NAJLEPSZY WYNIK 2.0 #####################################################
# choice = None
# scores = []
#
# while choice != "0":
#     print(
#         """
#         Najlepsze wyniki
#         0 - zakończ
#         1 - pokaż wyniki
#         2 - dodaj wyniK
#         """
#     )
#     choice = input("Wybierasz: ")
#
#     if choice == "0":
#         print("Do widzenia")
#
#     elif choice == "1":
#         for entry in scores:
#             score,name = entry
#             print(score,"\t",name)
#     elif choice == "2":
#
#         score = input("Wpisz wynik:")
#         name = input("Wpisz imie:")
#         entry = score, name
#         scores.append(entry)
#         scores.sort(reverse=True)
#         scores = scores[:5]
#
#     else:
#         print("Wybrano nie prawidłową opcję")
#
############################################## Translator piłkarski ####################################################

choice = None
geek = {"spalony":"Zawodnik atakujący znajduje się za przedostatnim zawodnik drużyny przeciwnej",
        "rożny":"Piłka jest wybijana przez drużyne atakującą z rogu boiska po stronie drużyny broniącej",
        "karny": "Zawodnik atakujący wykonuje strzał bezpośrednio w polu karnym drużyny broniącej w specjalnym do tego wyznacczonym miejscu",
        "faul":"Zawodnik zatzrymał zawodnika drużyny przeciwnej w nie przepisowy sposob"}

while choice != "0":
    print(
        """
        Najlepsze wyniki
        0 - zakończ
        1 - znajdz termin
        2 - dodaj nowy termin
        3 - zmień definicje terminu
        4 - usun termin
        
        """
    )
    choice = input("Wybieram: ")
    if choice == "0":
        print("Do widzenia")

    elif choice == "1":
        term = input("Wpisz termin który chcesz odszukać: ")
        if term in geek:
            definiton = geek[term]
            print(definiton)
        else:
            print("takiej definicji nine ma w słowniku: ")

    elif choice == "2":
        term = input("Wpisz nowy termin: ")
        if term not in geek:
            definiton = input("Wpisz definicje terminu: ")
            geek[term] = definiton
        else:
            print("Taki termin już istnieje")

    elif choice == "3":
        term = input("Wpisz termin którego definicje chcesz zmienić: ")

        if term in geek:
            definiton = input("Wpisz nową definicję: ")
            geek[term] = definiton

        else:
            print("w słowniku nie ma takiej definicji")

    elif choice == "4":
        term = input("wpisz termin który chcesz usunąc")

        if term in geek:
            del geek[term]

        else:
            print("w słowniku nie ma takiego terminu")

    else:
        print("Wybrano nieznaną opcją, spróbuj ponownie")