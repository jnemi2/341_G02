
upper = 0
lower = 0
symbols = 0

with open("texto.txt", "rt") as file:
    line = file.readline()
    while line != "":
        for char in line:
            if char.isupper():
                upper += 1
            elif char.islower():
                lower += 1
            else:
                symbols += 1
        line = file.readline()

print("The quantity of uppercase letters is ", upper)
print("The quantity of lowercase letters is ", lower)
print("The quantity of symbols is ", symbols)
