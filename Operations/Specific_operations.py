#this contains special numbers such as pi and e;
import math

op = input("Wich special number would you like to work with? Pi or e? ")

if op in ["pi"] :
    print(math.pi)
elif op in ["e"] :
    print(math.e)
