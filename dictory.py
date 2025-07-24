credentials = {
    "username": "B96227@students.ucu .ac.ug",
    "password": "1234r",
}

print(credentials["username"])

print("log in system")
username = input("Enter your username:")
password = input("Enter your password:")

if username == credentials["username"] and password == credentials["password"]:
    print("Log in successful")
else:
    print("lnvalide credential, please try again")


credentials ={
    "username": "B96227@students.ucu .ac.ug",
    "password": "1234r",
}
print(f"Initial dictionary: {credentials}")
credentials["password"] = "pops_sky"

print(f"update dictionary: {credentials}")
