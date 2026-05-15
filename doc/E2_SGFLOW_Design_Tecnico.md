# Design Técnico e MVP — E2

**Disciplina:** Estrutura de Dados  
**Prazo:** 15/05  
**Peso:** 25% da nota final 

## Identificação do Grupo

| Campo | Preenchimento |
|---|---|
| Nome do projeto | SGFLOW — Sistema de Gerenciamento de Fluxos Logísticos |
| Repositório GitHub | https://github.com/luigilegal/Sistema-SGFLOW |
| Integrante 1 | LUIGI SANTOS CAIRES — RGM 45722285 |
| Integrante 2 | MARCOS VINICIUS SANTANA SILVA — RGM 45638390 |

---

# 1. Escolha e Justificativa das Estruturas de Dados

## Estrutura 1 — Fila

**Nome completo e categoria:** Fila FIFO — estrutura linear.

**Complexidade das operações principais:**

| Operação | Tempo | Espaço | Observação |
|---|---:|---:|---|
| Inserção / enqueue | O(1) | O(1) | Insere caminhão no final da fila. |
| Remoção / dequeue | O(n) | O(1) | Remove o primeiro elemento com `pop(0)`, deslocando os demais. |
| Busca | O(n) | O(1) | Em caso de busca por placa, seria necessário percorrer a fila. |
| Acesso / frente | O(1) | O(1) | Consulta o primeiro caminhão sem remover. |

**Justificativa de escolha:**  
A fila foi escolhida para representar a ordem de chegada dos caminhões no pátio logístico. O primeiro caminhão que chega deve ser o primeiro atendido, caracterizando o comportamento FIFO.

**Alternativa descartada:** Pilha — foi descartada para caminhões porque a pilha atenderia primeiro o último caminhão que chegou, o que seria injusto no pátio.

**Limitações conhecidas:** A remoção com lista Python usando `pop(0)` tem custo O(n), pois os elementos precisam ser deslocados.

**Referência bibliográfica:** CORMEN, Thomas H. et al. *Introduction to Algorithms*. 3. ed. MIT Press, 2009.

---

## Estrutura 2 — Pilha

**Nome completo e categoria:** Pilha LIFO — estrutura linear.

**Complexidade das operações principais:**

| Operação | Tempo | Espaço | Observação |
|---|---:|---:|---|
| Inserção / push | O(1) | O(1) | Insere carga no topo. |
| Remoção / pop | O(1) | O(1) | Remove carga do topo. |
| Busca | O(n) | O(1) | Buscar uma carga específica exige percorrer a pilha. |
| Acesso / peek | O(1) | O(1) | Consulta a carga do topo sem remover. |

**Justificativa de escolha:**  
A pilha foi escolhida para representar cargas empilhadas. A última carga colocada no topo é a primeira a ser retirada, seguindo o comportamento LIFO.

**Alternativa descartada:** Fila — foi descartada para cargas empilhadas porque uma fila removeria a carga mais antiga primeiro, o que não representa a retirada pelo topo.

**Limitações conhecidas:** Acesso direto a uma carga no meio da pilha não é eficiente, pois exige percorrer os elementos.

**Referência bibliográfica:** ZIVIANI, Nivio. *Projeto de Algoritmos com Implementações em Pascal e C*. 3. ed. Cengage Learning, 2011.

---

## Estrutura 3 — Lista de Rotas com Ordenação Manual

**Nome completo e categoria:** Lista sequencial — estrutura linear.

**Complexidade das operações principais:**

| Operação | Tempo | Espaço | Observação |
|---|---:|---:|---|
| Inserção | O(1) | O(1) | Insere rota no final da lista. |
| Remoção | O(n) | O(1) | Pode exigir busca e deslocamento. |
| Busca | O(n) | O(1) | Busca sequencial por destino. |
| Acesso por índice | O(1) | O(1) | Acesso direto pelo índice. |
| Bubble Sort | O(n²) | O(1) | Ordenação manual por distância. |
| Insertion Sort | O(n²) | O(1) | Ordenação manual por distância. |

**Justificativa de escolha:**  
A lista foi escolhida para armazenar rotas porque permite inserir várias opções de origem, destino e distância. As rotas podem ser ordenadas por distância para ajudar o operador a visualizar os trajetos menores.

**Alternativa descartada:** Dicionário — foi descartado como estrutura principal porque o objetivo da etapa é demonstrar ordenação manual sobre uma sequência de elementos.

**Limitações conhecidas:** A busca é linear e os algoritmos Bubble Sort e Insertion Sort têm custo O(n²), podendo ficar lentos com muitos dados.

**Referência bibliográfica:** GOODRICH, Michael T.; TAMASSIA, Roberto; GOLDWASSER, Michael H. *Data Structures and Algorithms in Python*. Wiley, 2013.

---

