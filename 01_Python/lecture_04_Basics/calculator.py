num1 =float(input("Enter a first number:"))
num2 =float(input("Enter a second number:"))
operation = input("Enter operation(+ - * / ) :")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1-num2)
elif operation == "/":
    print(num1 / num2) 
else:
    print("Invalid operations")           

