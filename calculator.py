print("Let's Build a CALCULATOR")

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if b == 0:
        return "Cannot be divisible by zero"
    return a/b 

a = float(input("Enter 1st Number: "))
b = float(input("Enter 2nd Number: "))
operator = input("Enter Operation(+,-,*,/): ")

if operator == "+":
    result = add(a,b)
    print("Result: ",result)
elif operator == "-":
    result = sub(a,b)
    print("Result: ",result)
elif operator == "*":
    result = mul(a,b)
    print("Result: ",result)
elif operator == "/":
    result = div(a,b)
    print("Result: ",result)
else:
    print("Incorrect Operation")