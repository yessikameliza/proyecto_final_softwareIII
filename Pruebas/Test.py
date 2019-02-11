import unittest
from logica.Persistence import register_matter
from logica.Persistence import search_matter


class Test(unittest.TestCase):

    def test_registrar_matter(self):
        register_matter("123", "calculo 1", 1, "3", "0", 16)
        a: str = search_matter("123")[2]
        self.assertEqual("calculo 1", a)


if __name__ == "__main__":
    unittest.main()