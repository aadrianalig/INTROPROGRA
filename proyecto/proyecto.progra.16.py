#Animacion de bienvenida
import time
import os
import sys

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def escribir(texto, velocidad=0.05):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()

def animacion_banner():
    banner_frames = [
r"""
🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌
██     ██ ███████  ██       █████   ██████  ███    ███ ███████
██     ██ ██       ██      ██      ██    ██ ████  ████ ██            
██  █  ██ █████    ██      ██      ██    ██ ██ ████ ██ █████    
██ ███ ██ ██       ██      ██      ██    ██ ██  ██  ██ ██         
 ███ ███  ███████  ███████  █████   ██████  ██      ██ ███████
🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌 
✨ Bienvenido al Sistema de Recaudación ✨
""",
r"""
🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌
██     ██ ███████  ██       █████   ██████  ███    ███ ███████
██     ██ ██       ██      ██      ██    ██ ████  ████ ██            
██  █  ██ █████    ██      ██      ██    ██ ██ ████ ██ █████    
██ ███ ██ ██       ██      ██      ██    ██ ██  ██  ██ ██         
 ███ ███  ███████  ███████  █████   ██████  ██      ██ ███████
🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌 
✨ Bienvenido al Sistema de Recaudación ✨
"""
    ]
    for _ in range(2):  # Repite la animación 2 veces
        for frame in banner_frames:
            clear_console()
            print(frame)
            time.sleep(0.7)

def bienvenida():
    clear_console()
    animacion_banner()
    escribir("\n¡Bienvenido al programa de control de recaudación de Transportes Express!", 0.05)
    escribir("Cargando el sistema, por favor espere...", 0.05)
    for i in range(1, 11):
        sys.stdout.write(f"\rProgreso: [{'█'*i}{'.'*(10-i)}] {i*10}%")
        sys.stdout.flush()
        time.sleep(0.2)
    print("\n\n¡Listo para comenzar!")


#Solicitar informacion
def solicitar_cantidad(tipo):
    if tipo == "buses":
        limite = 80
    if tipo == "lineas":
        limite = 40
    print(f"Ingrese la cantidad de {tipo}")
    cantidad = int(input())
    while cantidad < 0 or cantidad > limite:
        print("El número no es correcto, ingrese nuevamente")
        cantidad = int(input())
    return cantidad

#Generar matriz de recaudacion
import random
def generar_recaudaciones (buses, lineas):
    matriz = []
    for i in range (buses): 
        fila = []
        for j in range(lineas):
            monto = random.randint(5000,12000)
            fila.append(monto)
        matriz.append(fila)
    return matriz

# Generar lista de total de recaudaciones por bus
def generar_lista_total_recaudaciones_por_bus(matriz):
    recaudaciones_totales_por_bus = []
    for i in range(len(matriz)):  # Recorre cada bus
        suma = 0  
        for j in range(len(matriz[i])):  # Recorre cada recaudación (por línea)
            suma = suma + matriz[i][j]  # Suma recaudación
        recaudaciones_totales_por_bus.append(suma)  # la suma total de ese bus
    return recaudaciones_totales_por_bus  

# Bus con mayor recaudación total
def encontrar_buses_mayor_recaudacion_total(recaudaciones_totales_por_bus):
    mayor = 0 
    buses_recaudacion_total_mayor = []
    for i in range(len(recaudaciones_totales_por_bus)): # Recorre la lista de recaudaciones por bus
        if recaudaciones_totales_por_bus[i] >= mayor:
            mayor = recaudaciones_totales_por_bus[i]  # Encuentra mayor

    for j in range(len(recaudaciones_totales_por_bus)):# Recorre para encontrar todos los buses que tengan esa recaudación máxima
        recaudacion = recaudaciones_totales_por_bus[j]
        if recaudacion == mayor:
            buses_recaudacion_total_mayor.append(j+1)  # Guardamos el número del bus (sumamos 1 porque empieza en 0)
    
    return buses_recaudacion_total_mayor  # Retornamos la lista de buses con mayor recaudación


# Bus con mayor recaudación por línea
def mayor_recaudacion_por_linea(matriz):
    lista_recaudacion_por_linea = []  # Aquí guardaremos los buses con mayor recaudación por cada línea

    for i in range(len(matriz[0])):  # Recorremos cada columna (línea)
        mayor = 0  # Reiniciamos el mayor para esa línea
        for j in range(len(matriz)):  # Recorremos cada fila (bus)
            if matriz[j][i] >= mayor:
                mayor = matriz[j][i]  # Buscamos la mayor recaudación de esa línea

        lista = []  # Lista para guardar los buses que tuvieron esa mayor recaudación
        for j in range(len(matriz)):
            if matriz[j][i] == mayor:
                lista.append(j+1)  # Guardamos el número del bus

        lista_recaudacion_por_linea.append(lista)  # Añadimos esa lista de buses a la lista principal
    
    return lista_recaudacion_por_linea  # Retornamos todos los buses con mayor recaudación por línea


