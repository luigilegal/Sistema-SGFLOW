import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from core.fila import Fila


class TestFila(unittest.TestCase):
    def test_caso_base_enqueue_frente(self):
        fila = Fila()
        fila.enqueue("ABC1D23")
        self.assertEqual(fila.frente(), "ABC1D23")

    def test_caso_vazio_dequeue_gera_erro(self):
        fila = Fila()
        with self.assertRaises(IndexError):
            fila.dequeue()

    def test_multiplos_elementos_fifo(self):
        fila = Fila()
        fila.enqueue("A")
        fila.enqueue("B")
        fila.enqueue("C")
        self.assertEqual(fila.dequeue(), "A")
        self.assertEqual(fila.dequeue(), "B")
        self.assertEqual(fila.frente(), "C")


if __name__ == "__main__":
    unittest.main()
