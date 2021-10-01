

def authenticate(username):
    file = open("passwd.txt", "rt")
    line = file.readline()