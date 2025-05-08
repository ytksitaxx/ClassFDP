intentos = 0

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

if num1 > num2:
    print("Error: el primer numero debe ser menor al segundo")
    num1 = int(input("ingresa nuevamente el primer numero: "))

puntoMedio = (num1 + num2) /2

ajusteNumAleatorio = (num2 - num1)*0.2

numAleatorio = (puntoMedio + ajusteNumAleatorio)
print("-----El juego está preparado para iniciar-----\n"
      "---Intente adivinar el numero magico---'\n")
numeroParaAdivinar = int(input("Ingrese su numero para adivinar"))
if numAleatorio != numeroParaAdivinar:
    intentos +=1
    if numeroParaAdivinar > numAleatorio:
        print("El numero que ingresaste es mayor que el numero que debes adivinar")
    else:
        print("El numero que ingresaste es menor que el numero que debes adivinar")
elif numAleatorio != numeroParaAdivinar and intentos == 1:
    if numeroParaAdivinar > numAleatorio:
        print("El numero que ingresaste es mayor que el numero que debes adivinar")
    else:
        print("El numero que ingresaste es menor que el numero que debes adivinar")