def calculadora_beneficios():
    valorbase_arancel = 1800000
    valorbase_matricula = 90000
    
    try:
        while True:
            try:
                promedio_estudiante = float(input("Ingresa el promedio final con el que egresaste del colegio o liceo: "))
                quintil_estudiante = int(input("Ingresa el quintil socioeconomico al que pertenece tu grupo familiar: "))
                if 0 <= promedio_estudiante <= 7.0 and 1 <= quintil_estudiante <= 5:
                    break
                else:
                    print("Datos no validos, intenta nuevamente")
            except ValueError:
                print("Ingresa un numero valido")
        
        # Descuento Arancel
        descuento_arancel = 0
        if promedio_estudiante > 6.0:
            if quintil_estudiante in[1,2]:
                descuento_arancel = 0.20
            elif quintil_estudiante in[3,4]:
                descuento_arancel = 0.15
        elif promedio_estudiante > 5.0:
            if quintil_estudiante in[1,2]:
                descuento_arancel = 0.13
            elif quintil_estudiante in[3,4]:
                descuento_arancel = 0.10
        
        # Descuento Matricula
        descuento_matricula = 0
        if quintil_estudiante in[1,2,3]:
            descuento_matricula = 0.10
        if promedio_estudiante > 5.5:
            descuento_matricula += 0.05
        
        # Valores Finales
        valorfinal_arancel = valorbase_arancel*(1 - descuento_arancel)
        valorfinal_matricula = valorbase_matricula*(1 - descuento_matricula)
        print("-----RESULTADOS-----")
        print("Valor Final Arancel:", valorfinal_arancel)
        print("Valor Final Matricula:", valorfinal_matricula)
    except ValueError:
        print("Datos no validos")

calculadora_beneficios()