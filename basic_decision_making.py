
str1 = int(input("Enter starting year: "))
str2 = int(input("Enter end year: "))
s = 0
for num in range(str1,str2):	
  if num%4==0:
  	s += 1
  	
if s!=0:
   print("Number of Leap Years Found: ", s)  	

if s==0:
   print("No Leap Years Found: ")	
