def Lists():
 if m > n:
   try:
    for i in range(0,m):
	     print(lst[i]," ",list1[i])
   except:
	   print("Out of Bounds. Lists must have the same length")

 elif m < n:
    try:
       for i in range(0,n):
         print(lst[i]," ",list1[i])   
    except:
       print("Out of Bounds. Lists must have the same length")             
 elif m == n:
 	for i in range(0,n):
         print(lst[i]," ",list1[i])   


lst = []
n = int(input("Enter how many number you want in a list: "))
for i in range(0,n):
    var1 = input("Enter Any Inputs:")
    lst = lst + [var1] 

list1 = []
m = int(input("Enter how many number you want in a list: "))
for j in range(0,m):
    var1 = input("Enter Any Inputs:")
    list1 = list1 + [var1] 

Lists()    

