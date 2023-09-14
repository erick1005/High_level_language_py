num1 = int(input("enter first number: "))
op = input("enter the operator: ")
num2 = int(input("enter the second number: "))

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


#dictionary

simple_dictonary = {

#you can add as many words as you need and
#as below to display the meaning of the word selected'
    "res" : "result",
    "sum" : "total of everything",
}

print(simple_dictonary.get("res", "not a valid search parameter"))