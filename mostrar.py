def mostrar_pacientes(matriz):
    print("\n--- Lista de Pacientes ---")
    for paciente in matriz:
        print(f"Historia Clínica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnóstico: {paciente[3]}, Días de internación: {paciente[4]}")