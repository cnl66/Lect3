"""Genomgång baserad på Övning 1.40 - Miniräknare

Program som implementerar en "Miniräknare" med följande meny:
    1. Enter two integers
    2. Add
    3. Subtract
    4. Multiply
    5. Divide
    0. Exit
"""


def valid_input(prompt):
    valid = False
    while not valid:
        user_input = input(prompt)
        if user_input in '123450':
            user_input = int(user_input)
            if 0 <= user_input <= 5:
                valid = True
    return user_input


def menu():
    """Meny-hantering
    Returnerar menyvalet
    """
    print("1. Enter two integers")
    print("2. Add")
    print("3. Subtract")
    print("4. Multiply")
    print("5. Divide")
    print("0. Exit")
    choice = valid_input("Your input: ")
    return choice


def enter_numbers():
    """Läser in och returnerar två tal"""
    print("Choose your numbers")
    number1 = int(input("Number 1:"))
    number2 = int(input("Number 2:"))
    return number1, number2


def add_numbers(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    if number2 != 0:
        result = number1 // number2
    else:
        result = "Divide by zero is not possible"
    return result


print("\n\nWelcome to Calculator Program")
choice = -1
result = "Det finns inget resultat ännu"
num1 = 0
num2 = 0
while choice != 0:
    choice = menu()
    if choice == 0:
        pass
    elif choice == 1:
        num1, num2 = enter_numbers()
    elif choice == 2:
        result = add_numbers(num1, num2)
    elif choice == 3:
        result = subtract(num1, num2)
    elif choice == 4:
        result = multiply(num1, num2)
    elif choice == 5:
        result = divide(num1, num2)
    else:
        print("Input must be 0, 1, 2, 3, 4 or 5")
    if 2 <= choice <= 5:
        print("Result: ", result, "\n")
