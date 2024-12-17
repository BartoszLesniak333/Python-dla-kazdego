#   1. Utwórz program, który wypisuje listę słów w przypadkowej kolejności.
#      Program powinien wypisać wszystkie słowa bez żadnych powtórzeń

import random

word = ['Mbappe','Vinicius','Bellingham','Rodrygo','Valverde','Militao']

word_new = []

while len(word) != 0:
    choice = random.choice(word)
    word_new.append(choice)
    for i in word:
        if i == choice:
            word.remove(i)


print(word_new)