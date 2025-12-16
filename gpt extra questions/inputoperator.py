a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op=input("Enter operation (+, -, *, /): ")
if op == '+':
    print(f"The sum is: {a + b}")
elif op == '-':     
    print(f"The difference is: {a - b}")
elif op == '*':
    print(f"The product is: {a * b}")
elif op == '/':
    if b != 0:
        print(f"The quotient is: {a / b}")
    else:
        print("Error: Division by zero is not allowed.")        
