import xml.etree.ElementTree as ET
import os


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
        lista_ordenada = ListaEnlazada()
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            lista_ordenada.agregar(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        return lista_ordenada


class Objetivo:
    def __init__(self, nombre, fila, columna):
        self.nombre = nombre
        self.fila = int(fila)
        self.columna = int(columna)


class Maqueta:
    def __init__(self, nombre, filas, columnas, entrada_fila, entrada_columna, estructura):
        self.nombre = nombre
        self.filas = int(filas)
        self.columnas = int(columnas)
        self.entrada_fila = int(entrada_fila)
        self.entrada_columna = int(entrada_columna)
        self.objetivos = ListaEnlazada()
        self.estructura = estructura

    def agregar_objetivo(self, objetivo):
        self.objetivos.agregar(objetivo)

    def obtener_lista_objetivos(self):
        return self.objetivos.obtener_lista_ordenada()


def cargar_archivo_xml(nombre_archivo):
    maquetas_cargadas = ListaEnlazada()

    try:
        tree = ET.parse(nombre_archivo)
        root = tree.getroot()

        for maqueta_xml in root.findall('maquetas/maqueta'):
            nombre = maqueta_xml.find('nombre')
            if nombre is not None and nombre.text is not None:
                nombre = nombre.text.strip()
            else:
                print("Error: El nombre de la maqueta no está definido correctamente.")
                continue

            filas = maqueta_xml.find('filas')
            if filas is not None and filas.text is not None:
                filas = int(filas.text.strip())
            else:
                print(f"Error: Las filas de la maqueta '{nombre}' no están definidas correctamente.")
                continue

            columnas = maqueta_xml.find('columnas')
            if columnas is not None and columnas.text is not None:
                columnas = int(columnas.text.strip())
            else:
                print(f"Error: Las columnas de la maqueta '{nombre}' no están definidas correctamente.")
                continue

            estructura = maqueta_xml.find('estructura')
            if estructura is not None and estructura.text is not None:
                estructura = estructura.text.strip()
            else:
                print(f"Error: La estructura de la maqueta '{nombre}' no está definida correctamente.")
                continue

            maqueta = Maqueta(nombre, filas, columnas, 0, 0, estructura)

            objetivos_elementos = maqueta_xml.findall('objetivos/objetivo')
            objetivos_lista = ListaEnlazada()
            for objetivo_xml in objetivos_elementos:
                objetivo_nombre = objetivo_xml.find('nombre').text.strip()
                objetivo_fila = int(objetivo_xml.find('fila').text.strip())
                objetivo_columna = int(objetivo_xml.find('columna').text.strip())
                objetivo = Objetivo(objetivo_nombre, objetivo_fila, objetivo_columna)
                maqueta.agregar_objetivo(objetivo)
                objetivos_lista.agregar(objetivo_nombre)

            maquetas_cargadas.agregar(maqueta)

            print(f"\nMaqueta: {maqueta.nombre}")
            print(f"Filas: {maqueta.filas}")
            print(f"Columnas: {maqueta.columnas}")
            print(f"Estructura:\n{maqueta.estructura}")

        print(f"\nSe cargaron correctamente las maquetas del archivo {nombre_archivo}")

    except Exception as e:
        print(f"Error al cargar el archivo {nombre_archivo}: {e}")

    return maquetas_cargadas


def graficar_maqueta_con_graphviz(maqueta):
    contenido = """
    digraph G {
    fontname="Helvetica,Arial,sans-serif"
    graph [
        rankdir = "LR"
    ];
    """

    filas = maqueta.filas
    columnas = maqueta.columnas
    estructura = maqueta.estructura.strip().replace(' ', '')

    contenido_patron = estructura

    contenido += f"""
    // Nodo de la maqueta
    node [shape=plaintext];
    maqueta [label=<
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
        """

    for fila in range(filas):
        contenido += "<TR>\n"
        for columna in range(columnas):
            letra = contenido_patron[(fila * columnas) + columna]
            if letra == '*':
                color = 'black'  # '*' representa una pared
                contenido += f'<TD BGCOLOR="{color}"></TD>\n'
            elif letra == '-':
                color = 'white'  # '-' representa espacio en blanco
                contenido += f'<TD BGCOLOR="{color}"></TD>\n'
            else:
                raise ValueError("Carácter inválido en la estructura de la maqueta")

        contenido += "</TR>\n"

    contenido += """
        </TABLE>
    >];
    """

    contenido += "}\n"

    nombre_archivo = "GraficoMaqueta"

    with open(f"{nombre_archivo}.dot", "w") as archivo_dot:
        archivo_dot.write(contenido)

    comando_dot = f"dot -Tpdf {nombre_archivo}.dot -o {nombre_archivo}.pdf"
    os.system(comando_dot)

    print(f"Archivo PDF '{nombre_archivo}.pdf' creado satisfactoriamente.")


def main():
    while True:
        print("============================================================")
        print("\nMenú:")
        print("a. Cargar un archivo XML de entrada")
        print("b. Gestión de maquetas")
        print("c. Salir")
        print("============================================================")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "a":
            nombre_archivo = input("Ingrese el nombre del archivo XML de entrada: ")
            maquetas = cargar_archivo_xml(nombre_archivo)

        elif opcion == "b":
            print("\nGestión de maquetas:")
            nombre_maqueta = input("Ingrese el nombre de la maqueta que desea graficar: ")
            nodo_actual = maquetas.cabeza
            maqueta_encontrada = False
            while nodo_actual is not None:
                if nodo_actual.dato.nombre.strip() == nombre_maqueta.strip():
                    graficar_maqueta_con_graphviz(nodo_actual.dato)
                    maqueta_encontrada = True
                    break
                nodo_actual = nodo_actual.siguiente
            if not maqueta_encontrada:
                print("Maqueta no encontrada.")

        elif opcion == "c":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, ingrese un número válido.")


if __name__ == "__main__":
    main()
