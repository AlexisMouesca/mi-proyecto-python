"""
Modulo que contiene la funcion cargar_pacientes.
"""
from herramientas import es_entero

def cargar_pacientes(matriz, inicio, cantidad):
    """
    Carga pacientes en una matriz.

    La carga de pacientes se realizar  solicitando los datos por teclado. Se
    solicitar  el n mero de historia cl nica, el nombre, la edad, el diagn stico y
    la cantidad de d as de internaci n. La edad y la cantidad de d as se
    verificar n para asegurarse de que sean n meros.

    Args:
        matriz (list): La matriz donde se cargar n los pacientes.
        inicio (int): La posici n inicial en la matriz donde se cargar n los
            pacientes.
        cantidad (int): La cantidad de pacientes a cargar.
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
