# enconding: utf-8
# IMPORTANTE codificar el script en UTF-8
import sqlite3

conexion = sqlite3.connect("DateBases.sqlite3")

consulta = conexion.cursor()

# Extrayendo todas las filas
sql = "SELECT numHoursSem FROM matter"
if consulta.execute(sql):
    filas = consulta.fetchall()
    for fila in filas:
        print(fila[0])

consulta.close()

conexion.commit()
conexion.close()
