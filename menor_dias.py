def paciente_menor_internacion(matriz):
    if len(matriz) == 0:
        print("No hay pacientes cargados.")
        return
    paciente_min = matriz[0]
    for i in range(1, len(matriz)):
        if matriz[i][4] < paciente_min[4]:
            paciente_min = matriz[i]
    print("\nPaciente con menos días de internación:")
    print(f"Historia Clínica: {paciente_min[0]}, Nombre: {paciente_min[1]}, Edad: {paciente_min[2]}, Diagnóstico: {paciente_min[3]}, Días: {paciente_min[4]}")