# enconding: utf-8
# IMPORTANTE codificar el script en UTF-8
import sqlite3


def delete_matter1(codigo: str):
    conexion = sqlite3.connect("dataBase.sqlite3")

    consulta = conexion.cursor()
    # SET (codigo, name, ubi_Semester, numCredit, codRequisite, numHoursSem) WHERE codigo = 1 """
    ident: int = -1
    sql1 = "SELECT * FROM matter"
    if consulta.execute(sql1):
        files = consulta.fetchall()
        for fila in files:
            print("entrp")
            if str(fila[1]) == codigo:
                ident = fila[0]
    if -1 != ident:
        id = int(ident)
        sql = "DELETE FROM matter WHERE id_Matter = ? AND codigo = ?"
        argumentos = (ident, codigo)
        consulta.execute(sql, argumentos)

    print("actualizo")
    consulta.close()
    conexion.commit()
    conexion.close()
    return ident


def delete_docent1(identification: str):
    conexion = sqlite3.connect("dataBase.sqlite3")

    consulta = conexion.cursor()
    # sql2 = """UPDATE matter
    id: int = None
    sql1 = "SELECT * FROM docent"
    if consulta.execute(sql1):
        files = consulta.fetchall()
        for fila in files:
            if str(fila[6]) == identification:
                id = int(fila[0])

    if not None == id:
        ident = str(id)
        sql = "DELETE FROM docent WHERE id_Docent = ? and identification = ?"
        argumentos = (id, identification)
        consulta.execute(sql, argumentos)

    print("actualizo")
    consulta.close()
    conexion.commit()
    conexion.close()
    return id


def delete_date1():
    conexion = sqlite3.connect("dataBase.sqlite3")
    consulta = conexion.cursor()
    sql1 = "DELETE FROM date"
    if consulta.execute(sql1):
        print("elimino fechas")
    print("entro aqui")
    consulta.close()
    conexion.commit()
    conexion.close()
