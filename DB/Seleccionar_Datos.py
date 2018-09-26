# enconding: utf-8
# IMPORTANTE codificar el script en UTF-8
import sqlite3


def searchMatter(codi: str):
    conexion = sqlite3.connect("dataBases.sqlite3")
    consulta = conexion.cursor()
    # Extrayendo todas las filas
    sql = """SELECT * FROM matter WHERE codigo = %s""" % codi
    if consulta.execute(sql):
        file = consulta.fetchall()

    consulta.close()

    conexion.commit()
    conexion.close()
    return file
