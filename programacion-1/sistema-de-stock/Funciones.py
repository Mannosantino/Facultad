import random as r
# Carga una lista de productos sin repetidos.
def carga_datos():
    productos= [
        "Huevo","Harina","Azucar","Helado","Refresco","Pan","Leche","Chocolates","Pimienta","Galletas","Cerveza","Agua",
        "Arroz","Pasta","Tomate","Cebolla","Papa","Zanahoria","Turrones","Manzana","Banana","Naranja","Uva",
        "Carne de res","Pollo","Pescado","Queso","Yogurt","Mantequilla","Aceite de oliva","Sal","Huevo","Agua",
        "Pimienta", "Pimienta","Azucar","Café","Té","Jugo de naranja","Soda","Papas fritas","Nueces","Almendras",
        "Miel", "Carne de res","Mermelada","Helado","Pastel","Torta","Donas","Chicles","Caramelos","Pastillas",
        "Gomitas","Turrones","Bombones","Chupetines","Regalices","Carne Congelada","Queso","Caramelos","Pastillas","Pollo","Harina","Pimienta","Queso"
    ]
    lista_productos = []
    for p in productos:
        if p not in lista_productos:
            lista_productos.append(p)
    return lista_productos

#Agrupa los productos en categorias segun su tipo
def categorizar(lista_productos):     
    lacteos = []
    bebidas = []
    dulces = []
    alimentos = []
    frutas_verduras = []
    
    for producto in lista_productos:
        if producto in ["Leche","Queso","Yogurt","Mantequilla"] and producto not in lacteos:
            lacteos.append(producto)
        elif producto in ["Harina","Arroz","Pasta","Aceite de oliva","Huevo","Pan","Sal","Pimienta","Carne de res","Pollo","Pescado","Tomate","Cebolla","Papa","Zanahoria","Carne Congelada","Azucar","Miel","Mermelada","Papas fritas","Nueces","Almendras"] and producto not in alimentos:
            alimentos.append(producto)
        elif producto in ["Manzana","Banana","Naranja","Uva"] and producto not in frutas_verduras:
            frutas_verduras.append(producto)
        elif producto in ["Refresco","Agua","Cerveza","Café","Té","Jugo de naranja","Soda"] and producto not in bebidas:
            bebidas.append(producto)
        elif producto in ["Chocolates","Galletas","Turrones","Caramelos","Helado","Pastel","Torta","Donas","Bombones","Chicles","Pastillas","Gomitas","Chupetines","Regalices"]and producto not in dulces:
            dulces.append(producto)

    return lacteos, bebidas, dulces, alimentos, frutas_verduras


# Asigna una ubicacion a cada producto segun su tipo.
def obtener_ubicacion(lista_productos):
    congelador = ["Helado","Carne Congelada","Pescado","Pollo","Carne de res"]
    heladera = ["Carne de res", "Pollo", "Pescado", "Queso", "Yogurt", "Mantequilla", "Leche"]
    golosinas = [
        "Chicles", "Caramelos", "Pastillas", "Gomitas", "Turrones", "Bombones",
        "Chupetines", "Regalices", "Chocolates", "Galletas", "Papas fritas",
        "Miel", "Mermelada", "Pastel", "Torta", "Donas"]
    deposito  = [
        "Arroz","Harina","Azucar","Aceite de oliva","Agua","Cerveza","Refresco",
        "Pasta","Mermelada","Sal","Pimienta","Soda","Jugo de naranja","Café","Té"]

    productos_ubicacion = []
    ubicaciones = []

    for producto in lista_productos:
        if producto in congelador:
            lugar = "Camara frigorifica"
        elif producto in heladera:
            lugar = "Heladera"
        elif producto in golosinas:
            lugar = "Mostrador"
        elif producto in deposito:
            lugar = "Deposito"
        else:
            lugar = "Estanteria"
        productos_ubicacion.append(producto)
        ubicaciones.append(lugar)
            
    return productos_ubicacion, ubicaciones

