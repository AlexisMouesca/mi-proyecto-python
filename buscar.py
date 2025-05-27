def buscar_paciente(matriz, historia_clinica):
    encontrado = False
    for paciente in matriz:
        if paciente[0] == historia_clinica:
            print("\nPaciente encontrado:")
            print(f"Historia Clínica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnóstico: {paciente[3]}, Días: {paciente[4]}")
            encontrado = True
    if not encontrado:
        print("Paciente no encontrado.")