users = [
    {
        "username": "games",
        "password": "Ilovegames"
    },
    {
        "username": "dogs",
        "password": "Ilovedogs"
    },
    {
        "username": "python",
        "password": "Ilovepython"
    },
]

username = input("Enter username:")
password = input("Enter password:")

logged_user = None


for user in users:
    if user["username"] == username and user["password"] == password:
        print("login successful")
        logged_user = user
        break

if logged_user is not None:
    print("successful login")
else:
    print("unsuccessful login")