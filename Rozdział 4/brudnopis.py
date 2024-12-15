########################### krojenir pizzy ###########################
# start = None
# word = "pizza"
#
# while start != "":
#     start = input("Start: ")
#     if start:
#         start = int(start)
#         koniec = int(input("Koniec: "))
#
#         print(word[start:koniec])

########################### inwentarz bohatera  ###########################
#
# tuple = ()
#
# if not tuple:
#     print("Nie posiadasz nic w ekwipunku")
#
# input("Wcisnij enter")
#
# tuple = ("srebrny miecz",1,
#          "zloty medalion",2,
#          "eliksir życia",4,
#          "szelingi",150)
#
# if tuple:
#     for items in tuple:
#         print(items)
#
#
# print(tuple)

######################### Zgasnij jakie to słowo ###########################
#
# import random
#
# WORDS = ("klawiatura","myszka","monitor","zasilacz","sluchawki")
#
# word = random.choice(WORDS)
#
# correct = word
#
# jumble = ""
#
# while word:
#     possition = random.randrange(len(word))
#
#     jumble += word[possition]
#
#     word = word[:possition] + word[(possition)+1:]
#
# print("Odgadnij to słowo: ",jumble)
# 
# answer = input("Podaj swoją odpowiedz: ")
#
# while answer != correct and answer != "":
#     print("niesstety to nie to słowo ")
#     answer = input("Podaj swoją odpowiedz: ")
#
# if answer == correct:
#     print("Brawo odgadłes słowo")
#
#
