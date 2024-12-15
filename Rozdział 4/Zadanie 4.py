#   4. Utwórz grę, w której komputer wybiera losowo słowo, które gracz musi
#      odgadnąć. Komputer informuje gracza, ile liter znajduje się w wybranym
#      słowie. Następnie gracz otrzymuje pięć szans na zadanie pytania, czy jakaś litera
#      jest zawarta w tym słowie. Komputer może odpowiedzieć tylko „tak” lub „nie”.
#      Potem gracz musi odgadnąć słowo.

import random

WORDS = ("ziemniak","marchew","ogórek","papryka","pietruszka")
word = random.choice(WORDS)
answer = None

print("\n\n\n")
print("\t\tWitaj w grze zgadnij jakie to warzywo\n\n\n")
print("Twoim zadaniem jest odgadąć o jakie warzywo mam na myśli")
print("\nNa początku podaje ci ile liter posiada wymyślone przeze mnie warzywo ,a nastepnie")
print("otrzymujesz pięć szans na zadanie pytania, czy jakaś litera jest zawarta w tym słowie.")
print("Będe odpowiadał jedynie twierdząco czyli 'tak' bądz 'nie'")
print("Potem musisz odgadnąć słowo")
print("Jeżeli chcesz sie poddać wpisz 'Poddaje się' w trakcie podawanie odpowiedzi\n\n ")



print("wylosowałem warzywo na: ", len(word)," liter")

for i in range(1,6):
    print("Pytanie ",i," : Czy warzywo posiada litere: ")
    odpowiedz = input()
    if odpowiedz in word:
        print("tak")
    else:
        print("nie")

while answer != word and answer !="Poddaje się":
    answer = input("Warzywo o którym myślisz nazwya się: ")

    if answer == word:
        print("Brawo udało ci się odgadnąć warzywo!")

    elif answer == "Poddaje się":
        print("Miałem na myśli: ",word)

    else:
        print("Nie myśle o tym warzywie\n")