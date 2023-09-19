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
    print(data)

    if password != password1:
        print("Password don't match, restart")
        register()
    else:
        if len(password)<=6:
            print("Password too short, restart:")
            register()
       # elif username in d:
        #    print("username exists")
         #   register()
        else:
           # db = open("database.txt", "a")
           # db.write(username+", "+password+"\n")
            print("Login successful!")
register()

def access():
    pass