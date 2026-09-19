def cargarUsuario():
    
    while True:
        try:

            nombreUsuario = input("Ingrese el nombre de usuario(sin espacíos): ").strip()
            if not nombreUsuario.isalpha():
                raise ValueError
            break

        except ValueError:
            print("Error: el nombre debe contener unicamente letras")    

    return nombreUsuario

def cargarContraseña():
    while True:
            try:

                contraseñaUsuario = input("Ingrese el nombre de usuario(sin espacíos) o enter para finalizar: ")
                if not contraseñaUsuario.isalnum() or " " in contraseñaUsuario:
                    raise ValueError
                break

            except ValueError:
                print("Error: la contraseña debe contener letras y numeros sin espacios")    

    return contraseñaUsuario


def validarUsuario(diccionarioUsuarios):
    try:
        archivoUsuarios= open('usuarios.csv', 'wt', encoding='UTF-8')

    except (FileNotFoundError,IOError) as error_1:
        print("Error: no se puedo abrir el archivo.\n",error_1)

    else:

        for linea in archivoUsuarios:

            usr, ctr = linea.strip().split(';')

        while True:

            
            usuario= cargarUsuario()

            if usuario == "":
                break
            else:
                contraseña= cargarContraseña()

                if usuario not in diccionarioUsuarios:
                    diccionarioUsuarios[usuario]: 







