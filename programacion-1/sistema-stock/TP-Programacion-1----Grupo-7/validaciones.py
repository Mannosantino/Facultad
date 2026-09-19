
# funcion para cuando se le pida el codigo del alumno al usuario
# solo pueda ingresar numeros, no acepta vacios ni letras
def validar_codigo():
    codigo = input("Ingrese el código del alumno: ")

    # por si el usuario ingreso vacio
    while (codigo == ""):
        print("El código no puede estar vacío.")
        codigo = input("Ingrese el código del alumno: ")

    valido = True
    posicion = 0

    # para validar que sea solo numeros, y sino entra en el siguiente while
    while (posicion < len(codigo)):
        if ((codigo[posicion] < "0") or (codigo[posicion] > "9")):
            valido = False
        posicion = posicion + 1

    # vuelve a pedir el codigo (por si antes ingreso letras o vacio)
    while (not valido):
        print("El código debe estar conformado solo por números.")
        codigo = input("Ingrese el código del alumno: ")

        while (codigo == ""):
            print("El código no puede estar vacío.")
            codigo = input("Ingrese el código del alumno: ")

        valido = True
        posicion = 0
        while (posicion < len(codigo)):
            if ((codigo[posicion] < "0") or (codigo[posicion] > "9")):
                valido = False
            posicion = posicion + 1

    return int(codigo)

# =========================================================================


# funcion para pedir edad valida, que no sea texto, ni menor a cero, ni vacio
def validar_edad(mensaje):
    valor = input(mensaje)
    numero = True

    # si el usuario ingresa vacio o texto "numero = Falso" asi
    # entra en el while
    if (valor == ""):
        numero = False
    else:
        for caracter in valor:
            if (caracter not in "0123456789"):
                numero = False

    # si el usuario no ingresa un número(o sea vacio o texto) o si el numero
    # es menor/igual a cero, le vuelve a pedir la edad hasta q sea correcto
    while ((not numero) or (int(valor) <= 0)):
        print("El número debe ser mayor a cero, no contener letras ni estar vacío.")
        valor = input(mensaje)
        numero = True
        if (valor == ""):
            numero = False
        else:
            for caracter in valor:
                if (caracter not in "0123456789"):
                    numero = False

    return int(valor)

# =========================================================================


# funcion para validar textos, que el usuario no ingrese numeros ni vacio
def validar_texto(mensaje):
    texto = input(mensaje)
    valido = True
    
    # Cadena con todas las letras permitidas (incluye tildes, eñes y espacio)
    permitidos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúÁÉÍÓÚñÑ "

    # si el usuario ingresa vacio o un numero
    # "valido = Falso" asi entra en el while
    if (texto == ""):
        valido = False
    else:
        for caracter in texto:
            if (caracter not in permitidos):
                valido = False

    # si el usuario no ingresa un texto (o sea vacio o numeros) le vuelve a
    # pedir el texto hasta q sea correcto
    while (not valido):
        print("Ingrese solamente texto y no deje el campo vacío.")
        texto = input(mensaje)
        valido = True
        if (texto == ""):
            valido = False
        else:
            for caracter in texto:
                if (caracter not in permitidos):
                    valido = False

    return texto

# =========================================================================


# funcion para validar q el usuario ingreso un numero entre 2 valores
def validar_rango(minimo, maximo):
    print("Ingrese una opción entre", minimo, "y", maximo, ": ", end="")
    numero = input()
    es_numero = True

    # para validar si el usuario no ingreso vacio ni texto
    if (numero == ""):
        es_numero = False
    else:
        for caracter in numero:
            if (caracter not in "0123456789"):
                es_numero = False

    # si no se ingreso un numero valido (osea vacio o texto) "rango = False"
    # para entrar en el while
    rango = True
    if (not es_numero):
        rango = False
    # si el usuario si ingreso un numero pero esta fuera del rango
    # "rango = False" para entrar en el while
    elif ((int(numero) < minimo) or (int(numero) > maximo)):
        rango = False

    # hasta q el usuario no ingrese un número válido (ni texto ni vacio) o un
    # numero q esté fuera de rango, se va a volver a pedir la opcion
    while (not rango):
        print("La opción debe ser un número entre", minimo, "y", maximo, ": ", end="")
        numero = input()
        es_numero = True
        if (numero == ""):
            es_numero = False
        else:
            for caracter in numero:
                if (caracter not in "0123456789"):
                    es_numero = False

        rango = True
        if (not es_numero):
            rango = False
        elif ((int(numero) < minimo) or (int(numero) > maximo)):
            rango = False

    return int(numero)

# =========================================================================


# funcion para validar q el usuario ingreso una nota correspondiente
def validar_nota():
    print("Ingrese una nota entre 0 y 10: ", end="")
    numero = input()
    es_numero = True

    # para validar si el usuario no ingreso vacio ni texto
    if (numero == ""):
        es_numero = False
    else:
        puntos = 0 # para contar los puntos del numero
        for caracter in numero:
            if (caracter not in "0123456789."):
                es_numero = False
            if (caracter == "."):
                puntos = puntos + 1
        # no acepta el numero si tiene mas de 1 punto
        if (puntos > 1):
            es_numero = False

    # si no se ingreso un numero valido (osea vacio o texto) "rango = False"
    # para entrar en el while
    rango = True
    if (not es_numero):
        rango = False
    # si el usuario si ingreso un numero pero esta fuera del rango
    # "rango = False" para entrar en el while
    elif ((float(numero) < 0) or (float(numero) > 10)):
        rango = False

    # hasta q el usuario no ingrese un número válido (ni texto ni vacio) o un
    # numero q esté fuera de rango, se va a volver a pedir la opcion
    while (not rango):
        print("La nota debe ser un número válido entre 0 y 10: ", end="")
        numero = input()
        es_numero = True
        if (numero == ""):
            es_numero = False
        else:
            puntos = 0
            for caracter in numero:
                if (caracter not in "0123456789."):
                    es_numero = False
                if (caracter == "."):
                    puntos = puntos + 1
            if (puntos > 1):
                es_numero = False

        rango = True
        if (not es_numero):
            rango = False
        elif ((float(numero) < 0) or (float(numero) > 10)):
            rango = False

    return float(numero)

# =========================================================================


# funcion para validar q un alumno existe
def validar_alumno(alumnos):
    encontrado = False

    while (not encontrado):
        codigo = validar_codigo()
        posicion = 0

        # recorre la matriz buscando si coincide el codigo ingresado
        while (posicion < len(alumnos)):
            if (int(codigo) == int(alumnos[posicion][0])):
                encontrado = True
                print()
                print("--- Datos del alumno encontrado ---")
                print("Código:", alumnos[posicion][0])
                print("Nombre:", alumnos[posicion][1])
                print("Apellido:", alumnos[posicion][2])
                print("Turno:", alumnos[posicion][3])
                print("Edad:", alumnos[posicion][4])
                print("Promedio General:", alumnos[posicion][5])
                print("Estado Académico:", alumnos[posicion][6])
                return int(codigo)

            posicion = posicion + 1

        print("El código no pertenece a ningún alumno. Intente nuevamente.")

# =========================================================================


# funcion para verificar si un codigo ya existe en la matriz
def existe_codigo(codigo, alumnos):
    posicion = 0
    encontrado = False

    while ((posicion < len(alumnos)) and (not encontrado)):
        if (int(alumnos[posicion][0]) == int(codigo)):
            encontrado = True
        posicion = posicion + 1

    return encontrado


