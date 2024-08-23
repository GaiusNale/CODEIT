import func

# i want to create a claculator that takes input from the user and adds, subtracts, multiplies, and divides the inputted numbers

# take variables (numbers) from the user 
num=int(input("Enter a number: "))
num2 = int(input ("Enter another number: ")) 

func.add(num, num2)
func.sub(num, num2)
quo = num / num2
prod = num * num2
exp = num ** num2
mod = num % num2


# added the numbers together

print(f"{num} divided {num2} is {quo}")
print(f"the product of {num} and {num2} is {prod}")
print(f"the result of {num} raised to the power of {num2} is {exp}")
print(f"the modulus of {num} and {num2} is {mod}")


name1 = "camille"
name2 = "adeiyi"

name_list = name1 + " " + name2
