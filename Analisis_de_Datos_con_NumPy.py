import numpy as np

def generar_datos_ventas(productos, tiendas, dias):
    # Genera datos de ventas aleatorias para el número de productos, tiendas y días especificados
    return np.random.randint(0, 101, (productos, tiendas, dias)) # Generamos un array de 3 dimensiones con números aleatorios entre 0 y 100

def calcular_totales_ventas_por_producto(datos):
    # Calcula el total de ventas por producto a lo largo de la semana
    return np.sum(datos, axis=(1, 2)) # Sumamos los valores de la primera y segunda dimensión del array

def calcular_totales_ventas_por_tienda(datos):
    # Calcula el total de ventas por tienda a lo largo de la semana
    return np.sum(datos, axis=(0, 2)) # Sumamos los valores de la primera y segunda dimensión del array

def calcular_promedio_ventas_por_producto(datos):
    # Calcula el promedio de ventas por producto por día
    return np.mean(datos, axis=(1, 2)) # Calculamos el promedio de los valores de la primera y segunda dimensión del array


def calcular_promedio_ventas_por_tienda(datos):
    # Calcula el promedio de ventas por tienda por día
    return np.mean(datos, axis=(0, 2)) # Calculamos el promedio de los valores de la primera y segunda dimensión del array

def encontrar_producto_mayor_menor_ventas(totales_por_producto):
    # Encuentra el producto con mayor y menor ventas totales en la semana
    producto_mayor_ventas = np.argmax(totales_por_producto)  # Buscamos el índice del producto con mayor venta
    producto_menor_ventas = np.argmin(totales_por_producto)   # Buscamos el índice del producto con menor venta
    return producto_mayor_ventas, producto_menor_ventas # Retornamos los índices de los productos con mayor y menor venta

def encontrar_tienda_mayor_menor_ventas(totales_por_tienda):
    # Encuentra la tienda con mayor y menor ventas totales en la semana
    tienda_mayor_ventas = np.argmax(totales_por_tienda) # Buscamos el índice de la tienda con mayor venta
    tienda_menor_ventas = np.argmin(totales_por_tienda) # Buscamos el índice de la tienda con menor venta
    return tienda_mayor_ventas, tienda_menor_ventas  # Retornamos los índices de las tiendas con mayor y menor venta

productos = 10
tiendas = 5
dias = 7

# Genera los datos de ventas
datos = generar_datos_ventas(productos, tiendas, dias) # Generamos los datos de ventas

# Calcula los totales y promedios
totales_por_producto = calcular_totales_ventas_por_producto(datos) # Calculamos los totales de ventas por producto
totales_por_tienda = calcular_totales_ventas_por_tienda(datos) # Calculamos los totales de ventas por tienda
promedio_por_producto = calcular_promedio_ventas_por_producto(datos) # Calculamos el promedio de ventas por producto
promedio_por_tienda = calcular_promedio_ventas_por_tienda(datos) # Calculamos el promedio de ventas por tienda

# Encuentra el producto y la tienda con mayor y menor ventas
producto_mayor_ventas, producto_menor_ventas = encontrar_producto_mayor_menor_ventas(totales_por_producto)  # Encuentra el producto con mayor y menor venta
tienda_mayor_ventas, tienda_menor_ventas = encontrar_tienda_mayor_menor_ventas(totales_por_tienda)  # Encuentra la tienda con mayor y menor venta

# Imprime los resultados
print("Total de ventas por producto a lo largo de la semana:", totales_por_producto)
print("Total de ventas por tienda a lo largo de la semana:", totales_por_tienda)
print("Promedio de ventas por producto por día:", promedio_por_producto)
print("Promedio de ventas por tienda por día:", promedio_por_tienda)
print(f"Producto con mayor ventas: Producto {producto_mayor_ventas}")
print(f"Producto con menor ventas: Producto {producto_menor_ventas}")
print(f"Tienda con mayor ventas: Tienda {tienda_mayor_ventas}")
print(f"Tienda con menor ventas: Tienda {tienda_menor_ventas}")