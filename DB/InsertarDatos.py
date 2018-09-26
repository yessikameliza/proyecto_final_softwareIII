# enconding: utf-8
# IMPORTANTE convertir el script a la codificación UTF-8
import sqlite3

from logica.Date import Date
from logica.Matter import Matter
from logica.Docent import Docent


def insertMatter(codigo: str, name: str, ubi_Semester: int, numCredit: str, codRequisite: str, numHoursSem: int):
    conexion = sqlite3.connect("DateBases.sqlite3")

    # Seleccionar el cursor para iniciar una consulta
    consulta = conexion.cursor()

    print("**** Programa para insertar datos en bases de datos sqlite3 ****")

    # Capturar excepciones para los números enteros y decimal
    # Sólo números enteros
    try:
        ubi_Semester = int(ubi_Semester)
    except ValueError:
        print(ubi_Semester, "no es un número entero")
        exit()

    # Valor de los argumentos
    argumentos = (codigo, name, ubi_Semester, numCredit, codRequisite, numHoursSem)

    sql = """INSERT INTO matter (codigo, name, ubi_Semester, numCredit, codRequisite, numHoursSem)
    VALUES (?, ?, ?, ?, ?, ?)"""
    if consulta.execute(sql, argumentos):
        print("Tabla creada con éxito")
    else:
        print("Ha ocurrido un error al crear la tabla")

    # Cerrar la consulta
    consulta.close()

    # Guardar los cambios en la base de datos
    conexion.commit()

    # Cerrar la conexión
    conexion.close()


def insertDocent(name: str, state: str, limitHours: int, contract: str, phone: str, identification: str):
    conexion = sqlite3.connect("DateBases.sqlite3")

    # Seleccionar el cursor para iniciar una consulta
    consulta = conexion.cursor()

    # TypeBlock = input("tipo de bloque: ")
    # Capturar excepciones para los números enteros y decimal
    # Sólo números enteros
    # Valor de los argumentos
    argumentos = (name, state, limitHours, contract, phone, identification)
    # argumentos2 = TypeBlock
    # consulta SQL con argumentos ?, ?, ?, ?, ?
    # sql2 = """INSERT INTO block (TypeBlock)
    # VALUES (?)"""
    sql = """INSERT INTO docent (name, estate, limitHoras, contract, phone, identification)
    VALUES (?, ?, ?, ?, ?, ?)"""
    sql2 = """SELECT * FROM docent WHERE identification = identification """
    # consulta.execute(sql2)

    # Realizar la consulta
    # filas = consulta.fetchall()
    # if filas is None:
    if consulta.execute(sql, argumentos):
        print("Tabla creada con éxito")
    else:
        print("Ha ocurrido un error al crear la tabla")

    # Cerrar la consulta
    consulta.close()

    # Guardar los cambios en la base de datos
    conexion.commit()

    # Cerrar la conexión
    conexion.close()


def insertDate(date: Date):
    conexion = sqlite3.connect("DB\DateBases.sqlite3")

    # Seleccionar el cursor para iniciar una consulta
    consulta = conexion.cursor()
    print("**** Programa para insertar datos en bases de datos sqlite3 ****")
    datee = date.date
    origin = date.origin
    # Capturar excepciones para los números enteros y decimal
    # Sólo números enteros
    # Valor de los argumentos
    argumentos = (datee, origin)

    sql = """INSERT INTO date (name, state)
    VALUES (?, ?)"""

    # Realizar la consulta
    if consulta.execute(sql, argumentos):
        print("Tabla creada con éxito")
    else:
        print("Ha ocurrido un error al crear la tabla")

    # Cerrar la consulta
    consulta.close()

    # Guardar los cambios en la base de datos
    conexion.commit()

    # Cerrar la conexión
    conexion.close()
