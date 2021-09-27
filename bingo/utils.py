import random


def generar_carton():
    card = []
    options = list(range(100))
    for num in range(25):
        card.append(options.pop(random.randint(0, len(options) - 1)))
        card.sort()
    return card
