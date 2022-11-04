#this contains special numbers such as pi and e;
import math

op = input("Wich special number would you like to work with? Pi or e? ")

if op in ["pi"] :
    print(math.pi)
elif op in ["e"] :
    print(math.e)
else :
    print("wrong path")
    ch = input("would you like to go back to the first option?")
    
if ch in ["yes"] :
    print("loading...")

import Basic_operations
