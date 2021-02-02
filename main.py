### Start Dependencies
import mysql.connector
### End Dependencies

### Start VARIABLE DECLARATIONS
loggedin = False
#TODO Connect to DB
cnx = mysql.connector.connect()

# End Connection
### End VARIABLE DECLARATIONS
### Start FUNCTION DEFINITIONS
def getLoginScreen():
    email = input("Type Email ")
    pwd = input("Type Password ") #TODO Add SQL commands
    if(loggedin == True):
        print("Succesfully logged in. Sending you to homepage")
    else:
        print("Error occured, crashing")



### End FUNCTION DEFINITIONS
### Start Program
print("Welcome to [INSERT NAME]")
while(True): #infinite loop
    print("Choose your preferred option") #TODO add conditional for user role
    print("1)View Available movies")
    if(loggedin == False):
        print("2)Login") #TODO add login functionality
    else:
        print("2)Logout")
    print("3)Add, edit, remove movies playing") #for Venueadmin, superadmin
    print("4)Add, edit, remove users") #for superadmin
    print("5)Exit Program")
    oper = int(input("")) #TODO Add conditional for user role
    if(oper == 1):
        getMovielist() #TODO def getmovielist
    elif(oper == 2):
        getLoginScreen()
        if(loggedin == True):
            continue


        else:
            break

    elif(oper == 5):
        print("Exiting...")
        break
    #TODO Add conditional for oper based on user role
    #TODO Add logic for login / Logout depending on current user status
    else:
        print("Wrong Choice, try again")
        continue
