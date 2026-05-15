class Pilha:
    

    def __init__(self):
        self._itens = []

    def push(self, item):
       
        self._itens.append(item)

    def pop(self):
        
        if self.esta_vazia():
            raise IndexError("Pilha vazia. Nenhuma carga para remover.")
        return self._itens.pop()

    def peek(self):
        
        if self.esta_vazia():
            return None
        return self._itens[-1]

    def esta_vazia(self):
       
        return len(self._itens) == 0

    def tamanho(self):
        
        return len(self._itens)

    def exibir(self):
       
        return self._itens.copy()
