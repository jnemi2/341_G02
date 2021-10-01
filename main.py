import usermanager.auth as auth
import usermanager.log as log

username = input("Please, enter your username: ")

verified = auth.authenticate(username)
if not verified:
    for i in range(2, 0, -1):
        username = input(str(i) + " remaining attempts to authenticate. Username: ")
        verified = auth.authenticate(username)
        if verified:
            break
if verified:
    log.log(username)
    print("Registered")
else:
    print("Authentication failed")