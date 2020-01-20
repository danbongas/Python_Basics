import random


list1 = ['physics','algebra','biology','computer','project management']
n = int(input("Enter any number within the range of 1-3: "))

str1 = list1[n]



for i in range(len(list1)-1, 0, -1):
  j = random.randint(0, i + 1)
  list1[i],list1[j] = list1[j],list1[i]

del list1[n]

     
    

print("You Just Deleted ",str1,"!"," Here are the results:\n", str(list1))
