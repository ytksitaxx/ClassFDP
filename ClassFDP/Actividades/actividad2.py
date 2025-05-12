# Constantes y Calculadora de Descuentos
descestu = 0.15
descfre = 0.10

precio = int(input("Ingresa el valor "))
es = input("¿Eres Estudiante? ")
fr = input("¿Eres Cliente Frecuente? ")

if es == "si":
    print("Precio original: ", precio, "Descuento: ", descestu, "Precio Final :", precio-(precio*descestu))
elif fr == "si":
    print("Precio original: ", precio, "Descuento: ", descfre, "Precio Final :", precio-(precio*descfre))
else:
    print("Precio original: ", precio, "Descuento: ", "0", "Precio Final :", precio)