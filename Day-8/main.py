def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2
operators = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    num1 = float(input("Enter the Number1 : "))
    n1 = int(num1)
    for symbol in operators:
        print(symbol)
    should_continue = True

    while should_continue:
        operator_symbol = input("Pick an operator ")
        num2 = float(input("Enter the Number2 : "))
        n2 = int(num2)
        calculator_function = operators[operator_symbol]
        result = calculator_function(int(n1),int(n2))
        print(result)

        print(f"{n1} {operator_symbol} {n2} = {result}")

        if input(f"Type 'y' to continue Calculation with {result} or else type 'n' to start a new calculation ") == 'y':
            num1 = result

        else:
            should_continue = False
            calculator()

calculator()















