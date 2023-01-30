from CalculatorArt import logo

isRunning = True


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)

num1 = float(input("What's the first number? "))
while isRunning:
    for symbol in operations:
        print(symbol)

    operationSymbol = input("Pick an operation from the line above: ")
    calculationFunction = operations[operationSymbol]\

    num2 = float(input("What's the next number? "))

    print(f'{num1} {operationSymbol} {num2} = {calculationFunction(num1, num2)}')

    continueCalculation = input(
        f"Type 'y' to continue calculating with {calculationFunction(num1, num2)}, type 'n' to start a new calculation or type anything else to exit: ")
    if continueCalculation == "y":
        num1 = calculationFunction(num1, num2)
    elif continueCalculation == "n":
        num1 = float(input("What's the first number? "))
    else:
        isRunning = False
