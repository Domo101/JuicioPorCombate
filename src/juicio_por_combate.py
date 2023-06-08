import json


def guardar_jugador(jugador):
    """guarda la jugador en un fichero"""
    # escribir en un archivo

    # w: para escribir en el
    # r: para leer
    # +: para crearlo si no existe
    archivo = open("./bd.json", "w+")

    # pasamos la jugador a un string en formato json
    jugador_en_json = json.dumps(jugador, indent=2)

    # lo enchuflamos al archivo
    archivo.write(jugador_en_json)

    # cerramos archivo
    archivo.close()


print("Juicio por combate")
