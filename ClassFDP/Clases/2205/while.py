abrir_menu = False
print("1. Abrir Menú\n" \
    "2. Otra Cosa\n" \
    "3. Salir\n")

opcion_usuario = int(input())

def menu(opcion_elegida):
    if opcion_elegida == 1:
        print("Abrir el menú")
        global abrir_menu
        abrir_menu = True
    elif opcion_elegida == 2:
        print("Otra cosa")
    elif opcion_elegida == 3:
        print("Salimos")
    else:
        print("Elige una opcion valida")

menu(opcion_usuario)

while abrir_menu:
    print("Hacemos cositas")