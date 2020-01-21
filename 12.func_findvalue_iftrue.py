def FindValue(lst): 
 indx = int(input('Type a number to see if it exists:\n'))

 for i in range(len(lst)): 	
    if lst[i] == indx:
        print("True  ")
        break   
    else:
        print("False") 
        break      
   

lst = []

n = int(input("Enter how many number you want in a list: "))
for i in range(0,n):
    var1 = int(input("Enter Digit(s):"))
    lst = lst + [var1] 


FindValue(lst)  
