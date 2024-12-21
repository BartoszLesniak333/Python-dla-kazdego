#   4. Udoskonal program Kto jest moim tatą? poprzez dodanie opcji, która umożliwi
#      użytkownikowi wprowadzenie imienia i (lub) nazwiska jakiejś osoby i uzyskanie
#      odpowiedzi, kto jest jej dziadkiem. Twój program powinien nadal wykorzystywać
#      tylko jeden słownik par syn-ojciec. Pamiętaj, aby włączyć do swojego słownika
#      kilka pokoleń, tak aby możliwe było tego rodzaju dopasowanie.

family = {"Michael Douglas": ["Kirk Douglas","Mark Douglas"],
            "Jaden Smith": ["Will Smith","Grandfather Smith"],
            "Kiefer Sutherland": ["Donald Sutherland","Grandfather Sutherland "],
            "Peter Fonda": ["Henry Fonda","Grandfather Fond"],
            "Brooklyn Beckham": ["David Beckham"]}

choice = None

while choice != "0":
    print("0 - Zakończ\n"
          "1 - Wyświetl synów \n"
          "2 - Podaj syna u którego chcesz pozanać ojca\n"
          "3 - Dodaj pare syn \ ojciec\n"
          "4 - Wymień pare syn \ ojciec\n"
          "5 - Usuń pare syn \ ojciec\n"
          "6 - Znajdz dziadka syna")
    choice = input("Wybieram: ")

    if choice == "0":
        print("Do zobaczenia! ")

    elif choice == "1":
        for i in family:
            print(i)
        print("\n")

    elif choice =="2":
        name = input("Imie i  nazwisko syna: ")
        if name in family:
            print("Imie ojca to: ",family[name][0],"\n")
        else:
            print("Nie ma takiego syna w bazie\n ")

    elif choice == "3":
        son = input("Podaj imie syna: ")
        father = input("Podaj imie ojca: ")
        family[son][0] = father
        print("\n")

    elif choice == "4":
        son_1 = input("Jakiego syna chesz wymienić: ")
        if son_1 in family:
            print("\nDodajemy nową pare")
            son = input("imie nowego syna: ")
            father = input("Imie jego ojca: ")
            family[son][0] = father
            del family[son_1]
        else:
            print("Nie ma takiego syna")

    elif choice == "5":
        son = input("Jakiego syna chesz usunąć?: ")
        if son in family:
            del family[son]
        else:
            print("Nie ma takiego syna\n")

    elif choice== "6":
        son = input("Imie syna: ")
        if son in family:
            if len(family[son])>1:
                print("Imie dziadka to: ",family[son][1],"\n")
            else:
                print("Nie ma dziadka\n")

    else:
        print("wybrano złą opcję")