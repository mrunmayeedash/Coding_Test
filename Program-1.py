#Program 1
class Calculator:
    def calculate(self, a: float, b: float, operation: str):
        operation = operation.lower()

        if operation == "add":
            return a + b

        elif operation == "sub":
            return a - b

        elif operation == "mul":
            return a * b

        elif operation == "div":
            if b == 0:
                return "Error: Cannot divide by zero"
            return a / b

        else:
            return "Error: Invalid operation"

calc = Calculator()

a = float(input("Enter value for a: "))
op = input("Enter operation (add/sub/mul/div): ")
b = float(input("Enter value for b: "))

result = calc.calculate(a, b, op)
print("Result:", result)