# Línea con menor recaudación de cada bus
def linea_menor_cada_bus(matriz):
    lista_indices_lineas = []  # Lista para guardar las líneas con menor recaudación de cada bus

    for i in range(len(matriz)):  # Recorremos cada bus (fila)
        menor = 800000000  # Inicializamos con un número muy grande
        for j in range(len(matriz[i])):  # Recorremos las líneas de ese bus
            if matriz[i][j] <= menor:
                menor = matriz[i][j]  # Guardamos el menor valor encontrado

        lista = []  # Lista para guardar qué línea(s) tienen ese menor valor
        for j in range(len(matriz[i])):
            if matriz[i][j] == menor:
                indice = j+1  # Sumamos 1 al índice para mostrarlo como línea 1, 2, 3...
                lista.append(indice)
        
        lista_indices_lineas.append(lista)  # Guardamos la(s) línea(s) de menor recaudación de ese bus
    
    return lista_indices_lineas  # Retornamos todas las líneas con menor recaudación por bus


# Función recursiva para sumar el total de toda la matriz
def suma_total_recaudacion(matriz):
    if matriz == []:  # Caso base: si la matriz está vacía, la suma es 0
        return 0

    primera_fila = matriz[0]  # Tomamos la primera fila de la matriz
    suma_fila = 0  # Inicializamos la suma de esa fila

    for i in range(len(primera_fila)):  # Sumamos los elementos de la fila
        suma_fila = suma_fila + primera_fila[i]

    # Llamamos a la misma función con el resto de la matriz (sin la primera fila)
    return suma_fila + suma_total_recaudacion(matriz[1:])

    
# Ordenar buses por recaudación total (de mayor a menor)
def ordenar_buses(matriz):
    lista_totales = generar_lista_total_recaudaciones_por_bus(matriz)
    buses_ordenados = []
    
    while len(buses_ordenados) < len(lista_totales):
        mayor = -1
        indice_mayor = -1
        for i in range(len(lista_totales)):
            if lista_totales[i] > mayor:
                mayor = lista_totales[i]
                indice_mayor = i
        
        buses_ordenados.append((indice_mayor + 1, mayor)) #(nmr_bus,monto)
        lista_totales[indice_mayor] = -99999999 #(montos validos son positivos)
        
    return buses_ordenados


# Recaudacion de un bus en una linea determinada

def recaudacion_bus(matriz, num_bus, num_linea):
    return matriz[num_bus - 1][num_linea - 1]

# Intercambio de montos de 2 buses en una linea determinada
def intercambiar_recaudaciones(matriz, bus1, bus2, linea):
    temp = matriz[bus1 - 1][linea - 1]
    matriz[bus1 - 1][linea - 1] = matriz[bus2 - 1][linea - 1]
    matriz[bus2 - 1][linea - 1] = temp

#mostrar matriz de recaudaciones
def mostrar_matriz(matriz):
    print("Matriz de recaudaciones actualizada:\n")
    
    print("      ", end="")
    for j in range(len(matriz[0])):
        print(f"Linea {j+1}", end="\t")
    print()
    
    for i in range(len(matriz)):
        print(f"Bus {i+1}", end="\t")
        for j in range(len(matriz[0])):
            print(matriz[i][j], end="\t")
        print()


