import random

def juego_adivinanza():
    print("--Bienvenido usuario al juego de adivinanza--")
    print("A continuacion ingresa dos numeros que representen el limite del numero aleatorio")
    while True:
        try:
            limite_inferior = int(input("Ingresa el limite inferior: "))
            limite_superior = int(input("Ingresa el limite superior: "))
            if limite_inferior < limite_superior:
                break
            else:
                print("El numero inferior debe ser menor al superior, intente nuevamente")
        except ValueError:
            print("Ingresa un dato valido")

    # Generar numero aleatorio
    numero_aleatorio = random.randint(limite_inferior,limite_superior)
    print("Se ha generado un numero aleatorio entre el", limite_inferior,"y", limite_superior)

    # Intentos del usuario
    for intento in range(1,4):
        try:
            respuesta = int(input("Intento N°", intento,"Ingresa tu numero"))
            if respuesta == numero_aleatorio:
                print("Felicidades acertaste el numero")
            elif respuesta < numero_aleatorio:
                print("El numero aleatorio es MAYOR")
            else:
                print("El numero aleatorio es MENOR")
            
            if intento == 2:
                print()
        except ValueError:
            print("Ingresa un dato valido")
    print("Fallaste.. el numero correcto era:", numero_aleatorio)

juego_adivinanza()