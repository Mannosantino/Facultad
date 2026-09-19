from funciones import (
    carga_datos,
    categorizar,
    obtener_ubicacion,
    asignar_stock,
    clasificar_stock,
    total_categoria,
    calcular_porcentajes_categoria,
    imprimir_min_max_stock,
    Vencimientos,
    matriz_stock,
    asignar_vencimiento,
    ordenar_vencimientos,
    mostrar_vencimientos_completos,
)

def main():
    print("\n")
    texto = "MI ALMACEN DIGITAL"
    ancho = len(texto) + 4  # espacio para los bordes y espacios

    print("\t\t\t" + "*" * ancho)
    print("\t\t\t" + f"* {texto} *")
    print("\t\t\t" + "*" * ancho)
  
    productos = carga_datos()
    productos_ubicacion, ubicaciones = obtener_ubicacion(productos)
    stock_productos = asignar_stock(productos_ubicacion)
    
    stock = [cantidad for _, cantidad in stock_productos]
    
    print("\n\t============ MATRIZ DE STOCK POR UBICACION ============")
    matriz = matriz_stock(productos_ubicacion, ubicaciones, stock)
    
   
    lacteos, bebidas, dulces, alimentos, frutas_verduras = categorizar(productos)
    total_lacteos, total_bebidas, total_dulces, total_alimentos, total_frutas_verduras, stock_total = total_categoria(productos_ubicacion, stock, lacteos, bebidas, dulces, alimentos, frutas_verduras)
    porcentaje_lacteos, porcentaje_bebidas, porcentaje_dulces, porcentaje_alimentos, porcentaje_frutas_verduras = calcular_porcentajes_categoria(total_lacteos, total_bebidas, total_dulces, total_alimentos, total_frutas_verduras, stock_total)

    print("\n============ STOCK TOTAL POR CATEGORIA ============")
    print(f"Lacteos: {total_lacteos} ({porcentaje_lacteos:.2f}%)")
    print(f"Bebidas: {total_bebidas} ({porcentaje_bebidas:.2f}%)")
    print(f"Dulces: {total_dulces} ({porcentaje_dulces:.2f}%)")
    print(f"Alimentos: {total_alimentos} ({porcentaje_alimentos:.2f}%)")
    print(f"Frutas y verduras: {total_frutas_verduras} ({porcentaje_frutas_verduras:.2f}%)")
    print(f"STOCK TOTAL: {stock_total}")

    stock_critico, stock_bajo, stock_medio = clasificar_stock(productos_ubicacion, stock)
    print("\n============ CLASIFICACION DE STOCK ============")
    print(f"Stock CRITICO (0 unidades): {stock_critico}")
    print(f"Stock BAJO (< 10 unidades): {stock_bajo}")
    print(f"Stock MEDIO (< 20 unidades): {stock_medio}")
    imprimir_min_max_stock(stock)
    
    
    fechas_venc = Vencimientos(productos_ubicacion)
    vencimientos, vencidos, proximos = asignar_vencimiento(fechas_venc, productos_ubicacion)
    mostrar_vencimientos_completos(vencimientos, vencidos, proximos)
        
    print("-"*80)


if __name__ == "__main__":
    main()

    

