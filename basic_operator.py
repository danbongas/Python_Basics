
var = int(input("Enter a digit: "))
print ("DIGIT IS: ",var)

var2 = int(input("Enter another digit: "))
print ("DIGIT IS:", var2)

def addition(var,var2): 
     res = var + var2
     print(res)
     return

def subtraction(var,var2): 
     res = var - var2
     print(res)
     return   

def multiplication(var,var2): 
     res = var * var2
     print(res)
     return    
     
def division(var,var2): 
     res = var / var2
     print(res)
     return      


var3 = input("Type + to Add, - to Minus, * to Multiply, and / to Divide:\n")

if(var3 == '+'):
	addition(var,var2) 
elif(var3 == '-'):
    subtraction(var,var2)
elif(var3 == '*'):
    multiplication(var,var2)
elif(var3 == '%'):
    division(var,var2)        