# Asigna un stock aleatorio entre 0 y 40 a cada producto. 
def asignar_stock(lista_productos):
    
    stock = [r.randint(0, 40) for _ in range(len(lista_productos))]
    stock_productos = []
    
    for i in range(len(lista_productos)):
        stock_productos.append([lista_productos[i], stock[i]])
    
    return stock_productos

# Calcula el stock total por categoria y el stock total general
def total_categoria(lista_productos, stock, lacteos, bebidas, dulces, alimentos, frutas_verduras):
    total_lacteos = 0
    total_bebidas = 0
    total_dulces = 0
    total_alimentos = 0
    total_frutas_verduras = 0
    
    for i in range(len(lista_productos)):
        producto = lista_productos[i]
        cantidad = stock[i]
       
        if producto in lacteos:
            total_lacteos = total_lacteos + cantidad
        elif producto in bebidas:
            total_bebidas = total_bebidas + cantidad
        elif producto in dulces:
            total_dulces = total_dulces + cantidad
        elif producto in alimentos:
            total_alimentos = total_alimentos + cantidad
        elif producto in frutas_verduras:
            total_frutas_verduras = total_frutas_verduras + cantidad
    
    stock_total = total_lacteos + total_bebidas + total_dulces + total_alimentos + total_frutas_verduras
    
    return total_lacteos, total_bebidas, total_dulces, total_alimentos, total_frutas_verduras, stock_total

#Calcula el porcentaje de stock por categoria respecto al stock total, tiene en cuenta la posibilida d de 0 stock
def calcular_porcentajes_categoria(total_lacteos, total_bebidas, total_dulces, total_alimentos, total_frutas_verduras, stock_total):
    if stock_total > 0:
        porcentaje_lacteos = (total_lacteos / stock_total) * 100
        porcentaje_bebidas = (total_bebidas / stock_total) * 100
        porcentaje_dulces = (total_dulces / stock_total) * 100
        porcentaje_alimentos = (total_alimentos / stock_total) * 100
        porcentaje_frutas_verduras = (total_frutas_verduras / stock_total) * 100
        
    else:
        porcentaje_lacteos = 0
        porcentaje_bebidas = 0
        porcentaje_dulces = 0
        porcentaje_alimentos = 0
        porcentaje_frutas_verduras = 0
    
    return porcentaje_lacteos, porcentaje_bebidas, porcentaje_dulces, porcentaje_alimentos, porcentaje_frutas_verduras

# Clasifica el stock segun su cantidad
def clasificar_stock(productos, stock):
    stock_critico = [] 
    stock_bajo = []     
    stock_medio = []    
    
    for i in range(len(productos)):
        producto = productos[i]
        cantidad = stock[i]
        
        if cantidad == 0:
            stock_critico.append(producto)
        elif cantidad < 10:
            stock_bajo.append(producto)
        elif cantidad < 20:
            stock_medio.append(producto)
    
    return stock_critico, stock_bajo, stock_medio

# Calcula e imprime el stock minimo y maximo
def imprimir_min_max_stock(stock):
    
    stock_minimo = min(stock) if stock else 0
    stock_maximo = max(stock) if stock else 0
    print(f"Stock MÍNIMO: {stock_minimo}")
    print(f"Stock MÁXIMO: {stock_maximo}")
    return stock_minimo, stock_maximo

# Determina si un anio es bisiesto
def es_bisiesto(anio):
    
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

# Genera fechas de vencimiento aleatorias para cada producto.
def Vencimientos(lista_productos):
    fechas= []
    
    for _ in range(len(lista_productos)):
      anio = r.randint(2024, 2027)
      mes = r.randint(1, 12)

      if mes in [1, 3, 5, 7, 8, 10, 12]:
          dia = r.randint(1,31)
      elif mes in [4, 6, 9, 11]:
          dia = r.randint(1,30)
      else:
          if es_bisiesto(anio):
              dia = r.randint(1,29)
          else:
              dia = r.randint(1,28)

      fechas.append(f"{dia}-{mes}-{anio}")

    return fechas

