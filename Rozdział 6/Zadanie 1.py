#   1. Popraw funkcję ask_number() w taki sposób, aby mogła być wywoływana
#      z wartością kroku. Spraw, aby domyślną wartością kroku była liczba 1.

def ask_number(question,low,high,step = 1):
    response = None
    while response not in range(low,high,step):
        response = int(input(question))
    return response

print(ask_number("Podaj liczbe: ",1,10,2))

