# enconding: utf-8
# IMPORTANTE convertir el script a la codificación UTF-8
import sqlite3

def insertMatter(codigo: str, name: str, ubi_Semester: int, numCredit: str, codRequisite: str, numHoursSem: int):
    conexion = sqlite3.connect("dataBases.sqlite3")

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
    conexion = sqlite3.connect("dataBases.sqlite3")

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


def insertDate(date: str, origin: str, idents: str):
    conexion = sqlite3.connect("dataBases.sqlite3")

    # Seleccionar el cursor para iniciar una consulta
    consulta = conexion.cursor()
    print("**** Programa para insertar datos en bases de datos sqlite3 ****")

    # Capturar excepciones para los números enteros y decimal
    # Sólo números enteros
    # Valor de los argumentos
    argumentos = (date, origin, idents)
    sql = """INSERT INTO date (Date, origin, idents)
    VALUES (?, ?, ?)"""

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

def insertHour():
    conexion = sqlite3.connect("dataBases.sqlite3")

    # Seleccionar el cursor para iniciar una consulta
    consulta = conexion.cursor()
    print("**** Programa para insertar datos en bases de datos sqlite3 ****")
    horaInicio = input("Introduzca la hora inicio: ")
    horaFin = input("Introduzca la hora fin: ")
    argumentos = (horaInicio, horaFin)
    sql = """
    INSERT
    INTO
    hour(hour_ini, hour_fin)
    VALUES(?, ?)"""
     # Realizar la consulta
    if consulta.execute(sql, argumentos):
        print("Tabla creada con éxito")
    else:
        print("Ha ocurrido un error al crear la tabla")
    # Cerrar la consulta
    consulta.close()
    #Guardar los cambios en la base de datos
    conexion.commit()

    # Cerrar la conexión
    conexion.close()