# 2. Arquitetura em Camadas

## Diagrama

```
+-----------------------------+
| Apresentação / UI / CLI      |
| src/ui/main.py               |
| Menu, entradas e saídas      |
+--------------+--------------+
               |
               v
+-----------------------------+
| Aplicação / Service          |
| src/service/sgflow_service.py|
| Validação e regras do SGFLOW |
+--------------+--------------+
               |
               v
+-----------------------------+
| Domínio / Core               |
| src/core/fila.py             |
| src/core/pilha.py            |
| src/core/ordenacao.py        |
+-----------------------------+
```

## Descrição das camadas

| Camada | Nome no projeto | Responsabilidade |
|---|---|---|
| Apresentação | `src/ui/main.py` | Exibe o menu, recebe dados do usuário e mostra resultados. |
| Aplicação | `src/service/sgflow_service.py` | Valida entradas e chama as operações do núcleo. |
| Domínio | `src/core/` | Implementa Fila, Pilha e algoritmos de ordenação. |

**Como as camadas se comunicam:**  
A UI recebe a opção digitada pelo usuário e chama o Service. O Service valida os dados e chama as estruturas no Core. O Core executa a operação e retorna o resultado. O Service devolve a resposta para a UI exibir na tela.

---

# 3. Estrutura de Diretórios

```
/
├── src/
│   ├── core/
│   │   ├── fila.py
│   │   ├── pilha.py
│   │   └── ordenacao.py
│   ├── service/
│   │   └── sgflow_service.py
│   └── ui/
│       └── main.py
├── tests/
│   ├── test_fila.py
│   ├── test_pilha.py
│   └── test_ordenacao.py
├── data/
│   ├── caminhoes.txt
│   ├── cargas.txt
│   └── rotas.txt
├── doc/
│   └── E2_SGFLOW_Design_Tecnico.md
├── README.md
└── .gitignore
```

**Justificativa de desvios:** Nenhum desvio. A estrutura segue o modelo sugerido.

---

# 4. Backlog do Projeto

## In-Scope — O que será implementado

**Item 1: Cadastrar caminhão na fila**  
Critério de aceite: **Dado** um caminhão com placa, motorista, operação e destino, **quando** o usuário cadastrar pelo menu, **então** o sistema adiciona o caminhão ao final da fila e exibe a fila atualizada.

**Item 2: Atender próximo caminhão**  
Critério de aceite: **Dado** uma fila com caminhões, **quando** o usuário escolher atender próximo, **então** o sistema remove o primeiro caminhão da fila e exibe o estado atualizado.

**Item 3: Empilhar carga**  
Critério de aceite: **Dado** uma carga com código, descrição e peso, **quando** o usuário empilhar a carga, **então** o sistema adiciona a carga no topo da pilha e exibe a pilha atualizada.

**Item 4: Desempilhar carga**  
Critério de aceite: **Dado** uma pilha com cargas, **quando** o usuário escolher desempilhar, **então** o sistema remove a carga do topo e exibe a pilha atualizada.

**Item 5: Ordenar rotas por distância**  
Critério de aceite: **Dado** uma lista de rotas cadastradas, **quando** o usuário escolher Bubble Sort ou Insertion Sort, **então** o sistema exibe as rotas ordenadas por distância.

**Item 6: Carregar dados por TXT**  
Critério de aceite: **Dado** arquivos TXT válidos em `data/`, **quando** o usuário escolher carregar dados, **então** o sistema lê caminhões, cargas e rotas e exibe os estados atualizados.

## Out-of-Scope — O que não será implementado

| Funcionalidade | Motivo de exclusão |
|---|---|
| Interface Web | Será implementada em uma etapa futura para melhorar a apresentação visual. |
| Banco de dados | A etapa pede MVP simples e leitura de arquivo; banco aumentaria a complexidade. |
| Login de usuários | Não contribui diretamente para avaliação de estruturas de dados. |
| Integração com mapas/GPS | Depende de APIs externas e foge do escopo acadêmico da etapa. |

---

# 5. Repositório GitHub

**Link do repositório:** https://github.com/luigilegal/Sistema-SGFLOW.

## Checklist do repositório

- Repositório público com nome descritivo.ok
- `.gitignore` configurado para Python.ok
- `README.md` com descrição e instruções de execução.ok
- Mínimo de 5 commits semânticos.ok

## Como executar

```
python src/ui/main.py
```

## Como executar testes

```
python -m unittest discover tests
```

---

# 6. Implementação do Núcleo

## 6.1 Estrutura implementada: Fila

**Linguagem:** Python 3  
**Localização:** `src/core/fila.py`

| Operação | Implementada? | Observação |
|---|---|---|
| enqueue | ok | Insere caminhão no final da fila. |
| dequeue | ok | Remove caminhão do início da fila. |
| frente | ok | Consulta o primeiro caminhão sem remover. |
| esta_vazia | ok | Verifica se a fila está vazia. |

