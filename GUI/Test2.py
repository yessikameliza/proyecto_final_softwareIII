import unittest
from logica.Persistence import register_matter
from logica.Persistence import search_matter
from logica.Persistence import delete_matter
from logica.Persistence import register_docent
from logica.Persistence import search_docent
from logica.Persistence import delete_docent

class Test(unittest.TestCase):

    def test_register_matter(self):
        register_matter("1233", "caalculo 1", 11, "33", "00", 116)
        a: str = search_matter("1233")[2]
        self.assertEqual(a, "caalculo 1")

    def test_remove_matter(self):
        delete_matter("1233")
        a: str = search_matter("1233")
        self.assertEqual(None, a)

    def test_register_docent(self):
        register_docent("melisa", "activo", 100, "catedratico", "1094970", "32424", "calculo", "Armenia")
        a: str = search_docent("324234")[2]
        self.assertEqual(a, "activo")

    def test_remove_docente(self):
        delete_docent("32424")
        self.assertEqual(None)


if __name__ == "__main__":
    unittest.main()
