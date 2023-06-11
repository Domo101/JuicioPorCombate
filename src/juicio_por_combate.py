import sys
import json


def guardar_jugador(fichero, jugador):
    """guarda la jugador en un fichero"""
    # escribir en un archivo

    # w: para escribir en el
    # r: para leer
    # +: para crearlo si no existe
    archivo = open(fichero, "w+")

    # pasamos la jugador a un string en formato json
    jugador_en_json = json.dumps(jugador, indent=2)

    # lo enchuflamos al archivo
    archivo.write(jugador_en_json)

    # cerramos archivo
    archivo.close()


def cargar_jugador(archivo):
    """cargar la jugador desde un fichero"""
    try:
        archivo = open(archivo, "r")

        # leemos el archivo
        jugador_en_json = archivo.read()

        # pasar el string a un array
        jugador = json.loads(jugador_en_json)

        # cerramos el archivo
        archivo.close()

    except FileNotFoundError:
        print("No se ha encontrado bd.json, creando nuevo jugador")
        return {}

    # retornamos el array de la jugador
    return jugador


jugador = cargar_jugador(sys.argv[1])

print(f"Jugador: {json.dumps(jugador)}")
