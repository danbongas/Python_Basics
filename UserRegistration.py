

def main():
 var1 = input("Input + to Add User And - to Remove User:\n")

 if(var1 == "+"):
     add_user()

def add_user():		
	user1.ShowListofUsers()
    



class UserRegistration:
   userCount = 0


   def __init__(self, First_name,Last_name,Full_name,Email):
       self.First_name = First_name
       self.Last_name = Last_name
       self.Full_name = Full_name
       self.Email = Email  
       UserRegistration.userCount += 1
  
   
   def ShowListofUsers(self):
   	    print("Name: ", self.Full_name)
   	    print("Email: ", self.Email)

   def ShowCount(self):
        print("Total Users : %d" % UserRegistration.userCount)    

   


 
  

user1 = UserRegistration("Richardo","Milo", "Richardo Milo", "richardomilo@gmail.com")
user1.ShowListofUsers() 
user2 = UserRegistration("Norman","Reedus", "Norman Reedus", "normanreedus@gmail.com")
user2.ShowListofUsers() 
print("Total Users : %d" % UserRegistration.userCount)
main()




 

   


    

 	
