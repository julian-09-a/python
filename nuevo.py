import random

def es_numero(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False

print("\n")
print("BIENVENIDO :) ")
print("\n")
tamano = int(input("Digite el tamaño inicial para su lista: "))
lista = [random.randint(1, 100) for _ in range(tamano)]

while True:
    print("\nMENU:")
    print("1) Ingresar elemento")
    print("2) Eliminar elemento")
    print("3) Ordenar lista")
    print("4) Seleccionar un elemento")
    print("5) Seleccionar una posición")
    print("6) Cambiar tamaño de la lista")
    print("7) Ver longitud de la lista")
    print("8) Borrar lista")
    print("9) Salir")
    
    print("\nLista de elementos:")
    print(lista)

    opcion = input("Seleccione una opción: ").lower()

    if opcion == '1':
        elemento = input("Digite el elemento a ingresar: ")
        if es_numero(elemento):
            elemento = int(elemento)
        lista.append(elemento)
        print(f"Elemento '{elemento}' ingresado correctamente.")
    elif opcion == '2':
        elemento = input("Digite el elemento a eliminar: ")
        if es_numero(elemento):
            elemento = int(elemento)
        if elemento in lista:
            lista.remove(elemento)
            print(f"Elemento '{elemento}' eliminado correctamente.")
        else:
            print(f"Elemento '{elemento}' no encontrado en la lista.")
    elif opcion == '3':
        orden = input("Ingrese 'a' para ordenar ascendente o 'd' para ordenar descendente: ").lower()
        if orden == 'a':
            lista.sort()
        elif orden == 'd':
            lista.sort(reverse=True)
        else:
            print("Opción de orden no válida.")
    elif opcion == '4':
        elemento = input("Digite el elemento a buscar: ")
        if es_numero(elemento):
            elemento = int(elemento)
        if elemento in lista:
            print(f"Elemento '{elemento}' encontrado en la lista.")
        else:
            print(f"Elemento '{elemento}' no encontrado en la lista.")
    elif opcion == '5':
        posicion = int(input("Digite la posición a buscar: "))
        if 0 <= posicion < len(lista):
            elemento_en_posicion = lista[posicion]
            print(f"El elemento en la posición {posicion} es '{elemento_en_posicion}'.")
        else:
            print("Posición fuera de rango.")
    elif opcion == '6':
        nuevo_tamano = int(input("Digite el nuevo tamaño de la lista: "))
        lista = [random.randint(1, 100) for _ in range(nuevo_tamano)]
        print("Lista modificada con el nuevo tamaño.")
    elif opcion == '7':
        print(f" La longitud de la lista es {len(lista)}.")
    elif opcion == '8':
        lista.clear()
        print("Lista borrada.")
    elif opcion == '9':
        break
    else:
        print("Opción no válida. Intente nuevamente.")

    
print(" El programa finalizo, chao :) ")
