import os

def cargar_archivo_xml(nombre_archivo):
    if nombre_archivo.endswith(".xml"):
        try:
            with open(nombre_archivo, "r") as archivo:
                contenido = archivo.read()
                print("Contenido del archivo:")
                print(contenido)
        except FileNotFoundError:
            print("El archivo especificado no existe.")
    else:
        print("El archivo no tiene la extensión .xml.")


while True:
    print("============================================================")
    print("\nMenú:")
    print("a. Cargar un archivo XML de entrada")
    print("b. Gestión de maquetas")
    print("c. Resolución de maquetas")
    print("d. Ayuda")
    print("e. Salir")
    print("============================================================")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "a":
        nombre_archivo = input("Ingrese el nombre del archivo XML de entrada: ")
        cargar_archivo_xml(nombre_archivo)

    elif opcion == "b":
        sub_opcion = input("Seleccione una opción:\n a. Ver listado de maquetas ordenado alfabéticamente\n b. Ver configuración de maqueta\n")

        if sub_opcion == "a":
            lista_pisos.mostrar_pisos_ordenados()
        elif sub_opcion == "b":
            nombre_maqueta = input("Ingrese el nombre de la maqueta: ")
            lista_pisos.mostrar_configuracion_maqueta(nombre_maqueta)
        else:
            print("Opción no válida.")

    elif opcion == "c":
        sub_opcion = input("Seleccione una opción:\n a. Ver gráficamente el camino para recolectar objetivos de una maqueta\n")

        if sub_opcion == "a":
            nombre_maqueta = input("Ingrese el nombre de la maqueta: ")
            lista_pisos.graficar_camino(nombre_maqueta)
        else:
            print("Opción no válida.")

    elif opcion == "d":
        ayuda()

    elif opcion == "e":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, ingrese un número válido.")