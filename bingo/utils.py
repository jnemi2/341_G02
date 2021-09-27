import random


def generar_carton():
    card = random.sample(range(100), 25)
    card.sort()
    return card
