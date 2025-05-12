# Programa que permita calcular los beneficios de los estudiantes
promedio = float(input("Ingresa tu promedio final "))
quintil = int(input("Ingresa el quintil de tu grupo familiar "))
vArancel = 1800000
matricula = 90000

if promedio > 6.0:
    if quintil in[1,2]:
        print("El valor del arancel es: ", vArancel*0.8)
        print("El valor de la matricula es: ", matricula*0.85)
    elif quintil == 3:
        print("El valor del arancel es: ", vArancel*0.85)
        print("El valor de la matricula es: ", matricula*0.85)
    else:
        print("El valor del arancel es: ", vArancel*0.8)
        print("El valor de la matricula es: ", matricula)
elif 5.0 < promedio <= 6.0:
    if promedio >= 5.5:
        if quintil in[1,2]:
            print("El valor del arancel es: ", vArancel*0.87)
            print("El valor de la matricula es: ", matricula*0.85)
        elif quintil == 3:
            print("El valor del arancel es: ", vArancel*0.9)
            print("El valor de la matricula es: ", matricula*0.85)
        else:
            print("El valor del arancel es: ", vArancel*0.9)
            print("El valor de la matricula es: ", matricula)
    elif promedio < 5.5:
        if quintil in[1,2]:
            print("El valor del arancel es: ", vArancel*0.87)
            print("El valor de la matricula es: ", matricula)
        else:
            print("El valor del arancel es: ", vArancel*0.9)
            print("El valor de la matricula es: ", matricula)
else:
    print("El valor del arancel es: ", vArancel)
    print("El valor de la matricula es: ", matricula)