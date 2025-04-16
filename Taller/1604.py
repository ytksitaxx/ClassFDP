nombre = "Sebastian"
edad = 18
estatura = 1.75
print(nombre,edad,estatura)
AñoNacimiento = 2006
AñoActual = 2025
print(AñoActual - AñoNacimiento)

Precio = 5990
Descuento = 0.85
PrecioFinal = float(Precio * Descuento)
print(PrecioFinal)
edad2 = 18
meses = edad * 12
dias = meses * 30
horas = dias * 24
print(edad,meses,dias,horas)

nota1 = 6.5
nota2 = 3.4
nota3 = 5.2
promedio = int(nota1 + nota2 + nota3)/3
if promedio >= 4.0:
    print("Has aprobado")
else:
    print("Has desaprobado")
    
#Rectangulo con base 5 y altura 3
Area = 5 * 3
Perimetro = (5*2)+(3*2)
print(Area,Perimetro)
resultado = 15 ** 2 < 200
print("¿15 elevado a 2 es mayor a 200?", resultado)