if __name__ == "__main__":
    bienvenida()
    print()
    #Solicitud para la generacion de la matriz
    buses = solicitar_cantidad("buses")
    lineas = solicitar_cantidad("lineas")
    print()
    matriz = generar_recaudaciones(buses, lineas)

    #Imprimir matiz
    print("Matriz de recaudaciones:\n")

    # Encabezado: nombres de las líneas
    print("       ", end="")
    for j in range(lineas):
        print("Línea", j+1, end="\t")
    print()

    # Cuerpo: filas con nombres de buses
    for i in range(buses):
        print("Bus", i+1, end="\t")
        for j in range(lineas):
            print(matriz[i][j], end="\t")
        print()

    #Menu interactivo con opciones (1-9)
    seguir = 2
    while seguir>1:
        print("\n¿Qué desea hacer?")
        print("1. Ver recaudación total por bus")
        print("2. Ver bus(es) con mayor recaudación total")
        print("3. Ver buses con mayor recaudación por línea")
        print("4. Ver línea(s) con menor recaudación de cada bus")
        print("5. Ver suma total recaudado")
        print("6. Ver buses ordenados por total (mayor -> menor) ")
        print("7. Ver recaudacion de un bus en una linea específica")
        print("8. Ver intercambio de montos de dos buses en una linea")
        print("9. Salir")

        #Pedir opcion del menu
        opcion = int(input("Seleccione una opción (1-9): "))

        if opcion == 1:
            print('-------------')
            lista = generar_lista_total_recaudaciones_por_bus(matriz)
            print("Recaudación total por bus:")
            for i in range(len(lista)):
                print(f"Bus {i+1}: s/.{lista[i]}")
            print('-------------')
                

        elif opcion == 2:
            print('-------------')
            lista = generar_lista_total_recaudaciones_por_bus(matriz)
            mayores = encontrar_buses_mayor_recaudacion_total(lista)
            print("Bus(es) con mayor recaudación total:")
            for i in range(len(mayores)):
                print(f"- Bus {mayores[i]}")
            print('-------------')
        
        elif opcion == 3:
            print('-------------')
            listas_por_linea = mayor_recaudacion_por_linea(matriz)
            for i in range(lineas):
                print(f"Línea {i+1}: mayor recaudación por bus(es):")
                for bus in listas_por_linea[i]:
                    print(f"- Bus {bus}")
            print('-------------')

        elif opcion == 4:
            print('-------------')
            listas = linea_menor_cada_bus(matriz)
            for i in range(buses):
               print(f'Bus {i+1}: línea(s) con menor recaudación:')
               for linea in listas[i]:
                   print(f"- Línea {linea}")
            print('-------------')

        elif opcion == 5:
            print('-------------')
            total = suma_total_recaudacion(matriz)
            print(f"Suma total de todas las recaudaciones: s/.{total}")
            print('-------------')

        elif opcion == 6:
            print('-------------')
            orden = ordenar_buses(matriz)
            print("Buses ordenados por recaudacion total (mayor a menor):")
            for i in range(len(orden)):
                bus = orden[i][0]
                monto = orden[i][1]
                print(f"- Bus{bus} : s/.{monto}")
            print('-------------')
      
        elif opcion == 7:
            print('-------------')
            print(f"Cantidad de buses disponibles: {buses}")
            num_bus = int(input("Ingrese el número del bus: "))
            while num_bus < 1 or num_bus > buses:
                print("No válido, ingrese los datos correctos.")
                print(f"Cantidad de buses disponibles: {buses}")
                num_bus = int(input("Ingrese el número del bus: "))

            print(f"Cantidad de líneas disponibles: {lineas}")
            num_linea = int(input("Ingrese el número de la línea: "))
            while num_linea < 1 or num_linea > lineas:
                print("No válido, ingrese los datos correctos.")
                print(f"Cantidad de líneas disponibles: {lineas}")
                num_linea = int(input("Ingrese el número de la línea: "))

            monto = recaudacion_bus(matriz, num_bus, num_linea)
            print(f"El bus {num_bus} recaudó s/.{monto} en la línea {num_linea}")
            print('-------------')
            
        elif opcion == 8:
            print('-------------')
            print(f"Cantidad de buses disponibles: {buses}")
            bus1 = int(input("Ingrese el número del primer bus: "))
            while bus1 < 1 or bus1 > buses:
                print("No válido, ingrese los datos correctos.")
                bus1 = int(input("Ingrese el número del primer bus: "))

            bus2 = int(input("Ingrese el número del segundo bus: "))
            while bus2 < 1 or bus2 > buses:
                print("No válido, ingrese los datos correctos.")
                bus2 = int(input("Ingrese el número del segundo bus: "))

            print(f"Cantidad de líneas disponibles: {lineas}")
            linea = int(input("Ingrese el número de la línea: "))
            while linea < 1 or linea > lineas:
                print("No válido, ingrese los datos correctos.")
                linea = int(input("Ingrese el número de la línea: "))
            print("--------------")    
            print("Antes del intercambio")
            print(f"Bus {bus1}, Línea {linea}: {matriz[bus1 - 1][linea - 1]}")
            print(f"Bus {bus2}, Línea {linea}: {matriz[bus2 - 1][linea - 1]}")

            intercambiar_recaudaciones(matriz, bus1, bus2, linea)

            print("--------------")
            print("Después del intercambio")
            print(f"Bus {bus1}, Línea {linea}: {matriz[bus1 - 1][linea - 1]}")
            print(f"Bus {bus2}, Línea {linea}: {matriz[bus2 - 1][linea - 1]}")
            print('-------------')
            
            mostrar_matriz(matriz)
            print('-------------')

        #Finalizar menu con un false
        elif opcion == 9:
            seguir = 0
            print('-------------')
            print("Gracias por usar el sistema de recaudacion. ¡Hasta pronto! 🚍")
        else:
            print("Opción inválida")
