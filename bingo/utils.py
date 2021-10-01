import random


def generar_carton():
    card = random.sample(range(100), 25)
    card.sort()
    return card

def format_card(card):
    text = ""
    for i in range(len(card)):
        if card[i] <= 9:
            text = text + "0" + str(card[i]) + " "
        else:
            text = text + str(card[i]) + " "
        if ((i+1) % 5) == 0:
            text = text + "\n"
    return text

def imprimir_carton(card):
    print(format_card(card))

def grabar_carton(card, filename="carton"):
    filename = filename + ".txt"
    file = open(filename, "wt")
    file.write(format_card(card))
    file.close()
