import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from service.sgflow_service import SGFlowService


def linha():
    print("-" * 70)


def menu():
    print("\n======================SGFLOW ===========================")
    print("Sistema de Gerenciamento de Fluxos Logísticos")
    print("Empresa: TranStrek")
    linha()
    print("1  - Cadastrar caminhão na fila")
    print("2  - Ver próximo caminhão")
    print("3  - Atender próximo caminhão")
    print("4  - Exibir fila de caminhões")
    print("5  - Empilhar carga")
    print("6  - Desempilhar carga")
    print("7  - Exibir pilha de cargas")
    print("8  - Cadastrar rota")
    print("9  - Exibir rotas cadastradas")
    print("10 - Ordenar rotas por Bubble Sort")
    print("11 - Ordenar rotas por Insertion Sort")
    print("12 - Carregar dados dos arquivos TXT")
    print("0  - Sair")
    linha()


def exibir_caminhao(c):
    if c is None:
        print("Nenhum caminhão disponível.")
    else:
        print(f"Placa: {c['placa']} | Motorista: {c['motorista']} | Operação: {c['operacao']} | Destino: {c['destino']}")


def exibir_fila(service):
    fila = service.listar_caminhoes()
    linha()
    print("ESTADO ATUAL DA FILA DE CAMINHÕES")
    linha()
    if not fila:
        print("Fila vazia.")
    for i, c in enumerate(fila, start=1):
        print(f"{i}. {c['placa']} | {c['motorista']} | {c['operacao']} | {c['destino']}")


def exibir_pilha(service):
    pilha = service.listar_cargas()
    linha()
    print("ESTADO ATUAL DA PILHA DE CARGAS")
    print("Topo da pilha aparece por último na lista abaixo.")
    linha()
    if not pilha:
        print("Pilha vazia.")
    for i, carga in enumerate(pilha, start=1):
        print(f"{i}. {carga['codigo']} | {carga['descricao']} | {carga['peso']} kg")


def exibir_rotas(rotas):
    linha()
    print("ROTAS")
    linha()
    if not rotas:
        print("Nenhuma rota cadastrada.")
    for i, r in enumerate(rotas, start=1):
        print(f"{i}. {r['origem']} -> {r['destino']} | {r['distancia']} km")


def carregar_todos_txt(service):
    arquivos = {
        "caminhões": os.path.join(PROJECT_ROOT, "data", "caminhoes.txt"),
        "cargas": os.path.join(PROJECT_ROOT, "data", "cargas.txt"),
        "rotas": os.path.join(PROJECT_ROOT, "data", "rotas.txt"),
    }
    print(service.carregar_caminhoes_txt(arquivos["caminhões"])[1])
    print(service.carregar_cargas_txt(arquivos["cargas"])[1])
    print(service.carregar_rotas_txt(arquivos["rotas"])[1])


def main():
    service = SGFlowService()

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            placa = input("Placa: ")
            motorista = input("Motorista: ")
            operacao = input("Operação (Carga/Descarga): ")
            destino = input("Destino: ")
            print(service.cadastrar_caminhao(placa, motorista, operacao, destino)[1])
            exibir_fila(service)

        elif opcao == "2":
            print("Próximo caminhão:")
            exibir_caminhao(service.proximo_caminhao())

        elif opcao == "3":
            sucesso, mensagem, caminhao = service.atender_caminhao()
            print(mensagem)
            if sucesso:
                exibir_caminhao(caminhao)
            exibir_fila(service)

        elif opcao == "4":
            exibir_fila(service)

        elif opcao == "5":
            codigo = input("Código da carga: ")
            descricao = input("Descrição: ")
            peso = input("Peso: ")
            print(service.empilhar_carga(codigo, descricao, peso)[1])
            exibir_pilha(service)

        elif opcao == "6":
            sucesso, mensagem, carga = service.desempilhar_carga()
            print(mensagem)
            exibir_pilha(service)

        elif opcao == "7":
            exibir_pilha(service)

        elif opcao == "8":
            origem = input("Origem: ")
            destino = input("Destino: ")
            distancia = input("Distância em km: ")
            print(service.cadastrar_rota(origem, destino, distancia)[1])
            exibir_rotas(service.listar_rotas())

        elif opcao == "9":
            exibir_rotas(service.listar_rotas())

        elif opcao == "10":
            exibir_rotas(service.ordenar_rotas_bubble())

        elif opcao == "11":
            exibir_rotas(service.ordenar_rotas_insertion())

        elif opcao == "12":
            carregar_todos_txt(service)
            exibir_fila(service)
            exibir_pilha(service)
            exibir_rotas(service.listar_rotas())

        elif opcao == "0":
            print("Encerrando o SGFLOW. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()
