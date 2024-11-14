# Account creation?
# I don't know what I'm doing...
User_Pass = {}
loggedIn = False

def login(username, password):
    global loggedIn
    if username in User_Pass and User_Pass[username] == password:
        print("logged in")
        loggedIn = True
    else:
        print("Incorrect Username or Password")
def signUp(newUser, newPass):
    if newUser in User_Pass:
        print("Username already in Use!")
    else:
        User_Pass[newUser] = newPass
        print("Account Created!")
def createAcc():
    print("Create your account")
    action = input("Login or Sign up?\nType Answer Here: ")

    if action.lower() == "login":
        x = input("Username\n")
        y = input("Password\n")
        login(x,y)
    elif action.lower() == "sign up":
        x = input("Username\n")
        y = input("Password\n")
        signUp(x,y)
    elif action.lower() == "check":
        print(f"Accounts: {User_Pass} ")
    else:
        print("Invalid Answer")


while not loggedIn:
    createAcc()

loop = True

while loop:
    print("Welcome to the Calculator!")
    input("")
