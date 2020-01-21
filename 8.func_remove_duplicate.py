def RemoveDuplicate(lst):
   list1 = []
   for i in lst:
     if i not in list1:
      list1.append(i)
   return list1		

lst = []

n = int(input("Enter how many number you want in a list: "))
for i in range(0,n):
    var1 = int(input("Enter Digit(s):"))
    lst = lst + [var1] 


print("List with no duplicates: \n",RemoveDuplicate(lst))   
