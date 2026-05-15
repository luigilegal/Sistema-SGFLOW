import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from core.fila import Fila
from core.pilha import Pilha
from core.ordenacao import bubble_sort_rotas, insertion_sort_rotas


class SGFlowService:
    """Camada de aplicação: valida dados e orquestra as estruturas."""

    def __init__(self):
        self.fila_caminhoes = Fila()
        self.pilha_cargas = Pilha()
        self.rotas = []

    # FILA DE CAMINHÕES
    def cadastrar_caminhao(self, placa, motorista, operacao, destino):
        placa = placa.strip().upper()
        motorista = motorista.strip()
        operacao = operacao.strip().capitalize()
        destino = destino.strip()

        if not placa or not motorista or not operacao or not destino:
            return False, "Erro: todos os campos do caminhão são obrigatórios."

        caminhao = {
            "placa": placa,
            "motorista": motorista,
            "operacao": operacao,
            "destino": destino,
        }
        self.fila_caminhoes.enqueue(caminhao)
        return True, f"Caminhão {placa} adicionado ao final da fila."

    def atender_caminhao(self):
        try:
            caminhao = self.fila_caminhoes.dequeue()
            return True, f"Caminhão {caminhao['placa']} atendido e removido da fila.", caminhao
        except IndexError as erro:
            return False, str(erro), None

    def proximo_caminhao(self):
        return self.fila_caminhoes.frente()

    def listar_caminhoes(self):
        return self.fila_caminhoes.exibir()

    # PILHA DE CARGAS
    def empilhar_carga(self, codigo, descricao, peso):
        codigo = codigo.strip().upper()
        descricao = descricao.strip()

        try:
            peso = float(str(peso).replace(",", "."))
        except ValueError:
            return False, "Erro: peso inválido."

        if not codigo or not descricao:
            return False, "Erro: código e descrição são obrigatórios."

        carga = {"codigo": codigo, "descricao": descricao, "peso": peso}
        self.pilha_cargas.push(carga)
        return True, f"Carga {codigo} empilhada no topo da pilha."

    def desempilhar_carga(self):
        try:
            carga = self.pilha_cargas.pop()
            return True, f"Carga {carga['codigo']} removida do topo da pilha.", carga
        except IndexError as erro:
            return False, str(erro), None

    def topo_carga(self):
        return self.pilha_cargas.peek()

    def listar_cargas(self):
        return self.pilha_cargas.exibir()

    # ROTAS E ORDENAÇÃO
    def cadastrar_rota(self, origem, destino, distancia):
        origem = origem.strip()
        destino = destino.strip()

        try:
            distancia = float(str(distancia).replace(",", "."))
        except ValueError:
            return False, "Erro: distância inválida."

        if not origem or not destino:
            return False, "Erro: origem e destino são obrigatórios."

        rota = {"origem": origem, "destino": destino, "distancia": distancia}
        self.rotas.append(rota)
        return True, f"Rota {origem} -> {destino} cadastrada."

    def listar_rotas(self):
        return self.rotas.copy()

    def ordenar_rotas_bubble(self):
        return bubble_sort_rotas(self.rotas)

    def ordenar_rotas_insertion(self):
        return insertion_sort_rotas(self.rotas)

    # LEITURA TXT
    def carregar_caminhoes_txt(self, caminho):
        if not os.path.exists(caminho):
            return False, f"Erro: arquivo não encontrado: {caminho}"

        total = 0
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(";")
                if len(partes) == 4:
                    sucesso, _ = self.cadastrar_caminhao(partes[0], partes[1], partes[2], partes[3])
                    if sucesso:
                        total += 1
        return True, f"{total} caminhões carregados do arquivo TXT."

    def carregar_cargas_txt(self, caminho):
        if not os.path.exists(caminho):
            return False, f"Erro: arquivo não encontrado: {caminho}"

        total = 0
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(";")
                if len(partes) == 3:
                    sucesso, _ = self.empilhar_carga(partes[0], partes[1], partes[2])
                    if sucesso:
                        total += 1
        return True, f"{total} cargas carregadas do arquivo TXT."

    def carregar_rotas_txt(self, caminho):
        if not os.path.exists(caminho):
            return False, f"Erro: arquivo não encontrado: {caminho}"

        total = 0
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(";")
                if len(partes) == 3:
                    sucesso, _ = self.cadastrar_rota(partes[0], partes[1], partes[2])
                    if sucesso:
                        total += 1
        return True, f"{total} rotas carregadas do arquivo TXT."
