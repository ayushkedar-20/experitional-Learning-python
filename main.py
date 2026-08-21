import math

a = float(input("Enter number: "))
op = input("Enter (+,-,*,/,sqrt,^): ")

if op == "+":
    b = float(input("Enter number: "))
    print(a + b)
elif op == "-":
    b = float(input("Enter number: "))
    print(a - b)
elif op == "*":
    b = float(input("Enter number: "))
    print(a * b)
elif op == "/":
    b = float(input("Enter number: "))
    print(a / b)
elif op == "sqrt":
    print(math.sqrt(a))
elif op == "^":
    b = float(input("Enter power: "))
    print(a ** b)
