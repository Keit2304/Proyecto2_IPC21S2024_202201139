import os
import xml.etree.ElementTree as ET

class Maqueta:
    def __init__(self, nombre, filas, columnas, entrada_fila, entrada_columna, objetivos, estructura):
        self.nombre = nombre
        self.filas = int(filas)
        self.columnas = int(columnas)
        self.entrada_fila = int(entrada_fila)
        self.entrada_columna = int(entrada_columna)
        self.objetivos = objetivos
        self.estructura = estructura

class Objetivo:
    def __init__(self, nombre, fila, columna):
        self.nombre = nombre
        self.fila = int(fila)
        self.columna = int(columna)

def cargar_archivo_xml(nombre_archivo):
    try:
        tree = ET.parse(nombre_archivo)
        root = tree.getroot()

        maquetas = []

        for maqueta_xml in root.findall('maquetas/maqueta'):
            nombre = maqueta_xml.find('nombre')
            if nombre is not None and nombre.text is not None:
                nombre = nombre.text
            else:
                print("Error: El nombre de la maqueta no está definido correctamente.")
                continue

            filas = maqueta_xml.find('filas')
            if filas is not None and filas.text is not None:
                filas = filas.text
            else:
                print(f"Error: Las filas de la maqueta '{nombre}' no están definidas correctamente.")
                continue

            columnas = maqueta_xml.find('columnas')
            if columnas is not None and columnas.text is not None:
                columnas = columnas.text
            else:
                print(f"Error: Las columnas de la maqueta '{nombre}' no están definidas correctamente.")
                continue

            entrada_fila = maqueta_xml.find('entrada/fila')
            if entrada_fila is not None and entrada_fila.text is not None:
                entrada_fila = entrada_fila.text
            else:
                print(f"Error: La fila de entrada de la maqueta '{nombre}' no está definida correctamente.")
                continue

            entrada_columna = maqueta_xml.find('entrada/columna')
            if entrada_columna is not None and entrada_columna.text is not None:
                entrada_columna = entrada_columna.text
            else:
                print(f"Error: La columna de entrada de la maqueta '{nombre}' no está definida correctamente.")
                continue

            objetivos = []
            for objetivo_xml in maqueta_xml.findall('objetivos/objetivo'):
                nombre_objetivo = objetivo_xml.find('nombre')
                if nombre_objetivo is not None and nombre_objetivo.text is not None:
                    nombre_objetivo = nombre_objetivo.text
                else:
                    print(f"Error: El nombre de un objetivo de la maqueta '{nombre}' no está definido correctamente.")
                    continue

                fila_objetivo = objetivo_xml.find('fila')
                if fila_objetivo is not None and fila_objetivo.text is not None:
                    fila_objetivo = fila_objetivo.text
                else:
                    print(f"Error: La fila de un objetivo de la maqueta '{nombre}' no está definida correctamente.")
                    continue

                columna_objetivo = objetivo_xml.find('columna')
                if columna_objetivo is not None and columna_objetivo.text is not None:
                    columna_objetivo = columna_objetivo.text
                else:
                    print(f"Error: La columna de un objetivo de la maqueta '{nombre}' no está definida correctamente.")
                    continue

                objetivo = Objetivo(nombre_objetivo, fila_objetivo, columna_objetivo)
                objetivos.append(objetivo)

            estructura = maqueta_xml.find('estructura')
            if estructura is not None and estructura.text is not None:
                estructura = estructura.text
            else:
                print(f"Error: La estructura de la maqueta '{nombre}' no está definida correctamente.")
                continue

            maqueta = Maqueta(nombre, filas, columnas, entrada_fila, entrada_columna, objetivos, estructura)
            maquetas.append(maqueta)

            # Imprimir la información de la maqueta y sus objetivos
            print(f"\nMaqueta: {maqueta.nombre}")
            print(f"Filas: {maqueta.filas}")
            print(f"Columnas: {maqueta.columnas}")
            print(f"Entrada: ({maqueta.entrada_fila}, {maqueta.entrada_columna})")
            print("Objetivos:")
            for objetivo in maqueta.objetivos:
                print(f"  {objetivo.nombre} ({objetivo.fila}, {objetivo.columna})")
            print(f"Estructura:\n{maqueta.estructura}")

        print(f"\nSe cargó correctamente el archivo {nombre_archivo}")
    except Exception as e:
        print(f"Error al cargar el archivo {nombre_archivo}: {e}")

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
