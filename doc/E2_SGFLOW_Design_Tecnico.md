<<<<<<< HEAD
# Design Técnico e MVP — E2

**Disciplina:** Estrutura de Dados  
**Prazo:** 15/05  
**Peso:** 25% da nota final 
=======
# Design Técnico e MVP 

>>>>>>> a9c0f52 (docs: atualiza documentação final do SGFLOW)

## Identificação do Grupo

| Campo | Preenchimento |
|---|---|
| Nome do projeto | SGFLOW — Sistema de Gerenciamento de Fluxos Logísticos |
| Repositório GitHub | https://github.com/luigilegal/Sistema-SGFLOW |
| Integrante 1 | LUIGI SANTOS CAIRES — RGM 45722285 |
<<<<<<< HEAD
| Integrante 2 | MARCOS VINICIUS SANTANA SILVA — RGM 45638390 |

---

# 1. Escolha e Justificativa das Estruturas de Dados

## Estrutura 1 — Fila

**Nome completo e categoria:** Fila FIFO — estrutura linear.

**Complexidade das operações principais:**

=======
| Integrante 2 | MARCOS VINICIUS SANTANA SILVA - RGM 45638390 |

---

## 1. Escolha e Justificativa das Estruturas de Dados

### Estrutura 1 — Fila FIFO

**Nome completo e categoria:** Fila FIFO — estrutura linear.

>>>>>>> a9c0f52 (docs: atualiza documentação final do SGFLOW)
| Operação | Tempo | Espaço | Observação |
|---|---:|---:|---|
| Inserção / enqueue | O(1) | O(1) | Insere caminhão no final da fila. |
| Remoção / dequeue | O(n) | O(1) | Remove o primeiro elemento com `pop(0)`, deslocando os demais. |
<<<<<<< HEAD
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
=======
| Busca por ID | O(n) | O(1) | Percorre a fila até encontrar o caminhão. |
| Acesso à frente | O(1) | O(1) | Consulta o primeiro caminhão sem remover. |

**Justificativa:** a fila representa a ordem de chegada dos caminhões no pátio. O primeiro caminhão que entra é o primeiro a ser atendido, caracterizando FIFO.

**Alternativa descartada:** pilha, pois atenderia primeiro o último caminhão cadastrado, o que não representa a ordem justa do pátio.

**Limitação conhecida:** a remoção com `pop(0)` em lista Python é O(n), pois os elementos seguintes precisam ser deslocados.

**Referência:** Estruturas de dados e algoritmos: https://www.alura.com.br/ Logística de transporte: https://bsoft.com.br/    base para requisitos: E2_Design_Tecnico_MVP.md

### Estrutura 2 — Pilha LIFO

**Nome completo e categoria:** Pilha LIFO — estrutura linear.

| Operação | Tempo | Espaço | Observação |
|---|---:|---:|---|
| Inserção / push | O(1) | O(1) | Adiciona carga no topo da pilha. |
| Remoção / pop | O(1) | O(1) | Remove carga do topo. |
| Consulta / peek | O(1) | O(1) | Consulta o topo sem remover. |
| Busca | O(n) | O(1) | Exige percorrer a pilha. |

**Justificativa:** a pilha representa as cargas de cada caminhão. Em descarga, a última carga no topo é a primeira a sair. Em carga, os itens são adicionados ao topo.

**Alternativa descartada:** fila, pois a fila removeria a carga mais antiga primeiro e não representaria o comportamento de carga empilhada.

**Limitação conhecida:** não há acesso eficiente a uma carga no meio da pilha.

**Referência:** Estruturas de dados e algoritmos: https://www.alura.com.br/ Logística de transporte: https://bsoft.com.br/     base para requisitos: E2_Design_Tecnico_MVP.md

### Estrutura 3 — Lista de Rotas com Ordenação 

**Nome completo e categoria:** Lista sequencial — estrutura linear.

| Operação | Tempo | Espaço | Observação |
|---|---:|---:|---|
| Inserção | O(1) | O(1) | Insere caminhão liberado ao final da lista. |
| Remoção da primeira rota | O(n) | O(1) | Remove o primeiro caminhão da ordem ativa e desloca os demais. |
| Busca | O(n) | O(1) | Busca sequencial. |
| Bubble Sort | O(n²) | O(1) | Ordena por menor distância em KM. |
| Insertion Sort | O(n²) | O(1) | Ordena por maior distância em KM ao inverter a ordem. |

**Justificativa:** a lista armazena os caminhões liberados para rota. A ordenação por KM permite dois critérios operacionais: menor distância primeiro com Bubble Sort e maior distância primeiro com Insertion Sort. O botão “Inverter Ordem” permite alternar entre esses critérios antes de liberar a partida.

**Alternativa descartada:** dicionário como estrutura principal, pois o requisito exige visualização e ordenação manual sobre uma sequência.

**Limitação conhecida:** Bubble Sort e Insertion Sort são simples e didáticos, mas podem ser lentos com grande volume de dados por possuírem complexidade O(n²).

