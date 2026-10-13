class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @property
    def add(self):
        return f"{self.num1 + self.num2}"

    @property
    def subtract(self):
        return f"{self.num1 - self.num2}"

    @property
    def multiply(self):
        return f"{self.num1 * self.num2}"

    @property
    def divide(self):
        return f"{self.num1 / self.num2}"

    @property
    def exponentiate(self):
        return f"{self.num1**self.num2}"


num1 = int(input("Enter first number: "))
symbol = input("Enter operation (+, -, *, /, **) = ")
match symbol:
    case "+":
        num2 = int(input("Enter second number: "))
        print(num1 + num2)
    case "-":
        num2 = int(input("Enter second number: "))
        print(num1 - num2)
    case "*":
        num2 = int(input("Enter second number: "))
        print(num1 * num2)
    case "/":
        num2 = int(input("Enter second number: "))
        print(num1 / num2)
    case "**":
        num2 = int(input("Enter second number: "))
        print(num1**num2)
    case _:
        print("Invalid Operation Selected")


# calc = Calculator(num1, num2)

# print(calc.add)
# print(calc.subtract)
# print(calc.multiply)
# print(calc.divide)
# print(calc.exponentiate)
