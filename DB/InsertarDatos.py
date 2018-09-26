# enconding: utf-8
# IMPORTANTE convertir el script a la codificación UTF-8
import sqlite3
from logica.Matter import Matter
from logica.Docent import Docent


def insertMatter(matter: Matter):
    conexion = sqlite3.connect("DateBases.sqlite3")

    # Seleccionar el cursor para iniciar una consulta
    consulta = conexion.cursor()

    print("**** Programa para insertar datos en bases de datos sqlite3 ****")
    # TypeBlock = input("tipo de bloque: ")
    codigo = matter.codigo
    name = matter.name
    ubi_Semester = matter.ubi_Semester
    numCredit = matter.numCredit
    codRequisite = matter.codRequisite
    numHoursSem = matter.numHoursSem
    # Capturar excepciones para los números enteros y decimal
    # Sólo números enteros
    try:
        ubi_Semester = int(ubi_Semester)
    except ValueError:
        print(ubi_Semester, "no es un número entero")
        exit()

    # Valor de los argumentos
    argumentos = (codigo, name, ubi_Semester, numCredit, codRequisite, numHoursSem)
    # argumentos2 = TypeBlock
    # consulta SQL con argumentos ?, ?, ?, ?, ?
    # sql2 = """INSERT INTO block (TypeBlock)
    # VALUES (?)"""
    sql = """INSERT INTO matter (codigo, name, ubi_Semester, numCredit, codRequisite, numHoursSem)
    VALUES (?, ?, ?, ?, ?, ?)"""
    sql2 = """SELECT * FROM matter WHERE codigo = codigo """
    consulta.execute(sql2)

    # Realizar la consulta
    filas = consulta.fetchall()
    if filas is None:
        if consulta.execute(sql, argumentos):
            print("Tabla creada con éxito")
        else:
            print("Ha ocurrido un error al crear la tabla")
    else:
        print("la materia ya existe")

    # Cerrar la consulta
    consulta.close()

    # Guardar los cambios en la base de datos
    conexion.commit()

    # Cerrar la conexión
    conexion.close()


def insertDocent(docent: Docent):
    conexion = sqlite3.connect("DateBases.sqlite3")

    # Seleccionar el cursor para iniciar una consulta
    consulta = conexion.cursor()

    print("**** Programa para insertar datos en bases de datos sqlite3 ****")
    # TypeBlock = input("tipo de bloque: ")

    name = docent.name
    state = docent.state
    limitHours = docent.limitHours
    contract = docent.contract
    phone = docent.phone
    identification = docent.identification
    # Capturar excepciones para los números enteros y decimal
    # Sólo números enteros
    # Valor de los argumentos
    argumentos = (name, state, limitHours, contract, phone, identification)
    # argumentos2 = TypeBlock
    # consulta SQL con argumentos ?, ?, ?, ?, ?
    # sql2 = """INSERT INTO block (TypeBlock)
    # VALUES (?)"""
    sql = """INSERT INTO docent (name, state, limitHours, contract, phone, identification)
    VALUES (?, ?, ?, ?, ?, ?)"""
    sql2 = """SELECT * FROM docent WHERE identification = identification """
    consulta.execute(sql2)

    # Realizar la consulta
    filas = consulta.fetchall()
    if filas is None:
        if consulta.execute(sql, argumentos):
            print("Tabla creada con éxito")
        else:
            print("Ha ocurrido un error al crear la tabla")
    else:
        print("la materia ya existe")

    # Cerrar la consulta
    consulta.close()

    # Guardar los cambios en la base de datos
    conexion.commit()

    # Cerrar la conexión
    conexion.close()
