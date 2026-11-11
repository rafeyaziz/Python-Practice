# while - 1-10
print("While 1-10")
i = 1
while i <= 10:
    print(i)
    i += 1

#10-1 reverse (for)
print("Reverse 1-10 for")
for i in range(10,0,-1):
    print(i)

#even numbers
print("Even Numbers 1-50")
for i in range(2,51,2):
    print(i)

#sum of numbers
print("Sum of numbers")
total = 0

for i in range(2,21,2):
    total = total + i

print("Sum: ",total)

#multiplication table
num = int(input("Enter a Number: "))

for i in range(1,11):
    result = num * i
    print(f"{num}x{i}={result}")

#stop at 6
for i in range(1,10):
    print(i)
    if i == 6:
        break
    