"""
Modulo que contiene la funcion cargar_pacientes.
"""
from herramientas import es_entero

def cargar_pacientes(matriz, inicio, cantidad):
    """
    Carga pacientes en una matriz.

    La carga de pacientes se realiza solicitando los datos. Se
    solicita el N° de historia clinica, el nombre, la edad, el diagnostico y
    la cantidad de dias de internacion. La edad y la cantidad de dias se
    verificaron para asegurarse de que sean numeros.
    """
    for i in range(cantidad):
        print(f"\nPaciente {inicio + i + 1}:")
        
        while True:
            historia_clinica = input("Número de historia clínica: ")
            if es_entero(historia_clinica):
                historia_clinica = int(historia_clinica)
                break
            print("Número inválido.")

        nombre = input("Nombre: ")

        while True:
            edad = input("Edad: ")
            if es_entero(edad):
                edad = int(edad)
                break
            print("Edad inválida.")

        diagnostico = input("Diagnóstico: ")

        while True:
            dias = input("Días de internación: ")
            if es_entero(dias):
                dias = int(dias)
                break
            print("Número inválido.")

        matriz[inicio + i] = [historia_clinica, nombre, edad, diagnostico, dias]
