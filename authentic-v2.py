def register():
    db = open("database.txt", "r")
    username = input("Create username:")
    password = input("Create password:")
    password1 = input("Confirm password:")
    d = []
    f = []
    for i in db:
        a,b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))

    if password != password1:
        print("Password don't match, restart")
        register()
    else:
        if len(password)<=6:
            print("Password too short, restart:")
            register()
        elif username in d:
           print("username exists")
           register()
        else:
           db = open("database.txt", "a")
           db.write(username+", "+password+"\n")
           print("Login successful!")

def access():
    db = open("database.txt", "r")
    username = input("Enter your username:")
    password = input("Enter your password:")

    if not len(username or password)<1:
        d = []
        f = []
        for i in db:
            a, b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))

        try:
            if data[username]:
                try:
                    if password == data[username]:
                        print("Login success")
                        print("Hi,", username)
                    else:
                        print("Password or username incorrect")
                except:
                    print("Incorrect password or username")
            else:
                print("Username or password doesn't exist")
        except:
            print("Username or password doesn't exist")

    else:
        print("Please enter a value")

def home(option=None):
    option = input("Login | Signup:")
    if option == "Login":
        access()
    elif option == "Signup":
        register()
    else:
        print("Please enter an option")
home()