def contar_pacientes_mayores_5(matriz):
    contador = 0
    for paciente in matriz:
        if paciente[4] > 5:
            contador += 1
    print(f"\nCantidad de pacientes con más de 5 días de internación: {contador}")