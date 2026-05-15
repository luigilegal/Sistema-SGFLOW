class Fila:
    

    def __init__(self):
        self._itens = []

    def enqueue(self, item):
       
        self._itens.append(item)

    def dequeue(self):
        
        if self.esta_vazia():
            raise IndexError("Fila vazia. Nenhum caminhão para atender.")
        return self._itens.pop(0)

    def frente(self):
       
        if self.esta_vazia():
            return None
        return self._itens[0]

    def esta_vazia(self):
        
        return len(self._itens) == 0

    def tamanho(self):
       
        return len(self._itens)

    def exibir(self):
       
        return self._itens.copy()
