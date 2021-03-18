### ***TODO LIST***
### TICKETING SQL DONE ENHANCEMENT Ask user for seat
### TODO ADD, EDIT, DELETE movies to venue for venueadmin
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
def create_server_connection(host_name, user_name, user_password, db): #Server Connect
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

def getSignupScreen() -> str:
    newEmail = input("Type your email: ")
    newPassword = input("Type your password: ")

    query = "INSERT INTO users(Email, Password, Role) VALUES ('"+str(newEmail)+"', '"+str(newPassword)+"', 'user');"
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit() # Fixed bug where INSERT not possible
        print("You're credentials have been added, you can now log in")
    except:
        print("There was some error in adding your credentials, this email is already in use")

def getLoginScreen(connection) -> str:
    global id, email, pwd, role, loginstatus
    # id = None
    # email = None
    # pwd = None
    # role = None
    # loginstatus = False

    email = input("Type Email ")
    pwd = input("Type Password ")
    query = "SELECT UserID, Email, Role FROM users WHERE Email = '" + email + "' AND Password = '" + pwd +"';"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    # Basically to check as None
    try:
        id = result[0]
        email= result[1]
        role = result[2]
    except:
        print("You're credentials are incorrect")
    if(role != None): # Giving Power to user
        loginstatus = True

def getLogoutScreen() -> str:
    print("Logged out")
    global email, pwd, role, loginstatus
    loginstatus = False # logging out
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
        query = "SELECT Name FROM venues WHERE UserID='"+str(id)+"';"
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        venueName = result[0] #VenueName of Venueadmin

        query = "SELECT MovieID, Name, Venue, Seats_free, Time FROM movies WHERE Venue='"+str(venueName)+"' AND Time >= now();"
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        print("Venue Admin of ", venueName)

        tab = PrettyTable(["MovieID","Name", "Venue", "Seats_free", "Time"])
        for i in result:
            tab.add_row([i[0], i[1], i[2], i[3], i[4]])
        print(tab)

        print("To Filter by Name, press n")
        print("To View all movies, press a")
        oper = input("")

        if(oper == 'n'): #Search by Movie name, only show movies owned by venue
            name = input("Enter Movie Name ")
            query = "SELECT MovieID, Name, Venue, Seats_free, Time FROM movies WHERE Name='"+str(name)+"';"
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()

            tab = PrettyTable(["MovieID", "Name", "Venue", "Seats_free", "Time"])
            for i in result:
                tab.add_row([i[0], i[1], i[2], i[3], i[4]])
            print(tab)
            oper = input("")

        if(oper == 'a'): #Search by all, only show movies owned by venue
            query = "SELECT MovieID, Name, Venue, Seats_free, Time FROM movies WHERE venue='"+str(venueName)+"';"
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()

            print("Venue Admin of ", venueName)
            tab = PrettyTable(["MovieID", "Name", "Venue", "Seats_free", "Time"])
            for i in result:
                tab.add_row([i[0], i[1], i[2], i[3], i[4]])
            print(tab)

    else: #For anyone else
        query = "SELECT MovieID, Name, Venue, Seats_free, Time FROM movies WHERE Time >= now();"
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        tab = PrettyTable(["MovieID", "Name", "Venue", "Seats_free", "Time"])
        for i in result:
            tab.add_row([i[0], i[1], i[2], i[3], i[4]])
        print(tab)

        print("To Filter by Name, press n ")
        print("To Filter by MovieID and book tickets, press b ")
        oper = input("")

        if(oper == 'n'): # Search by Name
            name = input("Enter Movie Name ")
            query = "SELECT MovieID, Name, Venue, Seats_free, Time FROM movies WHERE Name='"+str(name)+"';"
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()

            tab = PrettyTable(["MovieID", "Name", "Venue", "Seats_free", "Time"])
            for i in result:
                tab.add_row([i[0], i[1], i[2], i[3], i[4]])
            print(tab)
            oper = input("")
        if(oper == 'b'): #Search by MovieID
            id_query = input("Enter Movie ID to be filtered")
            query = "SELECT MovieID, Name, Venue, Seats_free, Time FROM movies WHERE MovieID='"+str(id_query)+"' AND Time >= now();"
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchone()

            if(result == None):
                print("No Movies are coming up!!!")

            else:
                tab = PrettyTable(["MovieID", "Name", "Venue", "Seats_free", "Time"])
                tab.add_row([result[0], result[1], result[2], result[3], result[4]])
                print(tab)
                print("If you want to book this ticket, press B")
                oper = input("")
                if(oper == 'B'):
                    query = "INSERT INTO tickets(UserID, MovieID) VALUES ('"+str(id)+"', '"+str(id_query)+"')"
                    cursor = connection.cursor()
                    cursor.execute(query)
                    connection.commit() # Fixed bug where INSERT not possible
                    print("You're Movie was booked!!!")


            oper = input("") # Waiting Variable



### End FUNCTION DEFINITIONS
### Start Program
connection = create_server_connection("localhost", "admin", "admin", "CompProject") #Connect to DB



# print("Welcome to [INSERT NAME]")
while(True): #infinite loop
    print(time.ctime()) #TIME
    print("Choose your preferred option")
    if(role != None):
        print("Logged in as " + str(role))

    if(loginstatus == True): #Check if user is logged in
        print("1)View Available movies")

    if(loginstatus == False): #Check if user is logged in
        print("2)Login")

    else:
        print("2)Logout")

    if(role == "venueadmin" or role == "superadmin"):
        print("3)Add, edit, remove movies playing") #for Venueadmin, superadmin
    # if(role == "superadmin"): BUG
    #     print("4)Add, edit, remove users") #for superadmin
    print("5)Exit Program")

    if(loginstatus == False): # Check if user is logged in
        print("6)Sign up")
    oper = input("")

    #Check Input(oper value)
    if(oper == '1' and loginstatus == True):
        getMovielist()
        continue

    elif(oper == '2'):
        if(loginstatus == False):
            getLoginScreen(connection)
        else:
            getLogoutScreen()
    if(role == "venueadmin" and oper == '3'):
        getMovielist()
        continue #Show only venueadmin's venue movies with add, remove, edit privileges
    elif(role == "superadmin" and oper == '3'):
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
    #FYI no else block for random inputs, it's a loop
#End
