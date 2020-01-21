def FindIndex(lst): 
 indx = int(input('Type a number you want to get the index:\n'))

 for i in range(len(lst)):
    if lst[i] == indx:
        print("Index is: ",i)
   

lst = []

n = int(input("Enter how many number you want in a list: "))
for i in range(0,n):
    var1 = int(input("Enter Digit(s):"))
    lst = lst + [var1] 


FindIndex(lst)  
