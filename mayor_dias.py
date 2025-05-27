def paciente_mayor_internacion(matriz):
    if len(matriz) == 0:
        print("No hay pacientes cargados.")
        return
    paciente_max = matriz[0]
    for i in range(1, len(matriz)):
        if matriz[i][4] > paciente_max[4]:
            paciente_max = matriz[i]
    print("\nPaciente con más días de internación:")
    print(f"Historia Clínica: {paciente_max[0]}, Nombre: {paciente_max[1]}, Edad: {paciente_max[2]}, Diagnóstico: {paciente_max[3]}, Días: {paciente_max[4]}")