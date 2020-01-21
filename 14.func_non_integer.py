def NonInteger(lst):
	new_val = list([i for i in lst if i.isnumeric()])

	return new_val


lst = []
n = int(input("Enter how many numbers you want in a list: "))
for i in range(0,n):
    var1 = input("Enter Any Inputs:")
    lst = lst + [var1] 

print(NonInteger(lst))    
