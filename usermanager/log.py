import datetime


def log(username, filename="fichadas.txt"):
    file = open(filename, "at")
    register = datetime.datetime.now()
    file.write(register + " - " + username + "\n")
    file.close()
