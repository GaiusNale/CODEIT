def add(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")

def sub(num1, num2):
    print(f"{num1} - {num2} = {num1-num2}")

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

ans = input("Choose one of two options\n1. Add\n2. Subtract\n")

if ans == "1":
    add(a,b)
elif ans == "2":
    sub(a,b)