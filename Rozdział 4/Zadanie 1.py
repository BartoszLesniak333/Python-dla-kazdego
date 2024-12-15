#    1. Napisz program, który liczy za użytkownika. Umożliw użytkownikowi
#       wprowadzenie liczby początkowej, liczby końcowej i wielkości odstępu między
#       kolejnymi liczbami.

start = int(input("podaj liczbe początkową: "))
end = int(input("podaj liczbe początkową: "))
odstep = int(input("podaj odstep pomiedzy liczbami: "))

for i in range(start,end,odstep):
    print(i)
