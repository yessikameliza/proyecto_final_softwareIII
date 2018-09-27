# enconding: utf-8
# IMPORTANTE codificar el script en UTF-8
import sqlite3
from typing import Any


def searchMatter(codi: str):
    conexion = sqlite3.connect("dataBases.sqlite3")
    consulta = conexion.cursor()

    # Extrayendo todas las filas
    filaa: Any = None
    sql = "SELECT * FROM matter"
    if consulta.execute(sql):
        files = consulta.fetchall()
        for fila in files:
            if str(fila[1]) == codi:
                print("entro aquí")
                filaa = fila

    consulta.close()

    conexion.commit()
    conexion.close()
    return filaa
