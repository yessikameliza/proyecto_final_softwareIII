# enconding: utf-8
# IMPORTANTE convertir el script a la codificación UTF-8
import sqlite3

def insertmatter(codigo: str, name: str, ubisemester: int, numcredit: str, codrequisite: str, numhourssem: int):
    conexion = sqlite3.connect("dataBase.sqlite3")

    # Seleccionar el cursor para iniciar una consulta
    consulta = conexion.cursor()

    print("**** Programa para insertar datos en bases de datos sqlite3 ****")

    # Capturar excepciones para los números enteros y decimal
    # Sólo números enteros
    try:
        ubisemester = int(ubisemester)
    except ValueError:
        print(ubisemester, "no es un número entero")
        exit()

    # Valor de los argumentos
    argumentos = (codigo, name, ubisemester, numcredit, codrequisite, numhourssem)

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


def insert_docent(name: str, state: str, limithours: int, contract: str, phone: str, identification: str, matter: str,
                  city: str):
    conexion = sqlite3.connect("dataBase.sqlite3")

    # Seleccionar el cursor para iniciar una consulta
    consulta = conexion.cursor()

    # TypeBlock = input("tipo de bloque: ")
    # Capturar excepciones para los números enteros y decimal
    # Sólo números enteros
    # Valor de los argumentos
    argumentos = (name, state, limithours, contract, phone, identification, matter, city)
    # argumentos2 = TypeBlock
    # consulta SQL con argumentos ?, ?, ?, ?, ?
    # sql2 = """INSERT INTO block (TypeBlock)
    # VALUES (?)"""
    sql = """INSERT INTO docent (name, estate, limitHoras, contract, phone, identification, matter, city)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
    #sql2 = """SELECT * FROM docent WHERE identification = identification """
    # consulta.execute(sql2)

    # Realizar la consulta
    # filas = consulta.fetchall()
    # if filas is None:
    if consulta.execute(sql, argumentos):
        print("docente insertado")
    else:
        print("Ha ocurrido un error al crear la tabla")

    # Cerrar la consulta
    consulta.close()

    # Guardar los cambios en la base de datos
    conexion.commit()

    # Cerrar la conexión
    conexion.close()


def insert_date(date: str, origin: str, idblock: int, idents: str):
    conexion = sqlite3.connect("dataBase.sqlite3")

    # Seleccionar el cursor para iniciar una consulta
    consulta = conexion.cursor()
    print("**** Programa para insertar datos en bases de datos sqlite3 ****")

    # Capturar excepciones para los números enteros y decimal
    # Sólo números enteros
    # Valor de los argumentos
    argumentos = (date, origin, idblock, idents)
    sql = """INSERT INTO date (Date, origin, id_block, idents)
    VALUES (?, ?, ?, ?)"""

    # Realizar la consulta
    if consulta.execute(sql, argumentos):
        print(date)
        print("Tabla creada con éxito")
    else:
        print("Ha ocurrido un error al crear la tabla")

    # Cerrar la consulta
    consulta.close()

    # Guardar los cambios en la base de datos
    conexion.commit()

    # Cerrar la conexión
    conexion.close()
def insertarhora():
    conexion = sqlite3.connect("dataBase.sqlite3")
    # Seleccionar el cursor para iniciar una consulta
    consulta = conexion.cursor()
    print("**** Programa para insertar datos en bases de datos sqlite3 ****")
    horainicio = input("Introduzca la hora inicio: ")
    horafin = input("Introduzca la hora fin: ")
    argumentos = (horainicio, horafin)
    sql = """INSERT INTO hour(hour_ini, hour_fin)
    VALUES(?, ?)"""
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

def insertar_block():
    conexion = sqlite3.connect("dataBase.sqlite3")
    # Seleccionar el cursor para iniciar una consulta
    consulta = conexion.cursor()
    print("**** Programa para insertar datos en bases de datos sqlite3 ****")
    num = input("Introduzca el id ")
    horainicio = input("Introduzca el bloque ")
    argumentos = (num, horainicio)
    sql = """INSERT INTO block(id_block, TypeBlock)
            VALUES(?, ?)"""
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