# Asigna vencimientos y productos vencidos o proximos segun su fecha
def asignar_vencimiento(fechas, lista_productos):
    vencimientos = []
    
    for i in range(len(lista_productos)):
        producto = lista_productos[i]
        fecha = fechas[i]
        vencimientos.append([producto, fecha])

    vencidos = []
    proximos_vencimientos = []
    
    for i in range(len(vencimientos)):
        producto = vencimientos[i][0]
        fecha = vencimientos[i][1]
        
        partes_fecha = fecha.split('-')
        dia = int(partes_fecha[0])
        mes = int(partes_fecha[1])
        anio = int(partes_fecha[2])
        
        if anio == 2025 and mes == 10:
            proximos_vencimientos.append([producto, fecha])
            
        if (anio == 2024) or (anio == 2025 and (mes < 9 or (mes == 9 and dia <= 10))):
            vencidos.append([producto, fecha])
    

    vencidos_ordenados = ordenar_vencimientos(vencidos)
    proximos_ordenados = ordenar_vencimientos(proximos_vencimientos)
            
    return vencimientos, vencidos_ordenados, proximos_ordenados

def ordenar_vencimientos(vencimientos):
    
    vencimientos_ordenados = sorted(vencimientos, key=lambda x: x[0])
    
    return vencimientos_ordenados

# Muestra la lista completa de productos con vencimientos y maneja casos vacios
def mostrar_vencimientos_completos(vencimientos, vencidos, proximos):
    print("\n============ LISTA COMPLETA DE PRODUCTOS CON VENCIMIENTOS ============")
    print("\n- Todos los productos con sus fechas de vencimiento:")

    vencimientos_ordenados = ordenar_vencimientos(vencimientos)
    for producto, fecha in vencimientos_ordenados:
        print(f"  {producto}: {fecha}")
    
    print("\n- Vencidos:")
    if vencidos:
        for vencido in vencidos:
            print(f"  {vencido[0]}: {vencido[1]}")
    else:
        print("  No hay productos vencidos")
    
    print("\n- Proximos a vencer:")
    if proximos:
        for proximo in proximos:
            print(f"  {proximo[0]}: {proximo[1]}")
    else:
        print("  No hay productos proximos a vencer")



# Crea una matriz que muestra el stock de cada producto en su ubicacion correspondiente.
def matriz_stock(lista_productos, ubicaciones, stock):
    columnas = ["Producto", "estanteria", "camara frigorifica", "heladera", "mostrador", "deposito"]

    matriz = [[0] * len(columnas) for _ in lista_productos]
    for i, producto in enumerate(lista_productos):
        matriz[i][0] = producto
        if ubicaciones[i] == "Estanteria":
            columna_pos = 1
        elif ubicaciones[i] == "Camara frigorifica":
            columna_pos = 2
        elif ubicaciones[i] == "Heladera":
            columna_pos = 3
        elif ubicaciones[i] == "Mostrador":
            columna_pos = 4
        elif ubicaciones[i] == "Deposito":
            columna_pos = 5
        else:
            columna_pos = 1

        matriz[i][columna_pos] = stock[i]
    filas_str = [[str(v) for v in fila] for fila in matriz]
    num_cols = len(columnas)
    anchos = [0] * num_cols
    for j in range(num_cols):
        max_fila = max((len(f[j]) for f in filas_str), default=0 )
        anchos[j] = max(len(columnas[j]), max_fila)

    borde_str = "+" + "+".join("-" * (anchos[j] + 2) for j in range(num_cols)) + "+"
    encabezado_str = "| " + " | ".join(columnas[j].center(anchos[j]) for j in range(num_cols)) + " |"
    
    print("\nMatriz de stock (filas=productos, columnas=ubicaciones)")
    print(borde_str)
    print(encabezado_str)
    print(borde_str)
    for fila in filas_str:
        fila_str = "| " + " | ".join(str(fila[j]).center(anchos[j]) for j in range(num_cols)) + " |"
        print(fila_str)
    print(borde_str)

    return matriz
