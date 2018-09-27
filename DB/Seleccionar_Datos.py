# enconding: utf-8
# IMPORTANTE codificar el script en UTF-8
import sqlite3
from typing import Any, List


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


def searchDocent(ident: str):
    conexion = sqlite3.connect("dataBases.sqlite3")
    consulta = conexion.cursor()

    # Extrayendo todas las filas
    filaa: Any = None
    sql = "SELECT * FROM docent"
    if consulta.execute(sql):
        files = consulta.fetchall()
        for fila in files:
            if str(fila[6]) == ident:
                print("entro aquí")
                filaa = fila

    consulta.close()

    conexion.commit()
    conexion.close()
    return filaa


def obtenerFechas(idents: str):
    conexion = sqlite3.connect("dataBases.sqlite3")
    consulta = conexion.cursor()

    # Extrayendo todas las filas
    filaa= []

    sql = "SELECT * FROM date"
    if consulta.execute(sql):
        files = consulta.fetchall()
        i = 0
        for fila in files:
            if str(fila[4]) == idents:
                print("entro aquí")
                filaa.append(fila[1])
                i = i + 1

    consulta.close()
    conexion.commit()
    conexion.close()
    return filaa


def obtenerMatter():
    conexion = sqlite3.connect("dataBases.sqlite3")
    consulta = conexion.cursor()

    # Extrayendo todas las filas
    filaa: list = None
    sql = "SELECT * FROM matter"
    if consulta.execute(sql):
        files = consulta.fetchall()
        filaa = files

    consulta.close()

    conexion.commit()
    conexion.close()
    return filaa
