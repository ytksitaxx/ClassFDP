def calculadora_edad():
    try:
        edad = int(input("Ingresa tu edad: "))
        añoNacimiento = 2025 - edad
        if 0 < edad <= 110:
            print("El año en que naciste es:",añoNacimiento)
        else:
            print("Edad ingresada invalida")
    except ValueError:
        print("Numero invalido")


calculadora_edad()