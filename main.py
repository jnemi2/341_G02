import usermanager.auth as auth
import usermanager.log as log

username = input("Please, enter your username: ")
password = input("Please, enter your password: ")
verified = auth.authenticate(username, password)
if not verified:
    for i in range(2, 0, -1):
        print(str(i) + " remaining attempts to authenticate.")
        username = input("Username: ")
        password = input("Password: ")
        verified = auth.authenticate(username, password)
        if verified:
            break
if verified:
    log.log(username)
    print("Registered")
else:
    print("Authentication failed")