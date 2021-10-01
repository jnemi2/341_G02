import os


def authenticate(username, password):
    if os.path.isfile("passwd.txt"):
        file = open("passwd.txt", "rt")
        line = file.readline().strip()
        while line != "" and line != (username + ":" + password):
            line = file.readline().strip()
        return line == (username + ":" + password)
    else:
        print("Error. There are no registered users")
        return False
