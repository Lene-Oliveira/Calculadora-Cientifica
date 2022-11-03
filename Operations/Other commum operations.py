#Other commum operations (exponentiation & √);
import math

def square(a):
    return a**2


def sqrt(a):
    return math.sqrt(a)

def exponentiate(a, b):
    return a**b

function_map= {
"square": square,
"square root": sqrt,
"exponentiate": exponentiate

}
op = input("Which operation would you like to do? square or square root? ")

if op in ["square", "square root", "log"]:
    a = float(input("What number would you like to perform your operation on? "))
    x = function_map[op](a)
    print(x)
else:
    a = float(input("What is the first number? "))
    b = float(input("What is the second number? "))
    x = function_map[op](a, b)
    print(x)
