# enconding: utf-8
# IMPORTANTE codificar el script en UTF-8
import sqlite3
from typing import Any, List


def search_matter2(codi: str):
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


def search_docent2(ident: str):
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

def search_docent_matter(matter: str, ciudad: str):
    conexion = sqlite3.connect("dataBases.sqlite3")
    consulta = conexion.cursor()

    # Extrayendo todas las filas
    filaa: Any = None
    sql = "SELECT * FROM docent"
    if consulta.execute(sql):
        files = consulta.fetchall()
        print(files, " profes")
        for fila in files:
            if str(fila[7]) == matter and str(fila[8]) == ciudad:
                    return fila
    consulta.close()

    conexion.commit()
    conexion.close()
    return filaa

def obtener_fechas2(idents: str):
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

def obtener_fecha_indu2(idents: str):
    conexion = sqlite3.connect("dataBases.sqlite3")
    consulta = conexion.cursor()

    # Extrayendo todas las filas
    filaa = []

    sql = "SELECT * FROM date"
    if consulta.execute(sql):
        files = consulta.fetchall()
        for fila in files:
            if str(fila[4]) == idents and str(fila[1]) != "0":
                        filaa.append(fila)

    consulta.close()
    conexion.commit()
    conexion.close()
    return filaa

def obtener_fechas_hour2(idents: str, origin: str):
    conexion = sqlite3.connect("dataBases.sqlite3")
    consulta = conexion.cursor()

    # Extrayendo todas las filas
    filaa= []

    sql = "SELECT * FROM date"
    if consulta.execute(sql):
        files = consulta.fetchall()
        for fila in files:
            if str(fila[4]) == idents and str(fila[2]) == origin and str(fila[1]) != "0":
                        filaa.append(fila)

    consulta.close()
    conexion.commit()
    conexion.close()
    return filaa

def obtener_matter2():
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

def buscar_mater_por_semester(semester):
    conexion = sqlite3.connect("dataBases.sqlite3")
    consulta = conexion.cursor()

    # Extrayendo todas las filas
    filaa: list = []
    sql = "SELECT * FROM matter"
    if consulta.execute(sql):
        files = consulta.fetchall()
        print("hola")
        print(files)
        for fila in files:
            if int(fila[3]) == int(semester):
                filaa.append(fila)
                print(filaa)

    consulta.close()

    conexion.commit()
    conexion.close()
    return filaa

def buscar_hora_inicio_fin():
    conexion = sqlite3.connect("dataBases.sqlite3")
    consulta = conexion.cursor()

    # Extrayendo todas las filas
    filaa: list = []
    sql = "SELECT * FROM hour"
    if consulta.execute(sql):
        files = consulta.fetchall()
        for fila in files:
               filaa.append(fila[1]+"-"+fila[2])

    consulta.close()
    conexion.commit()
    conexion.close()
    return filaa
