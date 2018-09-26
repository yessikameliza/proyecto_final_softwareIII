# enconding: utf-8
# IMPORTANTE codificar el script en UTF-8
import sqlite3

conexion = sqlite3.connect("DB\DateBases.sqlite3")

consulta = conexion.cursor()
sql2 = """UPDATE matter SET numHoursSem = 16 where id_Matter = 1"""
sql3 = """UPDATE matter SET numHoursSem = 16 where id_Matter = 2"""
sql4 = """UPDATE matter SET numHoursSem = 16 where id_Matter = 3"""
sql5 = """UPDATE matter SET numHoursSem = 16 where id_Matter = 4"""
sql6 = """UPDATE matter SET numHoursSem = 16 where id_Matter = 5"""
sql7 = """UPDATE matter SET numHoursSem = 16 where id_Matter = 6"""
sql8 = """UPDATE matter SET numHoursSem = 16 where id_Matter = 7"""
sql9 = """UPDATE matter SET numHoursSem = 16 where id_Matter = 8"""
sql10 = """UPDATE matter SET numHoursSem = 32 where id_Matter = 9"""
sql11 = """UPDATE matter SET numHoursSem = 16 where id_Matter = 10"""
sql12 = """UPDATE matter SET numHoursSem = 12 where id_Matter = 11"""
sql13 = """UPDATE matter SET numHoursSem = 28 where id_Matter = 12"""
sql14 = """UPDATE matter SET numHoursSem = 16 where id_Matter = 13"""
sql15 = """UPDATE matter SET numHoursSem = 16 where id_Matter = 14"""
sql16 = """UPDATE matter SET numHoursSem = 16 where id_Matter = 15"""
sql17 = """UPDATE matter SET numHoursSem = 16 where id_Matter = 16"""
sql18 = """UPDATE matter SET numHoursSem = 12 where id_Matter = 17"""
sql19 = """UPDATE matter SET numHoursSem = 12 where id_Matter = 18"""
consulta.execute(sql2)
consulta.execute(sql3)
consulta.execute(sql4)
consulta.execute(sql5)
consulta.execute(sql6)
consulta.execute(sql7)
consulta.execute(sql8)
consulta.execute(sql9)
consulta.execute(sql10)
consulta.execute(sql11)
consulta.execute(sql12)
consulta.execute(sql13)
consulta.execute(sql14)
consulta.execute(sql15)
consulta.execute(sql16)
consulta.execute(sql17)
consulta.execute(sql18)
consulta.execute(sql19)
consulta.close()
conexion.commit()
conexion.close()

