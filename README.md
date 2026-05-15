# SGFLOW 

Nossa méta,trazer melhor fluxo de transporte aos nossos clientes.

## Integrantes

- LUIGI SANTOS CAIRES — RGM 45722285
- MARCOS VINICIUS SANTANA SILVA — RGM 45638390


SGFLOW — Sistema de Gerenciamento de Fluxos Logísticos.


O projeto demonstra **Fila**, **Pilha** e **algoritmos de ordenação manuais** em um cenário logístico.

## O que o projeto faz

- Controla caminhões no pátio usando **Fila FIFO**.
- Controla cargas/paletes usando **Pilha LIFO**.
- Ordena rotas por distância usando **Bubble Sort** e **Insertion Sort** implementados manualmente.
- Lê dados de arquivos `.txt`.
- Possui menu interativo no terminal.
- Possui testes unitários com `unittest`, sem dependências externas.

## Como executar

Na pasta do projeto, rode:

```
python src/ui/main.py
```

Se o comando acima não funcionar, tente:

```
python3 src/ui/main.py
```

se mesmo assim n funcionar execute o arquivo "main.py"

## Como executar os testes

```
python -m unittest discover tests
```

## Estrutura de diretórios

```
Sistema-SGFLOW/
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

## Formatos dos arquivos TXT

### data/caminhoes.txt

```
placa;motorista;operacao;destino
```

### data/cargas.txt

```
codigo;descricao;peso
```

### data/rotas.txt

```
origem;destino;distancia_km
```

