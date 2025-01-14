# Day 10: Functions with Outputs, Docstrings
# Calculator Project
import art

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(art.logo)

    def perform():
        print(f"{number1} {symbol} {number2} = {result}")

    should_accumulate = True
    number1 = float(input("What's the first number?: "))

    while should_accumulate:
        symbol = input("+\n-\n*\n/\nPick an operation: ")
        number2 = float(input("What's the next number?: "))

        if symbol not in operations:
            symbol = "undefined"
            result = 0.0
            perform()
        else:
            result = operations[symbol](number1, number2)
            perform()

        restart = input(f"Type 'y' to continue calculating with your result:"
                        f" {result}, or type 'n' to start a new calculation: ")

        if restart == 'n':
            print("\n"*100)
            should_accumulate = False
            calculator()
        elif restart == 'y':
            number1 = result

calculator()
