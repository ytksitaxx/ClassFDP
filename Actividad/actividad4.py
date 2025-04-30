# Aritmética y Conversor de Unidades
print("------Bienvenido al sistema------")
print("¿Que opcion desea realizar?")
opcion = int(input("1. Convertir de kilómetros a millas\n"
                "2. Convertir de millas a kilómetros\n"
                "3. Convertir de grados Celsius a Fahrenheit\n"
                "4. Convertir de grados Fahrenheit a Celsius\n"))

if opcion == 1:
    numero = float(input("Ingresa el numero a convertir "))
    if numero < 0:
        print("No puedes ingresar un numero negativo")
    else: resultado = numero*0.621371
    print(numero, "kilometros son:", resultado, "millas")

elif opcion == 2:
    numero = float(input("Ingresa el numero a convertir "))
    if numero < 0:
        print("No puedes ingresar un numero negativo")
    else: resultado = numero/0.621371
    print(numero, "millas son:", resultado, "kilometros")

elif opcion == 3:
    numero = float(input("Ingresa la temperatura a convertir "))
    resultado = numero*9/4+32
    print(numero, "grados Celsius son:", resultado, "grados Fahrenheit")

elif opcion == 4:
    numero = float(input("Ingresa la temperatura a convertir "))
    resultado = (numero-32)*5/9
    print(numero, "grados Fahrenheit son:", resultado, "grados Celsius")
    if numero > 25:
        print("La temperatura es: Caliente")
    elif 15 <= numero <= 25:
        print("La temperatura es: Ambiente")
    else:
        print("La temperatura es: Bajo cero")
else:
    print("Elige una opcion valida")