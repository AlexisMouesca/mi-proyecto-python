from mostrar import mostrar_pacientes

def ordenar_pacientes(matriz):
    n = len(matriz)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if matriz[j][0] > matriz[j + 1][0]:
                temp = matriz[j]
                matriz[j] = matriz[j + 1]
                matriz[j + 1] = temp
    print("\nPacientes ordenados por N° de historia clínica:")
    mostrar_pacientes(matriz)