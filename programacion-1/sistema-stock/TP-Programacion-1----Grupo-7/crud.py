from validaciones import (validar_codigo, validar_edad, validar_texto, validar_nota, validar_alumno, existe_codigo, validar_rango)
from consultas import (turnos_disponibles, estados_academicos_disponibles, mostrar_alumnos)
from rich.console import Console

console = Console()


# funcion para agregar un alumno y sus datos
def alta_alumno(alumnos, turnos, estados_academicos):
    print()
    print("=== ALTA DE ALUMNO ===")

    # va pidiendo los datos y usa otras funciones para validarlos
    if (len(alumnos) == 0):
        codigo = 101 # Código inicial predeterminado si la lista esta vacia
    else:
        codigo = (alumnos[len(alumnos) - 1][0]) + 1

    # Control para garantizar que el codigo autogenerado no este repetido
    while (existe_codigo(codigo, alumnos)):
        codigo = codigo + 1

    print("Código asignado automáticamente:", codigo)

    nombre = validar_texto("Nombre: ")
    apellido = validar_texto("Apellido: ")
    turno = turnos_disponibles(turnos)
    edad = validar_edad("Edad: ")
    print("Promedio General:")
    promedio = validar_nota()
    estado = estados_academicos_disponibles(estados_academicos)

    # agrega los datos del alumno a una lista
    nuevo_alumno = [codigo, nombre, apellido, turno, edad, promedio, estado]
    # agrega esa lista a la matriz
    alumnos.append(nuevo_alumno)

    print()
    console.print("[bold green]Alumno cargado con éxito.[/bold green]")
    # muestra como quedaron los datos del alumno ingresado
    print("Datos del nuevo alumno:")
    mostrar_alumnos([nuevo_alumno])

# =========================================================================


# funcion para modificar los datos de un alumno cargado
def modificar_registro(alumnos, turnos, estados_academicos):
    print()
    print("=== MODIFICAR REGISTRO ===")
    print("Ingrese el código del alumno que desea modificar.")
    # solo permite ingresar el codigo de un alumno existente
    codigo = validar_alumno(alumnos)

    # para buscar los datos del alumno
    posicion_alumno = 0
    posicion = 0
    while (posicion < len(alumnos)):
        if (alumnos[posicion][0] == codigo):
            posicion_alumno = posicion
        posicion = posicion + 1

    # bucle para q el usuario eliga q datos modificar hasta q quiera salir
    continuar = True
    while continuar:
        print()
        print("--- MENÚ DE MODIFICACIÓN ---")
        print("1. Modificar Nombre")
        print("2. Modificar Apellido")
        print("3. Modificar Turno")
        print("4. Modificar Edad")
        print("5. Modificar Promedio General")
        print("6. Modificar Estado Académico")
        print("7. Terminar y salir")

        print("¿Que dato desea modificar?")
        # el usuario elije cual dato quiere modificar y se valida el rango
        opcion = validar_rango(1, 7)
        print()

        # estos if son para que se modifiquen los datos segun q opcion eliguio
        if (opcion == 1):
            nuevo_nombre = validar_texto("Ingrese el nuevo nombre: ")
            alumnos[posicion_alumno][1] = nuevo_nombre
            print("Nombre modificado correctamente.")

        elif (opcion == 2):
            nuevo_apellido = validar_texto("Ingrese el nuevo apellido: ")
            alumnos[posicion_alumno][2] = nuevo_apellido
            print("Apellido modificado correctamente.")

        elif (opcion == 3):
            nuevo_turno = turnos_disponibles(turnos)
            alumnos[posicion_alumno][3] = nuevo_turno
            print("Turno modificado correctamente.")

        elif (opcion == 4):
            nueva_edad = validar_edad("Ingrese la nueva edad: ")
            alumnos[posicion_alumno][4] = nueva_edad
            print("Edad modificada correctamente.")

        elif (opcion == 5):
            print("Ingrese el nuevo promedio:")
            nuevo_promedio = validar_nota()
            alumnos[posicion_alumno][5] = nuevo_promedio
            print("Promedio modificado correctamente.")

        elif (opcion == 6):
            nuevo_estado = estados_academicos_disponibles(estados_academicos)
            alumnos[posicion_alumno][6] = nuevo_estado
            print("Estado académico modificado correctamente.")

        # continuar = False para salir del while ya q el usuario no quiere
        # modificar mas datos
        elif (opcion == 7):
            continuar = False
            print("Modificación finalizada.")

    # muestra al usuario los datos ya actualizados
    print()
    print("=== DATOS ACTUALIZADOS DEL ALUMNO ===")
    mostrar_alumnos([alumnos[posicion_alumno]])

# =========================================================================


# funcion para eliminar un alumno de la matriz
def eliminar_registro(alumnos):
    print()
    print("=== ELIMINAR REGISTRO ===")
    print("Ingrese el código del alumno que desea eliminar.")
    # solo permite ingresar el codigo de un alumno existente
    codigo = validar_alumno(alumnos)

    # para buscar la posicion del alumno en la lista
    posicion_alumno = 0
    posicion = 0
    while (posicion < len(alumnos)):
        if (alumnos[posicion][0] == codigo):
            posicion_alumno = posicion
        posicion = posicion + 1

    print()
    print("¿Desea eliminar los datos de este alumno?")
    print("1. Confirmar eliminación")
    print("2. Cancelar eliminación")
    opcion = validar_rango(1, 2)

    if (opcion == 1):
        # elimina al alumno de la lista usando pop
        alumnos.pop(posicion_alumno)
        console.print("[bold green]Alumno eliminado correctamente.[/bold green]")
        print()
        if (len(alumnos) > 0):
            print("NUEVA LISTA DE DATOS:")
            mostrar_alumnos(alumnos)
        else:
            console.print("[yellow]No quedan alumnos en el sistema.[/yellow]")
    else:
        console.print("[red]Eliminación cancelada.[/red]")
