

class UserRegistration:
   userCount = 0
   


   def __init__(self, First_name,Last_name,Full_name,Email):
       self.First_name = First_name
       self.Last_name = Last_name
       self.Full_name = First_name +" "+ Last_name
       self.Email = Email         
       UserRegistration.userCount += 1     
              

  
   
   def ShowUser(self):
   	    print("Name: ", self.Full_name)
   	    print("Email: ", self.Email)

   
    

   def ShowCount(self):
        print("Total Users : %d" % UserRegistration.userCount)

   @classmethod
   def InputUser(cls):
       return cls(
       	  input('First Name:'),
       	  input('Last Name:'),
       	  "",        	        	  
       	  input('Email:'),
       	)

def main():

    var = input("Input + to Add User, # to Show, * to Update, - to Remove User :\n")
    if(var=='+'):
       return AddUser()
    if(var=='#'):
       return ShowAllUsers()   
    if(var=='*'):
       return UpdateUser() 
    if(var=='-'):
       return RemoveUser()     

def AddUser():

  fnme = input('First name:')
  lnme = input('Last name:')
  flnme = fnme+' '+lnme
  eml = input('Email:')
  emp = UserRegistration(fnme,lnme,flnme,eml)
  emps[emp.Full_name] = emp
  emp.ShowUser()
  print("Total Users Available :\n",len(emps))
  lst.append(UserRegistration(fnme,lnme,flnme,eml))
  return main()

def ShowAllUsers():

  for i in range(len(lst)):    
  	print("-------------------------")
  	print("User Index:", i)
  	print("First Name:",lst[i].First_name,"\n")
  	print("Last Name:",lst[i].Last_name,"\n")
  	print("Full Name:",lst[i].Full_name,"\n")
  	print("E-mail:",lst[i].Email,"\n")
  	print("-------------------------")
  	

  if len(lst) == 0:
     print("---NO DATA---")	
  return main()

def UpdateUser():

  print("There are ",len(lst)," users available. Input the index of the user you want to update:\n ")
  print("Note: index starts at 0:\n")
  user_id = int(input())
  for i in range(len(lst)):
   if i == user_id:
     print("Updating",lst[i].Full_name,"'s Profile..\n")
     fnme = input('First name:')  	   
     lnme = input('Last name:')
     flnme = fnme+' '+lnme
     eml = input('Email:')
     lst[i].First_name = fnme
     lst[i].Last_name = lnme
     lst[i].Full_name = flnme
     lst[i].Email = eml        

  return main()

def RemoveUser():

   print("There are ",len(lst)," users available. Input the index of the user you want to remove:\n ")
   print("Note: index starts at 0:\n")
   user_id = int(input())
   for i in range(len(lst)):
    if i == user_id:
       print(lst[i])
   print("User Deleted...\n")    
   return main()		





lst = []
emps = {}
v = 0
main()            


            	       

   





 

   


    

 	
