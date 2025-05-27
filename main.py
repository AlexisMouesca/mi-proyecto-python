"""
Modulo principal. Contiene la funcion principal que muestra el menu y permite al
usuario interactuar."""
from menu import mostrar_menu
from cargar import cargar_pacientes
from mostrar import mostrar_pacientes
from buscar import buscar_paciente
from ordenar import ordenar_pacientes
from mayor_dias import paciente_mayor_internacion
from menor_dias import paciente_menor_internacion
from contar_mayores_5 import contar_pacientes_mayores_5
from promedio_dias import promedio_internacion
from herramientas import es_entero

"""
Constante que establece la cantidad maxima de pacientes que se pueden cargar.
"""
MAX_PACIENTES = 100
pacientes = [[0, "", 0, "", 0] for _ in range(MAX_PACIENTES)]

def iniciar(cantidad_actual):
    """
    Funcion principal del programa. Muestra el menu de opciones y
    permite al usuario interactuar con el programa. La funcion
    utiliza un bucle while para mostrar el menu y procesar las
    opciones hasta que el usuario decida salir del programa.
    """
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            cantidad_input = input("Cuantos pacientes desea ingresar?: ")
            if es_entero(cantidad_input):
                cantidad = int(cantidad_input)
                if cantidad <= 0 or cantidad_actual[0] + cantidad > MAX_PACIENTES:
                    print("Cantidad invalida.")
                else:
                    cargar_pacientes(pacientes, cantidad_actual[0], cantidad)
                    cantidad_actual[0] += cantidad
            else:
                print("Ingrese un numero valido.")
        elif opcion == "2":
            if cantidad_actual[0] == 0:
                print("No hay pacientes cargados.")
            else:
                mostrar_pacientes(pacientes[:cantidad_actual[0]])
        elif opcion == "3":
            if cantidad_actual[0] == 0:
                print("No hay pacientes cargados.")
            else:
                numero_hc = input("Ingrese N° de historia clinica: ")
                if es_entero(numero_hc):
                    buscar_paciente(pacientes[:cantidad_actual[0]], int(numero_hc))
                else:
                    print("Numero invalido.")
        elif opcion == "4":
            if cantidad_actual[0] == 0:
                print("No hay pacientes cargados.")
            else:
                ordenar_pacientes(pacientes[:cantidad_actual[0]])
        elif opcion == "5":
            paciente_mayor_internacion(pacientes[:cantidad_actual[0]])
        elif opcion == "6":
            paciente_menor_internacion(pacientes[:cantidad_actual[0]])
        elif opcion == "7":
            contar_pacientes_mayores_5(pacientes[:cantidad_actual[0]])
        elif opcion == "8":
            promedio_internacion(pacientes[:cantidad_actual[0]])
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción invalida.")

"""
Llamada a la funcion principal. Inicia el programa.
"""
cantidad_actual = [0]
iniciar(cantidad_actual)