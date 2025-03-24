# try:
#     num =float(input("Wprowadz liczbe zmiennoprzecinkową: "))
# except:
#     print("Wystąpił problem")

# try:
#     num =float(input("Wprowadz liczbe zmiennoprzecinkową: "))
# except ValueError:
#     print("Wystąpił problem")

# print()
# for value in (None, "Hej!"):
#     try:
#         print("Próba konwersji:", value, "-->", end=" ")
#         print(float(value))
#     except (TypeError, ValueError):
#         print("Wystąpił jakiś błąd!")

print()
for value in (None, "Hej!"):
    try:
        print("Próba konwersji:", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("Możliwa jest tylko konwersja łańcucha lub liczby!")
    except ValueError:
        print("Możliwa jest tylko konwersja łańcucha cyfr!")