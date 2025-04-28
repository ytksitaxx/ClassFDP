print("Por favor ingresa la palabra")
palabra = input()

nuevaPalabra = ""

for i in range(len(palabra)):
    print(palabra[(len(palabra)-1)-i])
    nuevaPalabra += palabra[(len(palabra)-1)-i]
    print("La nueva palabra es:", nuevaPalabra)

if nuevaPalabra == palabra:
    print("La palabra :", palabra, " es igual a la palabra ", nuevaPalabra)
else:
    print("La palabra :", palabra, " es distinta a la palabra ", nuevaPalabra)