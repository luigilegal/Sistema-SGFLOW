class Pilha:
    """Pilha LIFO usada para controlar as cargas de um caminhão."""

    def __init__(self, itens=None):
        self._itens = list(itens) if itens else []

    def push(self, item):
        self._itens.append(item)

    def pop(self):
        if self.esta_vazia():
            raise IndexError("Pilha vazia. Não há carga para remover.")

        return self._itens.pop()

    def peek(self):
        if self.esta_vazia():
            return None

        return self._itens[-1]

    def esta_vazia(self):
        return len(self._itens) == 0

    def exibir(self):
        return self._itens.copy()

    def topo_primeiro(self):
        return list(reversed(self._itens))
