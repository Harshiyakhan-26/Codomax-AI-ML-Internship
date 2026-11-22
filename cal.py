def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operator"

x = float(input("First number: "))
y = float(input("Second number: "))
operator = input("Operator (+, -, *, /): ")
print("Result:", calculator(x, y, operator))
