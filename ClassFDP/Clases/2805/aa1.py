def esPrimo():
    while True:
        try:
            numeroU = int(input("Ingrese cuantos numero primos desea ingresar: "))
            if 0 < numeroU:
                break
            else:
                print("Por favor ingresa un numero positivo")
        except ValueError:
            print("Por favor ingresa un numero entero")

    primos = 0
    noPrimos = 0
    
    # Ingreso de datos
    for i in range(numeroU):
        while numero < 1:
            try:
                numero = int(input("Ingresa el numero: "))
            except ValueError:
                print("Por favor ingresa un numero entero")
        if numero % 2 != 0:
            print("Es primo")
            primos += 1
        elif numero == 2:
            print("Es primo")
            primos += 1
        elif numero < 2:
            print("No es primo")
            noPrimos += 1
        else:
            print("No es primo")
            noPrimos += 1

    # Resultados
    print("-----RESULTADOS-----")
    print("Total numero primos:", primos)
    print("Total no primos:", noPrimos)
esPrimo()