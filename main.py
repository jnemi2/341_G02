import bingo.utils as bingo

# card = bingo.generar_carton()
# bingo.imprimir_carton(card)
# bingo.grabar_carton(card)

def select_option():
    option = input("Ingrese una opcion: ")
    while option not in ["1", "2", "3"]:
        option = input("Error. Ingrese una opcion: ")
    return option

print("1) Generar e imprimir un cartón\n"
      "2) Generar y grabar un cartón\n"
      "3) Salir\n")
option = select_option()
while option != "3":
    if option == "1":
        bingo.imprimir_carton(bingo.generar_carton())
    else:
        file_name = input("Ingrese el nombre del archivo (sin extension .txt): ")
        card = bingo.generar_carton()
        bingo.grabar_carton(card, filename=file_name)
        print("Exito al guardar el carton en '" + file_name + ".txt'")
        bingo.imprimir_carton(card)
    print("1) Generar e imprimir un cartón\n"
          "2) Generar y grabar un cartón\n"
          "3) Salir\n")
    option = select_option()

print("Fin del programa")
