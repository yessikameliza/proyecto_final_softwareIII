import unittest
from logica.Persistence import register_matter
from logica.Persistence import search_matter
from logica.Persistence import register_docent
from logica.Persistence import register_date
from logica.Persistence import obtener_fechas_p
from logica.Persistence import update_docent
from logica.Persistence import search_docent
from logica.Persistence import update_matter

from logica.Persistence import delete_docent

from logica.Persistence import delete_matter
from logica.Persistence import delete_docent
from logica.Persistence import delete_date


class Test(unittest.TestCase):

    def test_register_matter(self):
        register_matter("1233", "caalculo 1", 11, "33", "00", 116)
        a: str = search_matter("1233")[2]
        self.assertEqual(a, "caalculo 1")


    def test_register_docent(self):
        register_docent("melisa", "activo", 100, "catedratico", "1094970", "324234", "calculo", "Armenia")
        a = search_docent("324234")[1]
        self.assertEqual(a, "melisa")

    def test_delete_matter(self):
        delete_matter("1233")
        print("NO existe ya: "+str(search_matter("1233")))

    def test_delete_docent(self):
        delete_docent("324234")
        print("NO existe: " + str(search_matter("324234")))

   ## def test_register_fechas(self):
     #   register_date("11/02/2019", "13/04/2018", 1, "Primeras fechas")
      #  auxi = obtener_fechas_p("11/02/2019", "13/04/2018")
       # for aux in auxi:
        #    aux2 = str((aux[2]))
         #   print(aux2)
          #  self.assertEqual(aux2, "13/04/2018")
   # def test_delete_fechas(self):
    #    delete_date()

    def test_actualizar_docente(self):
        register_docent("Alexander", "Activo", 300, "Ocasional", "3229491208", "1054565199", "Estadistica", "Pereira")
        update_docent("Alexander", "Inactivo", 300, "Ocasional", "3229491208", "1054565199", "Estadistica", "Pereira")
        aux: str = search_docent("1054565199")[2]
        self.assertEqual(aux, "Inactivo")
        delete_docent("1054565199")

    def test_actualizar_materia(self):
        register_matter("1001", "Fundamentos en obras", 4, "3", "1234567", 240)
        update_matter("1001", "Fundamentos en obras civiles", 5, "3", "1234567", 260)
        aux: str = search_matter("1001")[2]
        self.assertEqual(aux, "Fundamentos en obras civiles")
        delete_matter("1001")


    def test_eliminar_docente(self):
         register_docent("Alberto José", "Activo", 200, "Catedratico", "3206697975", "1000","Calculo 2", "Armenia")
         delete_docent("1000")
         aux: str = search_docent("1000")[6]
         self.assertEqual(aux, "1000")


if __name__ == "__main__":
    unittest.main()
