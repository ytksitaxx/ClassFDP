# calcular el promedio final de la asignatura de programación
ea1 = float(input("Ingresa la nota de la EA1: "))
ea2 = float(input("Ingresa la nota de la EA2: "))
ea3 = float(input("Ingresa la nota de la EA3: "))

pf = (ea1*0.3)+(ea2*0.4)+(ea3*0.3)
pfr = round(pf,1)
print("El promedio de presentación final es: ", pfr)

examen = float(input("Ingresa la nota del examen: "))
prom = (pfr*0.6) + (examen*0.4)
print("El promedio final es: ", round(prom,1))