# Litet avgränsat kodavsnitt
# En funktion gör EN sak
# En funktion ska vara en väl avgränsad enhet, dvs all information den behöver ska skickas in i den
# och den ska returnera sitt resultat


# syntax

def my_function(message):
    print("Funktionen kör")
    print(message)


def calc_function(x):
    """Funktion som räknar ut f(x) = x^2 + 1

    Parameter x: ett tal
    Returvärde:  tal av samma typ som x"""
    result = x**2 + 1
    return result


# my_function("Hej")
# my_function("Fint väder idag")

# number = 17
# my_function(number)


number = 7
new_number = calc_function(number)
print(new_number)
