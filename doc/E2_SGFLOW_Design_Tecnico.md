# Design Técnico e MVP 


## Identificação do Grupo

| Campo | Preenchimento |
|---|---|
| Nome do projeto | SGFLOW — Sistema de Gerenciamento de Fluxos Logísticos |
| Repositório GitHub | https://github.com/luigilegal/Sistema-SGFLOW |
| Integrante 1 | LUIGI SANTOS CAIRES — RGM 45722285 |
| Integrante 2 | MARCOS VINICIUS SANTANA SILVA - RGM 45638390 |

---

## 1. Escolha e Justificativa das Estruturas de Dados

### Estrutura 1 — Fila FIFO

**Nome completo e categoria:** Fila FIFO — estrutura linear.

| Operação | Tempo | Espaço | Observação |
|---|---:|---:|---|
| Inserção / enqueue | O(1) | O(1) | Insere caminhão no final da fila. |
| Remoção / dequeue | O(n) | O(1) | Remove o primeiro elemento com `pop(0)`, deslocando os demais. |
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
├── doc/
│   └── E2_SGFLOW_Design_Tecnico.md
├── README.md
└── .gitignore
```

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

acesse o site: https://sistema-sgflow.onrender.com

      ou

```
pip install -r requirements.txt
python src/ui/app.py
```

### Como executar testes

```
python -m unittest discover tests
```

---

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
