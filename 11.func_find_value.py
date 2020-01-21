def LookForValue(lst): 
 indx = int(input('Type an index in range of 0-3 to get the value:\n'))

 for i in range(len(lst)):
    if i == indx:
        print("Value is: ",lst[indx])
        break
    if indx >= 3:
        print("No value at this point")
        break    
   

lst = [{1: 'one'},{2: 'two'},{3: 'three'}]

print("This is the value of the list: ",lst)

LookForValue(lst)  
