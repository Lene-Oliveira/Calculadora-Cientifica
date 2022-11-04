Math for all the technical and specific functions such as cossen, Logaritm, pi and e;
    Exemples of usages troghout my code (for this part, please refer to "Other_commum_operations.py"):
        Import math 
        def sqrt(a):
             return math.sqrt(a)
        function_map = {
            "square root" = sqrt, 
        }
        op = input("Which operation would you like to do? square or square root? ")

            if op in ["square", "square root", "log"]:
                a = float(input("What number would you like to perform your operation on? "))
                 x = function_map[op](a)
                 print(x)
