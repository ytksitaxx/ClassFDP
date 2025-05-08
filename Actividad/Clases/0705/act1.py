dinero = 0
bono = 0

print("----------¡Bienvenid@!----------\n"
      "-Ingresa el numero de opcion que corresponda a su decil-\n"
      "1. primer decil \n"
      "2. segundo decil \n"
      "3. tercer decil \n"
      "4. cuarto decil \n"
      "5. quinto decil \n"
      "6. sexto decil \n"
      "7. septimo decil \n"
      "8. octavo decil \n"
      "9. noveno decil \n"
      "10. decimo decil")
respuesta_decil = int(input("Ingrese el decil al que pertenece: "))
nota_total_medio = float(input("Coloque su promedio de la enseñanza media: "))

if nota_total_medio > 6.5 and (respuesta_decil == 1 or respuesta_decil == 2):
    dinero = 200000
elif nota_total_medio > 6.5 and (respuesta_decil == 4 or respuesta_decil == 4):
    dinero = 150000
elif (nota_total_medio > 5.5 and nota_total_medio <= 6.5) and (respuesta_decil == 1 or respuesta_decil == 2):
    dinero = 120000
elif (nota_total_medio > 5.5 and nota_total_medio <= 6.5) and (respuesta_decil == 3 or respuesta_decil == 4):
    dinero = 100000
else:
    print("")

if (respuesta_decil == 1 or respuesta_decil == 2 or respuesta_decil == 3):
    bono = 50000
    if nota_total_medio >= 6.0:
        bono + 30000
print("Su monto asignado es:", dinero + bono)