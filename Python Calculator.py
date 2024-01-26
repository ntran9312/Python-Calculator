#Define four subroutines - add, subtract, multiply, divide that add multiply etc two numbers and return the result. Each should have two integer number arguments.
#The user is asked to input two numbers.  These numbers will be passed as arguments into one of the subroutines.
#The user is asked to input 1 to add, 2 to subtract etc.
#If they input 1, call the ‘add’ subroutine, input 2 calls the ‘subtract’ subroutine etc
#Output the returned result as part of a sentence.

def multiply(num1, num2):
  return num1 * num2

def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def divide(num1, num2):
  return num1 / num2

numOne = int(input("Enter your first number:\n"))
numTwo = int(input("Enter your second number:\n"))

operator = int(input("1 for multiply\n2 for add\n3 for subtract\n4 for divide\nEnter the number corresponding to what you want to do:\n"))

if operator == 1:
  equals = multiply(numOne, numTwo)
  print("Your result is " + str(equals))

elif operator == 2:
  equals = add(numOne, numTwo)
  print("Your result is " + str(equals))

elif operator == 3:
  equals = subtract(numOne, numTwo)
  print("Your result is " + str(equals))

elif operator == 4:
  equals = divide(numOne, numTwo)
  print("Your result is " + str(equals))

