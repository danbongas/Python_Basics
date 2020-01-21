def CheckDifference(lst,list1): 
     return (list(set(lst) - set(list1)))
 
    
   

lst = []
n = int(input("Enter how many number you want in a list: "))
for i in range(0,n):
    var1 = int(input("Enter Digit(s):"))
    lst = lst + [var1] 

list1 = []
 
m = int(input("Enter how many number you want in a list: "))
for i in range(0,m):
    var2 = int(input("Enter Digit(s):"))
    list1 = list1 + [var2] 



print("Resulted List:\n",CheckDifference(lst,list1))  
