

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
       self.Full_name = First_name +" "+ Last_name
       self.Email = Email  
       UserRegistration.userCount += 1
       self.users = []
              

  
   
   def ShowUser(self):
   	    print("Name: ", self.Full_name)
   	    print("Email: ", self.Email)

   def ShowListofUsers(self):
        for i in self.users:
            print(i)    

   def ShowCount(self):
        print("Total Users : %d" % UserRegistration.userCount)    

   


 
  

user1 = UserRegistration("Richardo","Milo", "Richardo Milo", "richardomilo@gmail.com")
user1.ShowUser() 
user2 = UserRegistration("Norman","Reedus", "Norman Reedus", "normanreedus@gmail.com")
user2.ShowUser() 
print("Total Users : %d" % UserRegistration.userCount)
main()




 

   


    

 	
