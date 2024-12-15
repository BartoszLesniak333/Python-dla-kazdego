#   2. Utwórz program, który wczytuje komunikat użytkownika, a następnie wypisuje
#      go w odwrotnej kolejności.
new = ""
word = input("Prosze wprowadz jakies słowo: ")
koniec = len(word) + 1
for i in range(1,koniec):
    new += (word[-i])

print(new)