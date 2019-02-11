import unittest
from DB.InsertarDatos import insert_matter
from DB.InsertarDatos import insert_docent
from DB.InsertarDatos import insert_date
from DB.Seleccionar_Datos import search_matter2
from DB.ActualizarDatos import update_matter1
from DB.EliminarDatos import delete_matter1
from DB.Seleccionar_Datos import search_docent2
from DB.ActualizarDatos import update_docent1
from DB.EliminarDatos import delete_date1
from DB.Seleccionar_Datos import obtener_fechas2
from DB.EliminarDatos import delete_docent1
from DB.Seleccionar_Datos import obtener_matter2
from DB.Seleccionar_Datos import buscar_mater_por_semester
from DB.Seleccionar_Datos import buscar_hora_inicio_fin
from DB.ActualizarDatos import update_date1
from DB.Seleccionar_Datos import obtener_fechas_hour2
from DB.ActualizarDatos import update_b_ma1
from DB.Seleccionar_Datos import obtener_fecha_indu2
from DB.Seleccionar_Datos import search_docent_matter
from logica.Persistence import register_matter
from logica.Persistence import search_matter


class Test(unittest.TestCase):

    def registrarMatter(self):
        register_matter("123", "calculo 1", 1, "3", "0", 16)
        a: str = search_matter("123")[2]
        self.assertEquals("calculo", a)
