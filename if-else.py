#Number check 
num = int(input("Enter a Number: "))

if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
elif num == 0:
    print("Number is zero")

#pass or fail
marks = int(input("Enter Marks: "))

if marks >= 40:
    print("PASS")
else:
    print("fail")

#Age classifier 
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenage")
elif age >= 20:
    print("Adult")

#Greater Number
num_1 = int(input("Enter Number 1: "))
num_2 = int(input("Enter Number 2: "))

if num_1 > num_2:
    print(f"{num_1} is greater than {num_2}")
elif num_1 < num_2:
    print(f"{num_2} is greater than {num_1}")
elif num_1 == num_2:
    print("Both are Equal") 