import numpy as np

def cargar_datos(ruta_archivo):
    # Carga los datos del archivo CSV utilizando NumPy
    datos = np.genfromtxt(ruta_archivo, delimiter=',', skip_header=1)
    #print(f"ndim: {datos.ndim}")
    #print(f"shape: {datos.shape}")
    #print(f"size: {datos.size}")
    #print(f"flatten: {datos.flatten()}")

    return datos


def total_de_ventas(dato):

    # Crear un diccionario para almacenar las sumas por producto
    suma_ingresos_por_producto = {}
    for fila in dato:
        producto = int(fila[1]) # Obtenemos el producto (columna 1)
        ingreso = float(fila[2]) # Obtenemos el ingreso (columna 2) y lo convertimos a float

        # Actualizar la suma en el diccionario
        if producto in suma_ingresos_por_producto:
            suma_ingresos_por_producto[producto] += ingreso # Sumar al ingreso existente
        else:
            suma_ingresos_por_producto[producto] = ingreso # Inicializar el ingreso
    print("Total de ventas por producto:".upper())
    print("producto \t ingreso".upper())
    for producto, total in suma_ingresos_por_producto.items():
        print(f"{producto} \t\t {total}")
    


    suma_ingresos_por_tienda = {}

    for fila in dato:
        tienda = int(fila[3]) # Obtenemos la tienda (columna 3)
        ingreso = float(fila[2]) # Obtenemos el ingreso (columna 2) y lo convertimos a float

        # Actualizar la suma en el diccionario
        if tienda in suma_ingresos_por_tienda:
            suma_ingresos_por_tienda[tienda] += ingreso # Sumar al ingreso existente
        else:
            suma_ingresos_por_tienda[tienda] = ingreso # Inicializar el ingreso
    print("\nTotal de ventas por tienda:".upper())
    print("tienda \t\t ingreso".upper())
    for tienda, total in suma_ingresos_por_tienda.items():
        print(f"{tienda} \t\t {total}")
    

if __name__ == "__main__":
    ruta_archivo = ruta_csv
    datos = cargar_datos(ruta_archivo)
    #print(datos)
    total_de_ventas(datos)