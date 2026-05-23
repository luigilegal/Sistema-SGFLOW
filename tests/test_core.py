import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")

if SRC not in sys.path:
    sys.path.insert(0, SRC)

from core.fila import Fila
from core.pilha import Pilha
from core.ordenacao import bubble_sort_rotas_crescente, insertion_sort_rotas_decrescente


class TestCore(unittest.TestCase):
    def test_fila_fifo(self):
        fila = Fila()
        fila.enqueue("A")
        fila.enqueue("B")
        self.assertEqual(fila.dequeue(), "A")

    def test_pilha_lifo(self):
        pilha = Pilha()
        pilha.push("A")
        pilha.push("B")
        self.assertEqual(pilha.pop(), "B")

    def test_bubble_sort_crescente(self):
        rotas = [{"distancia": 90}, {"distancia": 10}, {"distancia": 40}]
        ordenadas = bubble_sort_rotas_crescente(rotas)
        self.assertEqual([rota["distancia"] for rota in ordenadas], [10, 40, 90])

    def test_insertion_sort_decrescente(self):
        rotas = [{"distancia": 90}, {"distancia": 10}, {"distancia": 40}]
        ordenadas = insertion_sort_rotas_decrescente(rotas)
        self.assertEqual([rota["distancia"] for rota in ordenadas], [90, 40, 10])


if __name__ == "__main__":
    unittest.main()
