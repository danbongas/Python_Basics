list1 = []
n = int(input("Enter how many number you want in a list: "))

for i in range(0,n):
    var1 = int(input("Enter Digit(s):"))
 
    if var1%2!=0:
       list1 = list1 + [var1] 
 
print("Odd Numbers: "list1)    