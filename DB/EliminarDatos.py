# enconding: utf-8
# IMPORTANTE codificar el script en UTF-8
import sqlite3


def deleteMatter(codigo: str):
    conexion = sqlite3.connect("dataBases.sqlite3")

    consulta = conexion.cursor()
    # sql2 = """UPDATE matter
    # SET (codigo, name, ubi_Semester, numCredit, codRequisite, numHoursSem) WHERE codigo = 1 """
    id: int = None
    sql1 = "SELECT * FROM matter"
    if consulta.execute(sql1):
        files = consulta.fetchall()
        for fila in files:
            if str(fila[1]) == codigo:
                id = int(fila[0])

    if not None == id:
        ident = str(id)
        sql = "DELETE FROM matter WHERE id_Matter = ?"
        consulta.execute(sql, ident)

    print("actualizo")
    consulta.close()
    conexion.commit()
    conexion.close()
    return id
