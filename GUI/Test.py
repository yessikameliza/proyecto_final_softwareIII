import unittest
from logica.Persistence import register_matter
from logica.Persistence import search_matter
from logica.Persistence import delete_matter


class Test(unittest.TestCase):

    def test_registrar_matter(self):
        register_matter("1233", "caalculo 1", 11, "33", "00", 116)
        a: str = search_matter("1233")[2]
        self.assertEqual(a, "caalculo 1")

    dep test
if __name__ == "__main__":
    unittest.main()
