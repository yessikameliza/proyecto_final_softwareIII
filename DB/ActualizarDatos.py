# enconding: utf-8
# IMPORTANTE codificar el script en UTF-8
import sqlite3


def upDate_Matter(codigo: str, name: str, ubi_Semester: int, numCredit: str, codRequisite: str, numHoursSem: int):
    conexion = sqlite3.connect("dataBases.sqlite3")

    consulta = conexion.cursor()
    # sql2 = """UPDATE matter
    # SET (codigo, name, ubi_Semester, numCredit, codRequisite, numHoursSem) WHERE codigo = 1 """
    id: int
    sql1 = "SELECT * FROM matter"
    if consulta.execute(sql1):
        files = consulta.fetchall()
        for fila in files:
            if str(fila[1]) == codigo:
                id = int(fila[0])
    arg = (codigo, name, ubi_Semester, numCredit, codRequisite, numHoursSem, id)
    sql = """UPDATE matter SET codigo = ?, name = ?, ubi_Semester = ?, numCredit = ?, codRequisite = ?, numHoursSem = ?
      WHERE id_Matter = ? """

    consulta.execute(sql, arg)

    print("actualizo")
    consulta.close()
    conexion.commit()
    conexion.close()
def updateDocent(name, state, limitHours, contract, phone, identification):
    conexion = sqlite3.connect("dataBases.sqlite3")
    consulta = conexion.cursor()
    # sql2 = """UPDATE matter
    # SET (codigo, name, ubi_Semester, numCredit, codRequisite, numHoursSem) WHERE codigo = 1 """
    id: int
    sql1 = "SELECT * FROM docent"
    if consulta.execute(sql1):
        files = consulta.fetchall()
        for fila in files:
            if str(fila[1]) == identification:
                id = int(fila[6])
    arg = (name, state, limitHours, contract, phone, identification, id)
    sql = """UPDATE docent SET name = ?, estate = ?, limitHours = ?, contract = ?, phone = ?, identification = ?
      WHERE id_Docent = ? """

    consulta.execute(sql, arg)

    print("actualizo")
    consulta.close()
    conexion.commit()
    conexion.close()
