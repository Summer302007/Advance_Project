
# Importa el módulo os para comandos del sistema
import os
# Importa el módulo time para pausas en la ejecución
import time
productos_añadidos = {}# Diccionario global para almacenar los productos añadidos (nombre: (precio, cantidad))

# Función para añadir un producto al inventario si no existe aún
def Añadir_productos(nombre, precio, cantidad):
    
    if nombre in productos_añadidos:
        print("El producto ya existe.")
        
    else:# Opción inválida: el usuario ingresó una opción no válida
        productos_añadidos [nombre] = (precio, cantidad)
        print(f"!El producto {nombre} ha sido añadido exitosamente¡")
        
 # Función para buscar un producto por nombre e imprimir sus detalles       
def Buscar_producto(nombre):
    
    if nombre in productos_añadidos:
        precio, cantidad = productos_añadidos[nombre]
        print(f"{nombre} → Precio: ${precio} | Cantidad: {cantidad}")
    # Opción inválida: el usuario ingresó una opción no válida    
    else:
        print(f" Producto '{nombre}' no encontrado.")
        

# Función para actualizar el precio de un producto existente
def Actualizar_precio(nombre, nuevo_precio):
    if nombre in productos_añadidos:
        precio, cantidad = productos_añadidos[nombre]
        productos_añadidos[nombre] = (nuevo_precio, cantidad)
        print(f"El precio  el precio antiguo de {nombre} era {precio} ha sido actualizado por ${nuevo_precio}")
        print(productos_añadidos)
    else:
        print("producto no encontrado")
    
# Función para eliminar un producto del inventario
def Eliminar_producto(nombre):
    # Diccionario global para almacenar los productos añadidos (nombre: (precio, cantidad))
    if nombre in productos_añadidos:
        productos_añadidos.pop(nombre)#.pop ayuda a eliminar el producto
        print(f"El producto {nombre} ha sido eliminado")
        
    else:# Opción inválida: el usuario ingresó una opción no válida
        print("producto no encontrado")
    
# Función para calcular el valor total del inventario 
def Calcular_valor_total():#(precio x cantidad y suma todos los resultados de cada operacion realizada.)
    total = sum(map(lambda item: item[0] * item[1], productos_añadidos.values()))
    # Usar .values() para obtener solo los valores de ese diccionario, sin las claves.
    # map aplica esa multiplicación a cada producto.
    print(f"Valor total del inventario es de ${total}")

# Bucle principal del programa: muestra el menú hasta que el usuario decida salir
menu = False
# Inicia el bucle del menú principal
while not menu:
    
    print("*"*90)
    print(f"{"BIENVENIDO TU SISTEMA DE INVENTARIO":^80}\n")
    print("*"*90)

    print("\n1.Añadir productos")
    print("2.Buscar productos ")
    print("3.Actualizar precios")
    print("4.Eliminar productos")
    print("5.Calcular valor total del inventario")
    print("6.Salir")
    
    print("-"*90)
    Respuesta = input("\n¿Que actividad desear realizar? selecciona una opcion (1-6): ")
    print("-"*90)
    
    # Opción 1: Añadir un nuevo producto al inventario
    if Respuesta == "1":
        
        nombre = input("\nIngrese el producto que desea añadir: ")

        try:
            precio = float(input("Ingrese el precio del producto: $"))
            cantidad = int(input("Ingrese cantidad de productos disponibles: "))

            if precio > 0 and cantidad > 0:
                Añadir_productos(nombre, precio, cantidad)
                print(productos_añadidos)
            # Opción inválida: el usuario ingresó una opción no válida
            else:
                print("El precio y la cantidad deben ser mayores que cero.")
                
        except ValueError: #Opción inválida: el usuario ingresó una opción no válida
            print("Entrada inválida. Usa números para precio y cantidad.")
            print("-"*90)
    
    # Opción 2: Buscar un producto existente en el inventario
    elif Respuesta == "2":
        
        Buscar_producto(nombre = input("\n ¿Que producto que desea buscar?: "))
        print("-"*90)
     # Opción 3: Actualizar el precio de un producto existente   
    elif Respuesta == "3":
        nombre = input("\nNombre del producto: ")
        try:
            nuevo_precio = float(input("Nuevo precio: $"))
            if nuevo_precio > 0: #si el precio es mayor a cero se guarda
                Actualizar_precio(nombre, nuevo_precio)
            else:# Opción inválida: el usuario ingresó una opción no válida
                print("El precio debe ser mayor que cero.")

        except ValueError:# Opción inválida: el usuario ingresó una opción no válida, se devuelve al bucle y 
            #me vuelve a mostrar el menú para que ingrese los datos de nuevo
            print("Entrada inválida. Usa un número para el precio.")
            print("-"*90)
     # Opción 4: Eliminar un producto del inventario   
    elif Respuesta == "4":
        Eliminar_producto(nombre = input("\nNombre del producto que desea eliminar: "))
        print(productos_añadidos)
        print("-"*90)
     # Opción 5: Calcular el valor total del inventario   
    elif Respuesta == "5":
        Calcular_valor_total()
        print("-"*90)
      # Opción 6: Salir del programa  
    elif Respuesta == "6":
        print("\nHa salido del programa.")
        print("-"*90)
        menu = True
     # Opción inválida: el usuario ingresó una opción no válida   
    else:# si hay un error, se va a salir de la condición y vuelve a ejecutar la pregunta de nuevo con las opciones
        print("\nOpción inválida, intente de nuevo. (1-5)\n")
        print("-" * 90)
        time.sleep(1)
        os.system('clear')
