def numeros():
    while True:
        try:
            opcion = int(input("-----MENU PRINCIPAL-----\n"
                            "1.- Ingresar Numero.\n"
                            "2.- Mostrar Mayor.\n"
                            "3.- Mostrar Menor.\n"
                            "4.- Salir.\n"
                            "Selecciona una opcion: "))
            if 0 < opcion < 5:
                break
            else:
                print("### Ingresa una opcion valida ###\n")
        except ValueError:
            print("### Por favor ingresa un numero ###\n")
    
    # Opciones Usuario
    if opcion == 1:
        while True:
            try:
                numeroU = int(input("Ingresa tu numero: "))
                if 0 < numeroU <= 100:
                    print("Ingreso Valido")
                    numeros()
                else:
                    print("El numero debe estar entre 1 y 100")
            except ValueError:
                print("### Por favor ingresa un numero ###\n")
    elif opcion == 2:
        print("1243123")
        numeros()
    elif opcion == 3:
        print()
    else:
        exit()
numeros()