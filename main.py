# Start
print("Welcome to [INSERT NAME]")
while(True): #infinite loop
    print("Choose your preferred option") #TODO add conditional for user role
    print("1)View Available movies")
    print("2)Login") #TODO add login functionality
    print("3)Add, edit, remove movies playing") #for Venueadmin, superadmin
    print("4)Add, edit, remove users") #for superadmin
    oper = int(input("")) #TODO Add conditional for user role
    if(oper == 1):
        getMovielist() #TODO def getmovielist
    elif(oper == 2):
        getLoginScreen() #TODO def getloginscreen
    #TODO Add conditional for oper based on user role
    else:
        print("Wrong Choice, try again")
        continue
