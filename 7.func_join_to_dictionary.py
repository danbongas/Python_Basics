
def Convert(lst): 
    res_dct = {jnlst[i]: jnlst[i + 1] for i in range(0, len(jnlst), 2)} 
    return res_dct 

lst=[]
lst1=[]    

print("Merging Two Arrays into a Dictionary\n")     
print("Enter 3 Strings:\n")          
for i in range(0,3):  
  varnames = input('String:\n')
  lst.append(varnames)
print("Enter Another 3 Strings:\n")  
for j in range(0,3):
  varstring = input('String:\n')
  lst1.append(varstring)  

jnlst = lst + lst1



print(Convert(jnlst)) 