# Sarah Walker
# asks user for inputs and complete operations

from addition import add_two_numbers
from subtraction import subtractTwoNumbers
from multiplication import multiply
from division import division

print("Welcome to the math program!") 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: ")) 

addResult = add_two_numbers(num1, num2)
subResult = subtractTwoNumbers(num1, num2)
multResult = multiply(num1, num2)
divResult = division(num1, num2)

print(f"{num1} + {num2} = {addResult}")
print(f"{num1} - {num2} = {subResult}")
print(f"{num1} x {num2} = {multResult}")
print(f"{num1} / {num2} = {divResult}")
