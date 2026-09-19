from datos import (alumnos, turnos, estados_academicos)  
from menu import menu_principal  
from crud import (alta_alumno, modificar_registro, eliminar_registro)  
from consultas import (buscar_registro, buscar_por_turno, mostrar_alumnos)
from estadisticas import procesamiento_estadistico


ejecutando = True

# bucle principal del programa
while ejecutando:
    opcion = menu_principal()

    if (opcion == 1):
        alta_alumno(alumnos, turnos, estados_academicos)

    elif (opcion == 2):
        if (len(alumnos) == 0):
            print("No hay alumnos registrados.")
        else:
            buscar_registro(alumnos)

    elif (opcion == 3):
        if (len(alumnos) == 0):
            print("No hay alumnos registrados.")
        else:
            modificar_registro(alumnos, turnos, estados_academicos)

    elif (opcion == 4):
        if (len(alumnos) == 0):
            print("No hay alumnos registrados.")
        else:
            eliminar_registro(alumnos)

    elif (opcion == 5):
        if (len(alumnos) == 0):
            print("No hay alumnos registrados.")
        else:
            print()
            print("=== REGISTRO DE ALUMNOS ===")
            mostrar_alumnos(alumnos)

    elif (opcion == 6):
        if (len(alumnos) == 0):
            print("No hay alumnos registrados.")
        else:
            buscar_por_turno(alumnos, turnos)

    elif (opcion == 7):
        procesamiento_estadistico(alumnos, turnos, estados_academicos)

    elif (opcion == 8):
        ejecutando = False
        print()
        print("Gracias por utilizar el Sistema de Gestión Académica.")
