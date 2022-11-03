#Complex functions (log, cos, sin, tan & ᴨ);
import math


def log(a, b):
    return  math.log(a)/math.log(b)

def cos(a):
    return math.acos(a)

function_map={
"log": log,
"cos": cos,

}
op = input("Which operation would you like to do? log, cos, sin, tan, e or pi? ")

if op in [ "acos", ]:
    a = float(input("What number would you like to perform your operation on? "))
    x = function_map[op](a)
    print(x)
elif op in ["log"] :
    a = float(input("what number would you like to calculate?"))
    b = float (input("in what base would you like to calculate your log?"))
    x = log(a, b)
    print(x)
elif op in ["cos"] :
    a = float(input("what number would you like to calculate?"))
    print(math.acos(a))
elif op in ["pi"] :
    print(math.pi)
elif op in ["e"] :
    print(math.e)
else:
    a = float(input("What is the first number? "))
    b = float(input("What is the second number? "))
    x = function_map[op](a, b)
    print(x)