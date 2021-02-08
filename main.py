
### Start Dependencies
import mysql.connector
### End Dependencies
### Start VARIABLE DECLARATIONS
loginstatus = False
email = None
pwd = None
role = None
loginstatus = False

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


def getLoginScreen(connection):
    global email, pwd, role, loginstatus
    email = None
    pwd = None
    role = None
    loginstatus = False
    email = input("Type Email ")
    pwd = input("Type Password ")
    query = "SELECT Email, Role FROM users WHERE Email = '" + email + "' AND Password = '" + pwd +"';"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    email= result[0]  ## TRY and EXCEPT block2s
    role = result[1]
    if(role != None):
        loginstatus = True
def getLogoutScreen():
    print("Logged out")
    global email, pwd, role, loginstatus
    loginstatus = False
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
    if(role != None):
        print("Logged in as " + str(role))
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
    if(loginstatus == False):
        print("6)Sign up")
    oper = int(input("")) #TODO Add conditional for user role
    if(oper == 1 and loginstatus == True):
        getMovielist() #Only view
        continue
    elif(oper == 2):
        if(loginstatus == False):
            getLoginScreen(connection)
        else:
            getLogoutScreen()
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
        connection.close()
        break
    if(loginstatus == False and oper == 6):
        getSignupScreen()
#End
