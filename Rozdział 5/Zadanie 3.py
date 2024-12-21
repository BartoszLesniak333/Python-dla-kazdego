#   3. Napisz program Kto jest twoim tatą?, który umożliwia użytkownikowi
#      wprowadzenie imienia i nazwiska osoby płci męskiej i przedstawia imię
#      i nazwisko jej ojca. (Możesz dla zabawy wykorzystać nazwiska celebrytów,
#      osób fikcyjnych lub nawet postaci historycznych). Umożliw użytkownikowi
#      dodawanie, wymianę i usuwanie par syn-ojciec.


family = {"Michael Douglas": "Kirk Douglas",
            "Jaden Smith": "Will Smith",
            "Kiefer Sutherland": "Donald Sutherland",
            "Peter Fonda": "Henry Fonda",
            "Brooklyn Beckham": "David Beckham"}

choice = None

while choice != "0":
    print("0 - Zakończ\n"
          "1 - Wyświetl synów \n"
          "2 - Podaj syna u którego chcesz pozanać ojca\n"
          "3 - Dodaj pare syn \ ojciec\n"
          "4 - Wymień pare syn \ ojciec\n"
          "5 - Usuń pare syn \ ojciec\n")
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
            print("Imie ojca to: ",family[name],"\n")
        else:
            print("Nie ma takiego syna w bazie\n ")

    elif choice == "3":
        son = input("Podaj imie syna: ")
        father = input("Podaj imie ojca: ")
        family[son] = father
        print("\n")

    elif choice == "4":
        son_1 = input("Jakiego syna chesz wymienić: ")
        if son_1 in family:
            print("\nDodajemy nową pare")
            son = input("imie nowego syna: ")
            father = input("Imie jego ojca: ")
            family[son] = father
            del family[son_1]
        else:
            print("Nie ma takiego syna")

    elif choice == "5":
        son = input("Jakiego syna chesz usunąć?: ")
        if son in family:
            del family[son]
        else:
            print("Nie ma takiego syna")

    else:
        print("wybrano złą opcję")