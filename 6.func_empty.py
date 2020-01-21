def EmptyOrNot():  
   if(len(list1) == 0):
       print("Empty ",list1)
   else:
  	   print("Not Empty",list1) 

list1 = []
n = int(input("Enter how many number you want in a list: "))

for i in range(0,n):
    var1 = int(input("Enter Digit(s):"))
    list1 = list1 + [var1] 

EmptyOrNot()