**Referência:** Estruturas de dados e algoritmos: https://www.alura.com.br/ Logística de transporte: https://bsoft.com.br/     base para requisitos: E2_Design_Tecnico_MVP.md





---

## 2. Arquitetura em Camadas

```
+--------------------------------+
| Apresentação / UI Web          |
| src/ui/app.py                  |
| templates/index.html
| Performance.html               |
| static/css/style.css           |
+---------------+----------------+
                |
                v
+--------------------------------+
| Aplicação / Service             |
| src/service/sgflow_service.py   |
| Regras do SGFLOW                |
+---------------+----------------+
                |
                v
+--------------------------------+
| Domínio / Core                  |
| src/core/fila.py                |
| src/core/pilha.py               |
| src/core/ordenacao.py           |
+--------------------------------+
```

| Camada | Nome no projeto | Responsabilidade |
|---|---|---|
| Apresentação | `src/ui/app.py`, `templates/index.html`, `templates/performance.html`, `static/css/style.css` | Exibe o dashboard operacional, o dashboard de performance, recebe ações do usuário e mostra os resultados. |
| Aplicação | `src/service/sgflow_service.py` | Valida dados e orquestra fila, pilha, rotas, inversão de ordem e métricas de performance. |
| Domínio | `src/core/` | Implementa fila, pilha e algoritmos manuais de ordenação. |

**Comunicação:** a interface web envia os dados para as rotas Flask. As rotas chamam o Service, o Service valida as regras e chama as estruturas do Core. O resultado volta para a tela por mensagens no rodapé, pela atualização dos painéis e pelo registro das métricas no dashboard de performance.



---

## 3. Estrutura de Diretórios
>>>>>>> a9c0f52 (docs: atualiza documentação final do SGFLOW)

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
<<<<<<< HEAD
│       └── main.py
├── tests/
│   ├── test_fila.py
│   ├── test_pilha.py
│   └── test_ordenacao.py
├── data/
│   ├── caminhoes.txt
│   ├── cargas.txt
│   └── rotas.txt
=======
│       ├── app.py
│       ├── templates/
│       │   ├── index.html
│       │   └── performance.html
│       └── static/
│           └── css/
│               └── style.css
├── tests/
│   ├── test_core.py
│   └── test_service.py
├── data/
│   ├── caminhoes_exemplo.csv
│   └── caminhoes_exemplo.xlsx
|
>>>>>>> a9c0f52 (docs: atualiza documentação final do SGFLOW)
├── doc/
│   └── E2_SGFLOW_Design_Tecnico.md
├── README.md
└── .gitignore
```

<<<<<<< HEAD
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
=======
**Justificativa de desvios:** o projeto usa interface web com Flask, por isso há pastas `templates` e `static`.

---

## 4. Backlog do Projeto

### In-Scope

**Item 1: Cadastrar caminhão na fila**

**Dado** um caminhão com placa, motorista, operação, destino e distância, **quando** o usuário clicar no botão `+`, **então** o caminhão será adicionado ao final da fila FIFO.

**Item 2: Atender próximo caminhão**

**Dado** uma fila com caminhões, **quando** o usuário clicar em “Atender próximo da fila”, **então** o primeiro caminhão será removido da fila e colocado em atendimento.

**Item 3: Controlar pilha de cargas**

**Dado** um caminhão em atendimento, **quando** o usuário adicionar ou remover uma carga, **então** o sistema atualizará a pilha LIFO do caminhão.

**Item 4: Liberar caminhão para rota**

**Dado** um caminhão de carga com itens ou um caminhão de descarga vazio, **quando** a operação for finalizada, **então** o caminhão será movido para a lista de rotas.

**Item 5: Ordenar rotas por distância**

**Dado** caminhões liberados para rota, **quando** o sistema exibir a lista, **então** os caminhões aparecerão ordenados por menor KM usando Bubble Sort.

**Item 6: Inverter ordem das rotas**

**Dado** caminhões aguardando liberação para rota, **quando** o usuário clicar em “Inverter Ordem”, **então** o sistema alternará a ordenação para maior KM usando Insertion Sort. Ao clicar novamente, retorna para menor KM usando Bubble Sort.

**Item 7: Importar dados por arquivo**

**Dado** um arquivo CSV ou XLSX válido, **quando** o usuário importar, **então** os caminhões serão adicionados à fila com suas cargas iniciais.

**Item 8: Dashboard de Performance**

**Dado** operações realizadas no sistema, **quando** o usuário acessar o dashboard de performance, **então** serão exibidos registros de operação, algoritmo/estrutura, tempo, volume e memória. A tabela possui barra de rolagem, mantém todas as operações da execução, exibe totais no rodapé e permite limpar ou salvar os dados em arquivo `.txt`.

### Out-of-Scope

| Funcionalidade | Motivo |
|---|---|
| Banco de dados | A etapa foca nas estruturas em memória. |
| Login de usuários | Não é necessário para demonstrar fila, pilha, ordenação e telemetria. |
| Integração com mapas/GPS | Depende de serviços externos e foge do escopo da etapa. |

---

## 5. Repositório GitHub

**Link:** https://github.com/luigilegal/Sistema-SGFLOW

### Como executar

```
pip install -r requirements.txt
python src/ui/app.py
```

### Como executar testes
>>>>>>> a9c0f52 (docs: atualiza documentação final do SGFLOW)

```
python -m unittest discover tests
```

---

<<<<<<< HEAD
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
=======
## 6. Implementação do Núcleo

### Fila

**Arquivo:** `src/core/fila.py`

| Operação | Implementada? | Observação |
|---|---|---|
| enqueue | Sim | Insere caminhão no final da fila. |
| dequeue | Sim | Remove o primeiro caminhão da fila. |
| frente | Sim | Consulta o primeiro caminhão. |
| esta_vazia | Sim | Verifica se a fila está vazia. |

### Pilha

**Arquivo:** `src/core/pilha.py`

| Operação | Implementada? | Observação |
|---|---|---|
| push | Sim | Adiciona carga ao topo. |
| pop | Sim | Remove carga do topo. |
| peek | Sim | Consulta carga do topo. |
| esta_vazia | Sim | Verifica se a pilha está vazia. |

### Ordenação

**Arquivo:** `src/core/ordenacao.py`

| Algoritmo | Implementado? | Uso |
|---|---|---|
| Bubble Sort | Sim | Ordena caminhões liberados por menor distância em KM. |
| Insertion Sort | Sim | Ordena caminhões liberados por maior distância em KM quando o usuário inverte a ordem. |

### Trecho representativo

```python
def ordenar_rotas_por_distancia(rotas, ordem="crescente"):
    if ordem == "decrescente":
        return insertion_sort_rotas_decrescente(rotas)

    return bubble_sort_rotas_crescente(rotas)
