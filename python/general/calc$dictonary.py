num1 = input("enter first number: ")
op = input("enter the operator: ")
num2 = input("enter the second number")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("invalid operator")