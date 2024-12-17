import random

HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O 
 |  /-+-/
 |    |
 |   
 |  
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   |
 |   |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |
----------
""")

MAX_WRONG = len(HANGMAN) - 1

WORDS = ("pies","kot","chomik","rybka","świnka","żółw","papuga")

word = random.choice(WORDS)

so_far = "_"*len(word)
wrong = 0
used = []

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nWykorzystałeś już następujące litery:\n", used)
    print("\nNa razie zagadkowe słowo wygląda tak:\n", so_far)

    guess = input("Wprowadz litere")
    guess.lower()

    while guess in  used:
        print("Wprowadziłeś już tą litere.")
        guess = input("Wprowadz nową litere")
        guess.lower()

    if guess in word:
        print("\nTak!", guess, "znajduje się w zagadkowym słowie!")
        new = ""
        for i in range(len(word)):
            if guess in word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print("Ta litera nie znajduje się w tym słowie")
        wrong += 1

    if wrong == MAX_WRONG:
        print(HANGMAN[wrong])
        print("\nPrzegrałeś")
        print("\nZagadkowe słowo to: ",word)
    else:
        print("\nWygrałeś  !!!!!!")

