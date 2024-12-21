#   2. Napisz program Kreator postaci do gry z podziałem na role. Gracz powinien
#      otrzymać pulę 30 punktów, którą może spożytkować na cztery atrybuty: siła,
#      zdrowie, mądrość i zręczność. Gracz powinien mieć możliwość przeznaczania
#      punktów z puli na dowolny atrybut, jak również możliwość odbierania
#      punktów przypisanych do atrybutu i przekazywania ich z powrotem do puli

points = 30

atributs = {"Siła"      : 0,
            "Zdrowie"   : 0,
            "Mądrość"   : 0,
            "Zręczność" : 0}

choice = None

while choice != "0":
    print("0 - Zakończ"
          "\n1 - Przydziel punkty"
          "\n2 - odejmij punkty"
          "\n3 - Wyświetl atrybuty"
          "\nPosiadasz: ",points," punktów")

    choice = input("\nWybieram: ")

    if choice == "1":
        enter = int(input("Ilość punktów do przeznaczenia: "))
        if enter > points or enter <= 0:
            print("Nie możesz przeznaczyć takiej ilości puntków")

        else:
            points -= enter
            print("Gdzie chcesz przeznaczyć punkty?\n ")
            print(atributs)
            term = input("Wybieram atrybut: ")

            if term in atributs:
                atributs[term] = enter
                print("\n",atributs,"\n")
            else:
                print("Nie posiadasz takiego atrybutu!")

    if choice == "2":
        print("Z jakiego atrybuty chcesz zabrać punkty?\n")
        print(atributs)

        term = input("Wybieram atrybut: ")
        if atributs[term] == 0:
            print("Posiadasz zerową wartość w tym atrybucie nie możesz nic zabrac!!!")
        else:
            if term in atributs:
                enter = int(input("Ilość punktów chcesz zabrać: "))

                if enter < atributs[term] and enter > 0:
                        atributs[term] -= enter
                        points += enter
                        print(atributs)
                else:
                        print("Nie możesz zabrać takiej ilości punktów")
    if choice == "3":
        print(atributs)

