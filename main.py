### Start Dependencies
import time
from prettytable import PrettyTable
import mysql.connector
### End Dependencies
### Start VARIABLE DECLARATIONS
loginstatus = False
id = None
email = None
pwd = None
role = None
loginstatus = False

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

def getSignupScreen():
    newEmail = input("Type your email: ")
    newPassword = input("Type your password: ")
    #SQL
    print("You're credentials have been added, you can now log in")

def getLoginScreen(connection):
    global email, pwd, role, loginstatus
    email = None
    pwd = None
    role = None
    loginstatus = False
    email = input("Type Email ")
    pwd = input("Type Password ")
    query = "SELECT UserID, Email, Role FROM users WHERE Email = '" + email + "' AND Password = '" + pwd +"';"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    try:
        id = result[0]
        email= result[1]
        role = result[2]
    except:
        print("You're credentials are incorrect")
    if(role != None):
        loginstatus = True
def getLogoutScreen():
    print("Logged out")
    global email, pwd, role, loginstatus
    loginstatus = False
    email = None
    pwd = None
    role = None


# def getUserlist(connection):
#     query = "SELECT Email, Role FROM users;"
#     cursor = connection.cursor()
#     cursor.execute(query)
#     result = cursor.fetchall()
#     tab = PrettyTable(["Email", "Role"])
#     for i in result:
#         tab.add_row([i[0], i[1]])
#     print(tab)
#     print("To filter by Role, enter r")
#     print("To filter by Email, enter n")
#     print("To go back to main menu, enter anything else")
#     oper = input("")
#     if(oper == 'r'):
#         print("Filter by following roles:")
#         print("1)User")
#         print("2)Venueadmin")
#         print("3)Superadmin")
#         print("To go back to main menu, enter anything else")
#         oper = input("")
#         if(oper == '1'):
#             query = "SELECT Email, Role FROM users WHERE Role = 'user';"
#             cursor = connection.cursor()
#             cursor.execute(query)
#             result = cursor.fetchall()

#             tab = PrettyTable(["Email", "Role"])
#             for i in result:
#                 tab.add_row([i[0], i[1]])
#             print(tab)
#             print("Enter anything to bo back to main menu")
#             oper = input("")

#         if(oper == '2'):
#             query = "SELECT Email, Role FROM users WHERE Role = 'venueadmin';"
#             cursor = connection.cursor()
#             cursor.execute(query)
#             result = cursor.fetchall()

#             tab = PrettyTable(["Email", "Role"])
#             for i in result:
#                 tab.add_row([i[0], i[1]])
#             print(tab)
#             print("Enter anything to go back to main menu")
#             oper = input("")
#         if(oper == '3'):
#             query = "SELECT Email, Role FROM users WHERE Role = 'superadmin';"
#             cursor = connection.cursor()
#             cursor.execute(query)
#             result = cursor.fetchall()

#             tab = PrettyTable(["Email", "Role"])
#             for i in result:
#                 tab.add_row([i[0], i[1]])
#             print(tab)
#             print("Enter anything to bo back to main menu")
#             oper = input("")

#     elif(oper == 'n'):
#         e = input("Enter Email to be Filtered: ")
#         query = "SELECT Email, Role FROM users WHERE Email = '"+e+"';"
#         cursor = connection.cursor()
#         cursor.execute(query)
#         result = cursor.fetchall()

#         tab = PrettyTable(["Email", "Role"])
#         for i in result:
#             tab.add_row([i[0], i[1]])
#         print(tab)
#         oper = input("")
def getMovielist():
    if(role == 'venueadmin'):
        #For Venueadmin
        #TODO unfinished GET VENUE NAME
        query = "SELECT Name FROM venues WHERE UserID='"+str(id)+"';"
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        print(result)
    else:
        query = "SELECT Name, Venue, Seats_free, Time FROM movies;"
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        tab = PrettyTable(["Name", "Venue", "Seats_free", "Time"])
        for i in result:
            tab.add_row([i[0], i[1], i[2], i[3]])
        print(tab)
        print("To Filter by Name, press n")
        oper = input("")
        if(oper == 'n'):
            name = input("Enter Movie Name ")
            query = "SELECT Name, Venue, Seats_free, Time FROM movies WHERE Name='"+str(name)+"';"
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            tab = PrettyTable(["Name", "Venue", "Seats_free", "Time"])
            for i in result:
                tab.add_row([i[0], i[1], i[2], i[3]])
            print(tab)
            oper = input("")



### End FUNCTION DEFINITIONS
### Start Program
connection = create_server_connection("localhost", "admin", "admin", "CompProject") #Connect to DB



# print("Welcome to [INSERT NAME]")
while(True): #infinite loop
    print(time.ctime())
    print("Choose your preferred option")
    if(role != None):
        print("Logged in as " + str(role))
    if(loginstatus == True):
        print("1)View Available movies")
    if(loginstatus == False):
        print("2)Login")

    else:
        print("2)Logout")
    if(role == "venueadmin" or role == "superadmin"):
        print("3)Add, edit, remove movies playing") #for Venueadmin, superadmin
    # if(role == "superadmin"):
    #     print("4)Add, edit, remove users") #for superadmin
    print("5)Exit Program")
    if(loginstatus == False):
        print("6)Sign up")
    oper = input("")
    if(oper == '1' and loginstatus == True):
        getMovielist() #Only view
        continue
    elif(oper == '2'):
        if(loginstatus == False):
            getLoginScreen(connection)
        else:
            getLogoutScreen()
    if(role == "venueadmin" and oper == '3'):
        getMovielist()
        continue #Show only venueadmin's venue movies with add, remove, edit privileges
    if(role == "superadmin" and oper == '3'):
        getMovielist()
        continue #Show all movies
    # if(role == "superadmin" and oper == '4'):
    #     getUserlist(connection)
    #     continue
    if(oper == '5'):
        print("Exiting...")
        connection.close()
        break
    if(loginstatus == False and oper == '6'):
        getSignupScreen()
#End