```

### Leitura de arquivo

O sistema lê arquivos `.csv` e `.xlsx`. (Ao importar uma base de dados ela cria uma pasta chamada "uploads" onde fica salva as bases de dados importadas anteriormente).

Colunas esperadas:

```
placa,motorista,operacao,destino,distancia,cargas
```

As cargas são separadas por `|`.

#### Métricas de Performance

O sistema registra métricas das operações realizadas durante a execução. As métricas armazenam operação, algoritmo/estrutura, tempo de execução, volume de dados e consumo de memória em MB. O cálculo de memória utiliza `tracemalloc`, compatível com Windows, Linux e macOS.

---

## 7. MVP — Mínimo Produto Viável

### Tipo de interface

Interface Web simples com Flask, HTML e CSS.

### Tela 1 — Dashboard principal

Mostra o nome SGFLOW, botão de importação, quantidade de caminhões na fila, painéis de fila/pilha/rotas, botão “Inverter Ordem” e botão de acesso ao dashboard de performance.

### Tela 2 — Entrada de dados

O usuário cadastra caminhão informando placa, motorista, operação, destino, distância e cargas iniciais.

### Tela 3 — Resultado

O sistema exibe o estado atualizado da fila, da pilha e das rotas. As mensagens aparecem no rodapé ao lado do nome SGFLOW.

### Fluxo completo

1. O usuário cadastra ou importa caminhões.
2. O sistema adiciona caminhões à fila FIFO.
3. O usuário atende o próximo caminhão.
4. O sistema exibe a pilha de cargas do caminhão.
5. O usuário descarrega ou adiciona cargas.
6. O caminhão é liberado para rotas.
7. As rotas são ordenadas por distância.

---

## 8. Testes Unitários

**Framework:** `unittest`  
**Localização:** `tests/`

| Teste | Objetivo | Resultado |
|---|---|---|
| Fila FIFO | Verifica se o primeiro item inserido é o primeiro removido. | Passando |
| Pilha LIFO | Verifica se o último item inserido é o primeiro removido. | Passando |
| Bubble Sort | Verifica se as rotas ficam em ordem crescente de distância. | Passando |
| Insertion Sort | Verifica se as rotas ficam em ordem decrescente de distância. | Passando |
| Inversão de ordem | Verifica se o botão/função alterna a ordenação das rotas. | Passando |
| Descarga sem carga | Verifica bloqueio de descarga sem carga inicial. | Passando |
| Descarga completa | Verifica liberação após esvaziar a pilha. | Passando |
| Carga finalizada | Verifica liberação após adicionar carga e finalizar. | Passando |
| Performance | Verifica armazenamento de métricas, totais, média de memória e exportação `.txt`. | Passando |

---

## Checklist de Autoavaliação

- Big-O preenchido para fila, pilha e lista de rotas: Sim.
- Dois algoritmos manuais de ordenação implementados: Sim.
- Alternativas descartadas descritas: Sim.
- Arquitetura em camadas: Sim.
- Backlog com critérios de aceite: Sim.
- Repositório GitHub informado: Sim.
- Núcleo implementado: Sim.
- Leitura de arquivo funcionando: Sim.
- MVP com interface funcionando: Sim.
- Dashboard de performance implementado: Sim.
- Testes unitários documentados: Sim.
>>>>>>> a9c0f52 (docs: atualiza documentação final do SGFLOW)
