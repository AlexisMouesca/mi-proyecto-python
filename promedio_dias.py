def promedio_internacion(matriz):
    if len(matriz) == 0:
        print("No hay pacientes cargados.")
        return
    total = 0
    for paciente in matriz:
        total += paciente[4]
    promedio = total // len(matriz)
    print(f"\nPromedio de días de internación: {promedio}")