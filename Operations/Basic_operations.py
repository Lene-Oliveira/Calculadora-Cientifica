#Basic four operations (+, -, / and *)
#importing a library with the especific functions that will be needed
import math

#function definitions
def add(a, b):
    return a + b
 
def subtract(a, b):
    return a - b
 
def divide(a, b):
    return a/b
 
def multiply(a, b):
    return a*b

    
  
    # create map
function_map = {
    "add": add,
    "subtract": subtract,
    "divide": divide,
    "multiply": multiply,

}

#ask the user for the desired opperation
op = input("Which operation would you like to do? Add, subtract, divide or multiply? ")

if op in ["square", "square root", "log"]:
    a = float(input("What number would you like to perform your operation on? "))
    x = function_map[op](a)
    print(x)
else:
    a = float(input("What is the first number? "))
    b = float(input("What is the second number? "))
    x = function_map[op](a, b)
    print(x)
