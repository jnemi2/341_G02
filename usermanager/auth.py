import os


def authenticate(username):
    if os.path.isfile("passwd.txt"):
        file = open("passwd.txt", "rt")
        line = file.readline().strip()
        while line != "" and line.split(":")[0] != username:
            line = file.readline().strip()
        return line.split(":")[0] == username
    else:
        print("Error. There are no registered users")
        return False
