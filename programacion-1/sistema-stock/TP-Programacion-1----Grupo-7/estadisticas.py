from validaciones import validar_rango  
from consultas import (turnos_disponibles, estados_academicos_disponibles, mostrar_alumnos)


# funcion para ver las estadisticas de los alumnos
def procesamiento_estadistico(alumnos, turnos, estados_academicos):
    continuar = True

    while continuar:
        print()
        print("=== MENÚ DE ESTADÍSTICAS ===")
        print("1. Ver cantidad total de alumnos")
        print("2. Ver cantidad de alumnos por turno")
        print("3. Ver cantidad de alumnos por condición académica")
        print("4. Ver alumno con el mayor promedio general")
        print("5. Volver al menú principal")

        opcion = validar_rango(1, 5)
        print()

        # Para ver la cantidad total de alumnos registrados
        if (opcion == 1):
            if len(alumnos) == 0:
                print("No hay alumnos registrados.")
            else:
                print("Cantidad total de alumnos registrados:", len(alumnos))

        # Para ver la cantidad total de alumnos segun el turno
        elif (opcion == 2):
            if len(alumnos) == 0:
                print("No hay alumnos registrados.")
            else:
                turno_buscado = turnos_disponibles(turnos)
                contador_turno = 0
                for i in range(len(alumnos)):
                    if (alumnos[i][3] == turno_buscado):
                        contador_turno = contador_turno + 1
                print("Cantidad de alumnos en el turno", turno_buscado, ":", contador_turno)

        # Para ver la cantidad de alumnos segun condicion academica
        elif (opcion == 3):
            if (len(alumnos) == 0):
                print("No hay alumnos registrados.")
            else:
                condicion_buscada = estados_academicos_disponibles(estados_academicos)
                contador_condicion = 0
                for i in range(len(alumnos)):
                    if (alumnos[i][6] == condicion_buscada):
                        contador_condicion = contador_condicion + 1
                print("Cantidad de alumnos con condición", condicion_buscada, ":", contador_condicion)

        # Para ver el alumno con el mayor promedio
        elif (opcion == 4):
            if (len(alumnos) == 0):
                print("No hay alumnos registrados.")
            else:
                posicion_mayor = 0
                mayor_promedio = alumnos[0][5]

                # busca el promedio mas alto comparando elemento por elemento
                for i in range(1, len(alumnos)):
                    if (alumnos[i][5] > mayor_promedio):
                        mayor_promedio = alumnos[i][5]
                        posicion_mayor = i

                print("El promedio general más alto es:", mayor_promedio)
                print()
                print("Datos del alumno destacado:")
                mostrar_alumnos([alumnos[posicion_mayor]])

        # Salir del submenú de estadisticas
        elif (opcion == 5):
            continuar = False
            print("Volviendo al menú principal...")