## 6.2 Estrutura implementada: Pilha

**Linguagem:** Python 3  
**Localização:** `src/core/pilha.py`

| Operação | Implementada? | Observação |
|---|---|---|
| push | ok | Insere carga no topo da pilha. |
| pop | ok | Remove carga do topo da pilha. |
| peek | ok | Consulta a carga do topo sem remover. |
| esta_vazia | ok | Verifica se a pilha está vazia. |

## 6.3 Algoritmos implementados: Ordenação

**Linguagem:** Python 3  
**Localização:** `src/core/ordenacao.py`

| Algoritmo | Implementado? | Observação |
|---|---|---|
| Bubble Sort | ok | Ordena rotas por distância. |
| Insertion Sort | ok | Ordena rotas por distância. |

## Trecho representativo do código

```python
def dequeue(self):
    if self.esta_vazia():
        raise IndexError("Fila vazia. Nenhum caminhão para atender.")
    return self._itens.pop(0)
```

## Leitura de arquivo

O sistema lê arquivos TXT na pasta `data/`.

- `data/caminhoes.txt`: `placa;motorista;operacao;destino`
- `data/cargas.txt`: `codigo;descricao;peso`
- `data/rotas.txt`: `origem;destino;distancia_km`

---

# 7. MVP — Mínimo Produto Viável

## 7.1 Tipo de interface

- CLI: linha de comando.

## 7.2 Tela 1 — Boas-vindas / Menu Principal

**Descrição:** Ao iniciar, o usuário vê o nome do sistema e as operações disponíveis.

```
============================== SGFLOW ==============================
Sistema de Gerenciamento de Fluxos Logísticos
1  - Cadastrar caminhão na fila
2  - Ver próximo caminhão
3  - Atender próximo caminhão
...
0  - Sair
```

## 7.3 Tela 2 — Entrada de Dados

**Descrição:** O usuário informa dados pelo terminal.

```
Placa: ABC1D23
Motorista: Carlos Souza
Operação: Carga
Destino: São Paulo
```

Também há opção de carregar arquivos TXT pelo menu.

## 7.4 Tela 3 — Resultado

**Descrição:** O sistema exibe o resultado e o estado atual das estruturas.

```
Caminhão ABC1D23 adicionado ao final da fila.
ESTADO ATUAL DA FILA DE CAMINHÕES
1. ABC1D23 | Carlos Souza | Carga | São Paulo
```

Para operação inválida:

```
Fila vazia. Nenhum caminhão para atender.
```

## 7.5 Fluxo completo demonstrado

**Cenário:** Usuário carrega dados TXT, visualiza fila, atende caminhão, empilha carga e ordena rotas.

```
Escolha uma opção: 12
4 caminhões carregados do arquivo TXT.
4 cargas carregadas do arquivo TXT.
5 rotas carregadas do arquivo TXT.

Escolha uma opção: 3
Caminhão ABC1D23 atendido e removido da fila.

Escolha uma opção: 10
Rotas exibidas em ordem crescente de distância usando Bubble Sort.
```

---

# 8. Testes Unitários

**Framework utilizado:** `unittest`  
**Localização:** `tests/`

## Estrutura testada: Fila

- Teste 1 — Caso base: verifica `enqueue` e `frente`. Resultado: ok Passando.
- Teste 2 — Caso vazio: verifica erro ao executar `dequeue` em fila vazia. Resultado: ok Passando.
- Teste 3 — Múltiplos elementos: verifica comportamento FIFO. Resultado: ok Passando.

## Estrutura testada: Pilha

- Teste 1 — Caso base: verifica `push` e `peek`. Resultado: ok Passando.
- Teste 2 — Caso vazio: verifica erro ao executar `pop` em pilha vazia. Resultado: ok Passando.
- Teste 3 — Múltiplos elementos: verifica comportamento LIFO. Resultado: ok Passando.

## Algoritmos testados: Ordenação

- Teste 1 — Bubble Sort ordena rotas por distância. Resultado: ok Passando.
- Teste 2 — Insertion Sort ordena rotas por distância. Resultado: ok Passando.
- Teste 3 — Lista vazia retorna lista vazia. Resultado: ok Passando.

---

# Checklist de Autoavaliação

- Big-O preenchido para cada estrutura: ok
- Alternativa descartada com justificativa: ok
- Limitações conhecidas: ok
- Arquitetura em 3 camadas: ok
- Estrutura de diretórios: ok
- Backlog com In-Scope e Out-of-Scope: ok
- Repositório GitHub previsto: ok
- Núcleo implementado: ok
- Leitura TXT funcionando: ok
- MVP com menu, entrada e resultado: ok
- Testes unitários: ok
