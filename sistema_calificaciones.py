def obtener_numero_estudiantes():
    # Pide al usuario el número de estudiantes y devuelve el valor
    """
    Solicitamos al usuario que ingrese la cantidad de estudiantes previendo también la
    posibilidad de que cometa algún error por equivocación ingresando símbolos o números
    negativos
    """
    print("\n¡Bienvenido al Sistema de Calificaciones!")

    try:
        student_qty = int(input("\nIngrese el número de estudiantes: ")) # Solicitamos que ingrese la cantidad de estudiantes
        if student_qty > 0: # Verificamos que lo ingresado sea mayor a cero 
            return student_qty # Retornamos el valor ingresado
        else: # Si el valor ingresado es menor que 1 le solicitamos nuevamente que vuelva a ingresar
            print("No puede ser menor a 1") # Avisamos al usuario que ha ingresado un número menor a 1
            return obtener_numero_estudiantes() # Volvemos a ejecutar la misma función para que vuelva a ingresar el valor
    except ValueError: # Si el valor contiene símbolos capturamos el error
        print("El número de estudiantes es inválido") # Avisamos al usuario que ha ingresado un valor inválido
        return obtener_numero_estudiantes() # Volvemos a ejecutar la misma función para que vuelva a ingresar el valor

def obtener_nombre_estudiante():
    # Pide al usuario el nombre del estudiante y devuelve el valor
    """
    Solicitamos al usuario que ingrese el nombre de los estudiantes y también prevenimos que cometa algún error
    """
    try:
        student_name = str(input("\nIngrese el nombre del estudiante: ")) # Solicitamos el nombre del estudiante
        if student_name != "" and student_name.isalpha(): # Corroboramos que el campo no esté vacío y que solo sea letras
            return student_name.strip().capitalize() # Retornamos el valor ingresado y quitamos los espacios. También ponemos en mayúscula la primera letra
        else:
            print("Inválido! El campo nombre del estudiante no puede estar vacío. Solo pueden contener letras.")
            return obtener_nombre_estudiante() # En caso de algún incumplimiento en el condicional volvemos a iniciar esta función
    except ValueError:
        print("Nombre inválido")
        return obtener_nombre_estudiante() # En caso de algún error volvemos a iniciar esta función

def obtener_numero_asignaturas():
    # Pide al usuario el número de asignaturas y devuelve el valor
    """
    Solicitos al usuario que ingrese la cantidad de asignaturas por estudiante
    """
    try:
        asignature_qty = int(input("Ingrese el número de asignaturas: ")) # Solicitamos que ingrese la cantidad de asignaturas
        if asignature_qty > 0: # Corroboramos que sea mayor que cero
            return asignature_qty # Retornamos el valor
        else:
            print("La cantidad de asignaturas no puede ser menor a 1\n")
            return obtener_numero_asignaturas() # Si es menor que 1 volvemos a ejecutar esta funcion para solicitar
    except ValueError:
        print("Número de asignaturas es inválido. Solo se aceptan números enteros.\n")
        return obtener_numero_asignaturas() # Si el usuario ingresa otro tipo de valor que no sea número retornamos a la misma función para ejecutarlo de vuelta 

def obtener_calificaciones(num_asignaturas):
    # Pide al usuario las calificaciones para cada asignatura y las devuelve en una lista
    """
    En esta funcion ingresaremos las calificaciones segun la cantidad
    de asignaturas que se haya ingresado previamente
    """
    calificaciones = []
    for i in range(num_asignaturas): # Recorremos la cantidad de asignaturas
        try:
            # Ingresamos las calificaciones para cada asignatura
            calificacion = int(input(f"Ingrese la calificación de la asignatura {i+1}:\nNota: La calificación debe ser un número entre 0 y 10: "))
            while calificacion < 0 or calificacion > 10: # Corroboramos si el usuario no ingrese calificaciones fuera del rango de 0 a 10
                print("La calificación es inválida")
                return obtener_calificaciones(num_asignaturas) # Si el usuario ingresó numeros fuera del rango volvemos a ejecutar la función
            calificaciones.append(calificacion)
        except ValueError: # Capturamos el error en caso de que se haya ingresado un valor que no sea número entero
            print("La calificación es inválida")
            return obtener_calificaciones(num_asignaturas) # Volvemos a ejecutar la función debido al error previo
    return calificaciones # Retornamos las calificaciones

def calcular_promedio(calificaciones):
    # Calcula y devuelve el promedio de las calificaciones
    """
    Calculamos el promedio de cada estudiante
    """
    promedio = sum(calificaciones) / len(calificaciones) # Sumamos las calificaciones y dividimos por la cantidad de asignaturas
    return promedio # Retornamos el promedio

def determinar_estado(promedio):
    # Determina si el estudiante ha aprobado o reprobado basándose en el promedio
    """
    Verificamos si el estudiante aprobó o no la asignatura
    """
    estado = ''
    for i in range(num_estudiantes): # Recorremos la cantidad de estudiante
        if promedio < 6: # Corroboramos si el promedio de cada estudiante es menor a 6
            estado = 'Reprobado' # Si es menor que 6 entonces está reprobado
        else:
            estado = 'Aprobado' # Si es mayor que 6 está aprobado
    return estado # Retornamos el estado

def imprimir_resumen(estudiantes):
    # Imprime un resumen con el nombre de los estudiantes, su promedio y su estado
    """
    Imprimimos el resultado de cada estudiante mostrando el nombre, su promedio y su estado
    """
    print()
    for diccionario in estudiantes: # Recorremos la lista de estudiantes
        print(f"Nombre: {diccionario['nombre']}\tPromedio: {diccionario['promedio']}\tEstado: {diccionario['estado']}")

num_estudiantes = obtener_numero_estudiantes() # Capturamos la cantidad de estudiantes
estudiantes = [] # Lista que guardará los datos de los estudiantes

for _ in range(num_estudiantes): # Recorremos la cantidad de estudiantes
    nombre = obtener_nombre_estudiante() # Capturamos el nombre de cada estudiante
    num_asignaturas = obtener_numero_asignaturas() # Capturamos la cantidad de asignaturas de cada estudiante
    calificaciones = obtener_calificaciones(num_asignaturas) # Capturamos las calificaciones según cada asignatura
    promedio = calcular_promedio(calificaciones) # Capturamos el promedio de cada estudiante
    estado = determinar_estado(promedio) # Capturamos el estado de cada estudiante
    
    estudiantes.append({    # Guardamos los datos de los estudiantes en una lista que contiene un diccionario
        'nombre': nombre,
        'promedio': promedio,
        'estado': estado
    })

imprimir_resumen(estudiantes) # Ejecutamos el programa