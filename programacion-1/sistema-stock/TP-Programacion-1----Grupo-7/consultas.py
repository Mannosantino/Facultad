# importaciones
from validaciones import (validar_codigo, validar_rango)
from rich.console import Console
from rich.table import Table

# consola de rich, se usa en todo el archivo para imprimir con estilo
console = Console()

# =========================================================================


# funcion para calcular el ancho mas grande de una columna mas un margen
# (se deja comentada la lógica original: ya no se usa para las tablas,
# porque ahora rich calcula el ancho de las columnas automáticamente,
# pero la dejamos documentada por si la cátedra pregunta cómo se hacía)
def calcular_ancho_texto(datos, columna, encabezado):
    ancho = len(encabezado)
    for i in range(len(datos)):
        if (len(str(datos[i][columna])) > ancho):
            ancho = len(str(datos[i][columna]))
    return (ancho + 3)

# =========================================================================


# funcion para rellenar con espacios a la derecha y q quede todo alineado
# (idem: ya no se usa en mostrar_alumnos, queda documentada)
def completar_espacios(texto, ancho):
    cantidad_espacios = ancho - len(str(texto))
    return (str(texto) + (" " * cantidad_espacios))

# =========================================================================


# funcion para mostrarle al usuario los turnos disponibles
def turnos_disponibles(turnos):
    print()
    print("--- TURNOS DISPONIBLES ---")
    # imprime los turnos en la lista turnos
    for i in range(len(turnos)):
        # las opciones empiezan en 1 y no en 0
        print(i + 1, "-", turnos[i])

    # usamos la funcion validar_rango para q el usuario solo ingrese un
    # numero dentro del rango (ni vacio ni texto)
    opcion = validar_rango(1, len(turnos))
    return (turnos[opcion - 1])

# =========================================================================


# funcion para mostrarle al usuario los estados academicos disponibles
def estados_academicos_disponibles(estados_academicos):
    print()
    print("--- ESTADOS ACADÉMICOS ---")
    # imprime los estados en la lista estados_academicos
    for i in range(len(estados_academicos)):
        # las opciones empiezan en 1 y no en 0
        print(i + 1, "-", estados_academicos[i])

    # usamos la funcion validar_rango para q el usuario solo ingrese un
    # numero dentro del rango (ni vacio ni texto)
    opcion = validar_rango(1, len(estados_academicos))
    return (estados_academicos[opcion - 1])

# =========================================================================


# funcion para mostrar la tabla de alumnos emprolijada en columnas
# (ahora usando la librería rich para que se vea con bordes y colores)
def mostrar_alumnos(alumnos):
    # se crea una tabla de rich, con título y bordes
    tabla = Table(title="Alumnos", show_lines=True)

    # se agregan las columnas, cada una con un color distinto
    tabla.add_column("Código", style="cyan", justify="center")
    tabla.add_column("Nombre", style="white")
    tabla.add_column("Apellido", style="white")
    tabla.add_column("Turno", style="yellow")
    tabla.add_column("Edad", style="white", justify="center")
    tabla.add_column("Promedio General", style="green", justify="center")
    tabla.add_column("Estado Académico", style="magenta")

    # se agrega una fila por cada alumno
    for i in range(len(alumnos)):
        tabla.add_row(
            str(alumnos[i][0]),
            str(alumnos[i][1]),
            str(alumnos[i][2]),
            str(alumnos[i][3]),
            str(alumnos[i][4]),
            str(alumnos[i][5]),
            str(alumnos[i][6]),
        )

    console.print(tabla)

# =========================================================================


# funcion para buscar un alumno por su codigo y devuelva todos sus datos
def buscar_registro(alumnos):
    alumno_encontrado = []
    print()
    print("=== BUSCAR ALUMNO ===")
    # ingresa el codigo ya validado
    codigo = validar_codigo()
    encontrado = False
    posicion = 0

    # usamos len para no salirnos del largo de la lista, y usa while para
    # repetirlo hasta que se encuentre el alumno
    while ((posicion < len(alumnos)) and (not encontrado)):
        # si lo encuentra muestra los datos y devuelve true para parar el while
        if (int(codigo) == int(alumnos[posicion][0])):
            alumno_encontrado.append(alumnos[posicion])
            encontrado = True
            mostrar_alumnos(alumno_encontrado)
        # si no lo encuentra le suma 1 a la posicion para buscar en la
        # siguiente fila
        else:
            posicion = posicion + 1

    # si el while recorre toda la matriz y no lo encuentra encontrado sigue
    # siendo false y muestra q el alumno con ese codigo no existe
    if (not encontrado):
        print("El alumno con el código", codigo, "no existe.")

# =========================================================================


# funcion para buscar alumnos segun del turno que sean
def buscar_por_turno(alumnos, turnos):
    alumnos_coincidentes_turno = []

    print()
    print("=== CONSULTA POR TURNO ===")
    turno_buscado = turnos_disponibles(turnos)

    # recorre los alumnos y guarda los que coinciden con el turno elegido
    for i in range(len(alumnos)):
        if (alumnos[i][3] == turno_buscado):
            alumnos_coincidentes_turno.append(alumnos[i])

    if (len(alumnos_coincidentes_turno) == 0):
        print("No hay alumnos registrados en el turno", turno_buscado, ".")
    else:
        print()
        print("Alumnos del turno", turno_buscado, ":")
        mostrar_alumnos(alumnos_coincidentes_turno)
