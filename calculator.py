"""
17. Write a program that serves as a basic calculator. It asks for two
    numbers, then it asks for an operator. Gracefully deal with input that
    doesn't cleanly convert to numbers. Deal with division by zero errors.
"""


class Calculator():
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operator = operator

    def sum(self):
        return self.operand1 + self.operand2

    def diff(self):
        return self.operand1 - self.operand2

    def divide(self):
        return self.operand1 / self.operand2

    def multiply(self):
        return self.operand1 * self.operand2


try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    operator = input("Enter operator: ")
    calc = Calculator(num1, num2)
    if operator == '+':
        result = calc.sum()
    elif operator == '-':
        result = calc.diff()
    elif operator == '/':
        try:
            result = calc.divide()
        except ZeroDivisionError:
            print("You cannot divide by 0.")
            exit(1)
    elif operator == '*':
        result = calc.multiply()
    else:
        print("Invalid operator!")
        exit(1)
    print("Result = ", result)
except ValueError:
    print("Invalid input!")
