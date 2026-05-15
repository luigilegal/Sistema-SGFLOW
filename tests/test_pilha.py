import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from core.pilha import Pilha


class TestPilha(unittest.TestCase):
    def test_caso_base_push_peek(self):
        pilha = Pilha()
        pilha.push("PAL001")
        self.assertEqual(pilha.peek(), "PAL001")

    def test_caso_vazio_pop_gera_erro(self):
        pilha = Pilha()
        with self.assertRaises(IndexError):
            pilha.pop()

    def test_multiplos_elementos_lifo(self):
        pilha = Pilha()
        pilha.push("A")
        pilha.push("B")
        pilha.push("C")
        self.assertEqual(pilha.pop(), "C")
        self.assertEqual(pilha.pop(), "B")
        self.assertEqual(pilha.peek(), "A")


if __name__ == "__main__":
    unittest.main()
