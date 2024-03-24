import os
import xml.etree.ElementTree as ET

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        return self.cabeza is None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def mostrar(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente

    def obtener_lista_ordenada(self):
        lista_ordenada = []
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            lista_ordenada.append(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        lista_ordenada.sort(key=lambda maqueta: maqueta.nombre)
        return lista_ordenada

class Maqueta:
    def __init__(self, nombre, filas, columnas, entrada_fila, entrada_columna, estructura):
        self.nombre = nombre
        self.filas = int(filas)
        self.columnas = int(columnas)
        self.entrada_fila = int(entrada_fila)
        self.entrada_columna = int(entrada_columna)
        self.objetivos = ListaEnlazada()
        self.estructura = estructura

class Objetivo:
    def __init__(self, nombre, fila, columna):
        self.nombre = nombre
        self.fila = int(fila)
        self.columna = int(columna)

maquetas_cargadas = ListaEnlazada()

def cargar_archivo_xml(nombre_archivo):
    try:
        tree = ET.parse(nombre_archivo)
        root = tree.getroot()

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

            estructura = maqueta_xml.find('estructura')
            if estructura is not None and estructura.text is not None:
                estructura = estructura.text
            else:
                print(f"Error: La estructura de la maqueta '{nombre}' no está definida correctamente.")
                continue

            maqueta = Maqueta(nombre, filas, columnas, entrada_fila, entrada_columna, estructura)
            maquetas_cargadas.agregar(maqueta)

            print(f"\nMaqueta: {maqueta.nombre}")
            print(f"Filas: {maqueta.filas}")
            print(f"Columnas: {maqueta.columnas}")
            print(f"Entrada: ({maqueta.entrada_fila}, {maqueta.entrada_columna})")
            print("Objetivos:")
            maqueta.objetivos.mostrar()
            print(f"Estructura:\n{maqueta.estructura}")

        print(f"(Cada * representa una PARED y cada - representa un CAMINO)")
        print(f"\nSe cargó correctamente el archivo {nombre_archivo}")

    except Exception as e:
        print(f"Error al cargar el archivo {nombre_archivo}: {e}")


def ver_maquetas_ordenadas():
    lista_ordenada = maquetas_cargadas.obtener_lista_ordenada()
    print("\nListado de maquetas ordenadas alfabéticamente:")
    for maqueta in lista_ordenada:
        print(f"- {maqueta.nombre}")

def graficar_maquetas():
    lista_ordenada = maquetas_cargadas.obtener_lista_ordenada()
    for maqueta in lista_ordenada:
        print(f"\nMaqueta: {maqueta.nombre}")
        estructura = maqueta.estructura.split("\n")
        for fila in estructura:
            print(fila)

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
        print("\nGestión de maquetas:")
        subopcion = input("Ingrese '1' para ver el listado de maquetas ordenadas alfabéticamente, o '2' para graficar las maquetas: ")
        if subopcion == "1":
            ver_maquetas_ordenadas()
        elif subopcion == "2":
            graficar_maquetas()
        else:
            print("Opción inválida.")

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
