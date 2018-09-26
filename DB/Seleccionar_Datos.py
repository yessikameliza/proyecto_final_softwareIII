# enconding: utf-8
# IMPORTANTE codificar el script en UTF-8
import sqlite3

conexion = sqlite3.connect("GUI\dataBases.sqlite3")

consulta = conexion.cursor()

# Extrayendo todas las filas
sql = "SELECT * FROM matter"
if consulta.execute(sql):
    filas = consulta.fetchall()
    for fila in filas:
        print(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7])

consulta.close()

conexion.commit()
conexion.close()
