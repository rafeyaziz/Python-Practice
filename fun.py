def add(a,b):
    return a + b

result = add(20,10)
print(result)

def mul(a,b):
    return a * b

result = mul(15,34)
print(result)

def div(a,b):
    return a/b

result = div(16,4)
print(result)

def sub(a,b):
    return a - b
result = sub(14,10)
print(result)

def square(num):
    return num * num 
result = square(5)
print(result)

def greet(name):
    print("Hello",name)

greet("Rafey")

def is_even(num):
    if num % 2:
        print("Odd Number")
    else:
        print("Even number")

num = int(input("Enter a number: "))
check = is_even(num)