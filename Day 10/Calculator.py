from CalculatorArt import logo


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
num2 = float(input("What's the second number? "))

for symbol in operations:
    print(symbol)

operationSymbol = input("Pick an operation from the line above: ")

calculationFunction = operations[operationSymbol]

print(f'{num1} {operationSymbol} {num2} = {calculationFunction(num1, num2)}')
