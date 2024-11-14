User_Pass = {}
loggedIn = False
loop = True

def login(username, password):
    global loggedIn
    if username in User_Pass and User_Pass[username] == password:
        print("Logged in successfully!")
        loggedIn = True
    else:
        print("Incorrect Username or Password")

def signUp(newUser, newPass):
    if newUser in User_Pass:
        print("Username already in use!")
    else:
        User_Pass[newUser] = newPass
        print("Account created successfully!")

def createAcc():
    print("Create your account")
    action = input("Login or Sign up?\nType Answer Here: ")

    if action.lower() == "login":
        x = input("Username: ")
        y = input("Password: ")
        login(x, y)
    elif action.lower() == "sign up":
        x = input("Choose a Username: ")
        y = input("Choose a Password: ")
        signUp(x, y)
    elif action.lower() == "check":
        print(f"Accounts: {User_Pass}")
    else:
        print("Invalid Answer")
