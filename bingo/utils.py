import random


def generar_carton():
    card = random.sample(range(100), 25)
    card.sort()
    return card

def imprimir_carton(card):
    for i in range(len(card)):
        if card[i] <= 9:
            print("0" + str(card[i]), end=" ")
        else:
            print(str(card[i]), end=" ")
        if ((i+1) % 5) == 0:
            print()
    print()
