# programa que reciba 3 números por teclado, uno por uno, y diga: cuántos números son pares y cuantos impares.
numero = 0
suma = 0
pares = 0
impares = 0

for i in range(3):
    numero = int(input("Ingresa el numero: "))
    if numero % 2 == 0:
        pares +=1
    else:
        impares += 1
    suma += numero
    
print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
if suma < 100:
    print("La suma es menor a 100")
else:
    print("La suma es mayor a 100")

if suma % 2 == 0:
    print("La suma es par")
else:
    print("La suam es imapar")