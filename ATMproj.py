import logging
logging.basicConfig(filename="ATM.log",level=logging.INFO,format="%(asctime)s:%(levelname)s%(message)s")
class User:#my first class .This class creates an object of the user and has a method which stores the user details in txt file
   
    def __init__(self,name,accno,pin,amt):
        self.name=name
        self.accno=accno
        self.pin=pin
        self.amt=amt
    

    def storage(self):
        self.details=[name,accno,pin,amt]
        with open("database.txt","a") as f:
            for i in self.details:
                f.write(str(i) + "\t")
            f.write("\n")
        
                
class ATM(User):#ATM is the class which has all the methods that perform all the operations of an ATM.
    def __init__(self,pin):
        self.pin=pin
    def card(self):#This method auntheticates the pin entered from all the pins in the database 
        try:
         with open("database.txt","r") as f:
             details=f.readlines()
            
             for i in range(0,len(details)):
                 data=details[i].split("\t")
                 if str(self.pin)==data[2]:
                    print("Welcome",data[0])
                    self.amount=int(data[3])
                    self.nxtstep=1
                    break
                    
                 else:
                    if i==len(details)-1:
                        print("Authentication Error")
                        self.nxtstep=2
        except:
            print("first sign in")
            self.nxtstep=2
    #all the furthur methods take place only after the authentication
          
    def ViewBal(self):#this method views the balance of the user
         print("the current Balance is Rs",self.amount)
         
    def Withdraw(self,money):#this method is used for money withdrawal
        if money>self.amount:
            print("Not enough to withdraw")
        else:
            self.amount-=money
            with open("database.txt","r+") as f:
              details=f.readlines()
              for a in details:
                  data=a.split("\t")
                  
                  if data[2]==str(self.pin):
                     temp=data[3]
            #the next few steps are for updating the file using replace function
            with open("database.txt","r") as f:
                 details=f.read()
            with open("database.txt","w") as f:
                 f.write(details.replace(str(temp),str(self.amount)))
           
         
           
            
            print("Amount withdrawal successful")

            logging.info("{} has been withdrawn from your account.remaining balance is {}".format(money,self.amount))

            
    def Deposit(self,money):#this method is used for money deposit
        
            self.amount+=money
            with open("database.txt","r+") as f:
                details=f.readlines()
                for i in range(0,len(details)):
                  data=details[i].split("\t")
                  if (str(self.pin))==data[2]:
                      temp=data[3]
            with open("database.txt","r") as f:
                 details=f.read()
            with open("database.txt","w") as f:
                 f.write(details.replace(str(temp),str(self.amount)))
           
             #the next few steps are for updating the file using replace function    
                   
            logging.info("{} has been deposited into your account.current balance is {}".format(money,self.amount)) 
            
            print("Amount deposit successful")



print("Welcome To ATM")
while True:
    choice=input("Login or signin or exit.Type the option")
    if choice.upper()=="SIGNIN":
       
            name=input("Enter Name")
            accno=int(input("Enter account no"))
            pin=int(input("Enter pin"))
            amt=int(input("Enter amt"))
            Obj1=User(name,accno,pin,amt)
            #the next few steps include an exception error handling in case database.txt does not exist because of the user being the first one
            try:
              with open("database.txt","r") as f:
                details=f.readlines()
            
                  
               #we check the username to see if user has already signedin or not
                for i in range(0,len(details)):
                      data=details[i].split("\t")
                      if (Obj1.name).upper()==(data[0]).upper():
                         print("U are already signed in so kindly login")
                         break
                      else:
                        if i==len(details)-1:
                           print("signed in")
                           Obj1.storage()
                            
            except:
                 print("U are the first user .Welcome")
                 Obj1.storage()
    if choice.upper()=="LOGIN":
           print("First Authenticate Your Card")
           pin=int(input("Enter the pin"))
           Obj2=ATM(pin)
           Obj2.card()
           if Obj2.nxtstep==1:
               while True:
                  options=input("1.View Balance 2.Deposit 3.Withdraw 4.Exit.Type the option number")
                  if options=="1":
                     Obj2.ViewBal()
                  elif options=="2":
                      money=int(input("Enter the money u want to deposit"))
                      Obj2.Deposit(money)
                  elif options=="3":
                        money=int(input("Enter the money u want to withdraw"))
                        Obj2.Withdraw(money)

                  elif options=="4":
                      break


    if choice.upper()=="EXIT":
             print("operation carried out")
             break                     
                                  

       
               
               
            
    
        
