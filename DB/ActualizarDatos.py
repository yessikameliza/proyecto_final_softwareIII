# enconding: utf-8
# IMPORTANTE codificar el script en UTF-8
import sqlite3
from DB.InsertarDatos import insert_date


def update_matter1(codigo: str, name: str, ubisemester: int, numcredit: str, codrequisite: str, numhourssem: int):
    conexion = sqlite3.connect("dataBase.sqlite3")

    consulta = conexion.cursor()
    id: int
    sql1 = "SELECT * FROM matter"
    if consulta.execute(sql1):
        files = consulta.fetchall()
        for fila in files:
            if str(fila[1]) == codigo:
                id = int(fila[0])
    arg = (codigo, name, ubisemester, numcredit, codrequisite, numhourssem, id)
    sql = """UPDATE matter SET codigo = ?, name = ?, ubi_Semester = ?, numCredit = ?, codRequisite = ?, numHoursSem = ?
      WHERE id_Matter = ? """

    consulta.execute(sql, arg)

    print("actualizo")
    consulta.close()
    conexion.commit()
    conexion.close()


def update_docent1(name, state, limithours, contract, phone, identification, matter, city):
    conexion = sqlite3.connect("dataBase.sqlite3")
    consulta = conexion.cursor()
    id: int = None
    sql1 = "SELECT * FROM docent"
    if consulta.execute(sql1):
        files = consulta.fetchall()
        for fila in files:

            if str(fila[6]) == identification:
                id = int(fila[0])
                print(id)

    arg = (name, state, limithours, contract, phone, identification, matter, city, id)
    sql = """UPDATE docent SET name = ?, estate = ?, limitHoras = ?, contract = ?, phone = ?, identification = ?,
     matter= ?, city= ?
      WHERE id_Docent = ? """

    if consulta.execute(sql, arg):
        print("se actualizo el docente")
    else:
        print("no actualizo")

    print("actualizo")
    consulta.close()
    conexion.commit()
    conexion.close()

def update_b_ma1(nombre: str, idblock: int):
    conexion = sqlite3.connect("dataBase.sqlite3")
    consulta = conexion.cursor()
    sql1 = "SELECT * FROM matter"
    if consulta.execute(sql1):
        files = consulta.fetchall()
        for fila in files:

            if str(fila[2]) == nombre:
                arg = (idblock, fila[0])
                sql = """UPDATE matter SET id_block = ?
                          WHERE id_Matter = ? """
                if consulta.execute(sql, arg):
                    print("se actualizo el docente")
                else:
                    print("no actualizo")

    print("actualizo")
    consulta.close()
    conexion.commit()
    conexion.close()

def update_date1(date: str, origin: str, idblock: int, idents: str):
    insert_date(date, origin, idblock, idents)
