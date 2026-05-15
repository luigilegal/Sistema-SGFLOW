import os
import sys
import unittest
#area de testes ordenação
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from core.ordenacao import bubble_sort_rotas, insertion_sort_rotas


class TestOrdenacao(unittest.TestCase):
    def setUp(self):
        self.rotas = [
            {"destino": "Santos", "distancia": 110},
            {"destino": "Suzano", "distancia": 18},
            {"destino": "Guarulhos", "distancia": 47},
        ]

    def test_bubble_sort_ordena_por_distancia(self):
        ordenadas = bubble_sort_rotas(self.rotas)
        self.assertEqual([r["distancia"] for r in ordenadas], [18, 47, 110])

    def test_insertion_sort_ordena_por_distancia(self):
        ordenadas = insertion_sort_rotas(self.rotas)
        self.assertEqual([r["distancia"] for r in ordenadas], [18, 47, 110])

    def test_lista_vazia(self):
        self.assertEqual(bubble_sort_rotas([]), [])
        self.assertEqual(insertion_sort_rotas([]), [])


if __name__ == "__main__":
    unittest.main()
