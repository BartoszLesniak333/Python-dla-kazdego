# def instruction():
#     """Wyświetl instrukcję gry."""
#     print("""
#                 Witaj w największym intelektualnym wyzwaniu wszech czasów, jakim jest
#                  gra 'Kółko i krzyżyk'. Będzie to ostateczna rozgrywka między Twoim
#                  ludzkim mózgiem a moim krzemowym procesorem.
#                  Swoje posunięcie wskażesz poprzez wprowadzenie liczby z zakresu 0 - 8.
#                  Liczba ta odpowiada pozycji na planszy zgodnie z poniższym schematem:
#                                                  0 | 1 | 2
#                                                  ---------
#                                                  3 | 4 | 5
#                                                  ---------
#                                                  6 | 7 | 8
#                  Przygotuj się, Człowieku. Ostateczna batalia niebawem się rozpocznie. \n
#     """)
#
# print("Oto instruckja programu: ")
# instruction()


# #Function
# def display(mes):
#     print(mes)
#
# def give_me_five():
#     five = 5
#     return five
#
# def ask_yes_or_no(question):
#     """Zadaj pytanie, na które można odpowiedzieć tak lub nie."""
#     response = None
#     while response not in ("y","n"):
#         response = input(question).lower()
#     return response

# #Main
# display("Ta wiadomośc jest dla ciebie ")
#
# number = give_me_five()
#
# print("Oto liczba która dla ciebie wyświetle: ", number)
#
# ask_yes_or_no("Czy zgadzasz sie ze piłka nożna traci na zainteresowaniu [y/n]")
# def birthday_1(name,age):
#     print("Szczęsliwych uroddzin, ",name," Masz już ",age," lat")
#     return name,age
#
# def birthday_2(name="Wojo",age=6):
#     print("Szczęsliwych uroddzin, ",name," Masz już ",age," lat")
#     return name,age
# birthday_1("Katarzyna",7)
# birthday_2(age=8)

def read_global():
    print("Wartość zmiennej value odczytana wewnątrz zakresu lokalnego",
          "\nfunkcji read_global() wynosi:", value)

def shadow_global():
    value = -10
    print("Wartość zmiennej value odczytana wewnątrz zakresu lokalnego",
    "\nfunkcji shadow_global() wynosi:", value)

def change_global():
    global value
    value = -10
    print("Wartość zmiennej value odczytana wewnątrz zakresu lokalnego",
          "\nfunkcji change_global() wynosi:", value)



value = 10
print("W zakresie globalnym wartość zmiennej value została ustawiona na:", value, "\n")

read_global()
print("Po powrocie do zakresu globalnego wartość zmiennej value nadal wynosi:", value,
 "\n")

shadow_global()
print("Po powrocie do zakresu globalnego wartość zmiennej value nadal wynosi:", value,
 "\n")

change_global()
print("Po powrocie do zakresu globalnego okazuje się, że wartość zmiennej value",
      "\nzmieniła się na:", value)