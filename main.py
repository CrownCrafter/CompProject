
### Start Dependencies
import mysql.connector
### End Dependencies
### Start VARIABLE DECLARATIONS
loginstatus = False
userID = None
email = None
pwd = None
role = None
#TODO Connect to DB
### End VARIABLE DECLARATIONS
### Start FUNCTION DEFINITIONS
def create_server_connection(host_name, user_name, user_password, db):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db
        )
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor(connection)
    try:
        cursor.execute(query)
        connection.commit()
    except Error as err:
        print(f"Error: '{err}'")

def getLoginScreen(connection):
    email = input("Type Email ")
    pwd = input("Type Password ") #TODO Add SQL commands
    query = "SELECT USERID, Email, Password, Role FROM users WHERE Email = ", email," AND Password = ", pwd,";"
    print(query)
    if(loggedIn == True):
         print("Succesfully logged in. Sending you to homepage")
         ## Give user a role
    else:
         print("Error occured, crashing")
    return loggedIn

def getLogoutScreen(userID, email, pwd, role):
    print("Logged out")
    userID = None
    email = None
    pwd = None
    role = None

def getMovielist():
    print("Insert Movie list here")

def getUserlist():
    print("Insert user list here")
### End FUNCTION DEFINITIONS
### Start Program
connection = create_server_connection("localhost", "admin", "admin", "CompProject") #Connect to DB



print("Welcome to [INSERT NAME]")
while(True): #infinite loop
    print("Choose your preferred option") #TODO add conditional for user role
    if(loginstatus == True):
        print("1)View Available movies")
    if(loginstatus == False):
        print("2)Login") #TODO add login functionality

    else:
        print("2)Logout")
    if(role == "venueadmin" or role == "superadmin"):
        print("3)Add, edit, remove movies playing") #for Venueadmin, superadmin
    if(role == "superadmin"):
        print("4)Add, edit, remove users") #for superadmin
    print("5)Exit Program")
    oper = int(input("")) #TODO Add conditional for user role
    if(oper == 1 and loginstatus == True):
        getMovielist() #Only view
        continue
    elif(oper == 2):
        if(loginstatus == False):
            if(getLoginScreen(connection) == True):
                loginstatus = True
            elif(getLoginScreen(connection) == False):
                loginstatus = False
            continue
        else:
            getLogoutScreen()
            loginstatus = False
            continue
    if(role == "venueadmin" and oper == 3):
        getMovielist()
        continue #Show only venueadmin's venue movies with add, remove, edit privileges
    if(role == "superadmin" and oper == 3):
        getMovielist()
        continue #Show all movies
    if(role == "superadmin" and oper == 4):
        getUserlist()
        continue #TODO def getuserlist
    if(oper == 5):
        print("Exiting...")
        break
    else:
        print("Wrong Choice, try again")
        continue
#End
