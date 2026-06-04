# Monitoramento de Queimadas em Unidades de Conservação Federais

Aplicação em Python para análise de registros históricos de área queimada em Unidades de Conservação (UCs) federais brasileiras. Desenvolvida como projeto da disciplina de Estruturas de Dados, com foco na aplicação prática de listas ligadas, pilhas, filas, busca linear e Merge Sort sobre dados reais do ICMBio.

---

# Video
[![Ver demonstração no YouTube](https://img.shields.io/badge/YouTube-Ver%20Demonstração-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=OsPviwjvno8)

---

## Tema

Incêndios florestais e focos de calor - monitoramento e análise de ocorrências em áreas de proteção federal.

---

## Origem dos Dados

**Dataset:** [Áreas Queimadas em Unidades de Conservação Federais](https://www.kaggle.com/datasets/dandamb/reas-queimadas-em-ucs-federais) - Kaggle

**Fonte primária:** [ICMBio - Dados Abertos](https://dados.gov.br/dados/conjuntos-dados/incendios-em-unidades-de-conservacao-federais) (acessado em 07/10/2024)

**Arquivo local:** `dados/queimadas_UCs_federais.csv`

| Campo | Descrição                |
|-------|--------------------------|
| UC    | Nome da Unidade de Conservação |
| AREA  | Área queimada (hectares) |
| ANO   | Ano da ocorrência        |

---

## Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| Busca por UC | Localiza todos os registros de uma Unidade de Conservação pelo nome |
| Histórico de buscas | Exibe as consultas realizadas na sessão atual |
| Adição de registros | Insere novas ocorrências sem modificar o arquivo original |
| Remoção de registros | Remove uma ocorrência específica da lista em memória |
| Top 10 maiores queimadas | Ordena por área decrescente e exibe os 10 maiores registros |
| Estatísticas gerais | Total de registros, área total, média por ocorrência e maior ocorrência |
| Gráfico temporal | Evolução da área queimada ao longo do tempo para uma UC específica |
| Comparação entre UCs | Gráfico comparativo com duas ou mais UCs sobrepostas |
| Exportação CSV | Exporta registros de UCs selecionadas para um novo arquivo CSV |

Gráficos gerados são salvos automaticamente em `graficos/`.

---

## Estruturas de Dados

### Lista Ligada - `estruturas/linked_list.py`

Armazena todos os registros carregados do dataset.

Operações: inserção no início, inserção no fim, remoção, busca, exibição, contagem.

### Pilha - `estruturas/pilha.py`

Registra o histórico de buscas realizadas pelo usuário na sessão.

Operações: push, pop, peek, size.

### Fila - `estruturas/fila.py`

Processa as solicitações de exportação para CSV em ordem de chegada.

Operações: enqueue, dequeue, size.

---

## Algoritmos

### Busca Linear — `algoritmos/busca.py`

Percorre a lista ligada comparando o nome de cada UC com o termo buscado. Complexidade O(n).

### Merge Sort — `algoritmos/merge_sort.py`

Ordena os registros por área queimada em ordem decrescente. Utilizado no Top 10 e em relatórios ordenados. Complexidade O(n log n).

---

## Estrutura do Projeto

```
.
├── algoritmos/
│   ├── busca.py
│   └── merge_sort.py
├── dados/
│   └── queimadas_UCs_federais.csv
├── estruturas/
│   ├── fila.py
│   ├── linked_list.py
│   └── pilha.py
├── graficos/
├── models/
│   └── queimada.py
├── utils/
│   ├── conversor.py
│   ├── csv.py
│   ├── estatisticas.py
│   ├── grafico.py
│   └── manipulacao.py
├── main.py
└── requirements.txt
```

---

## Tecnologias

- Python 3
- [Pandas](https://pandas.pydata.org/) — leitura e manipulação do CSV
- [Matplotlib](https://matplotlib.org/) — geração de gráficos

---

## Como Executar

**1. Instalar dependências:**

```bash
pip install -r requirements.txt
```

Ou manualmente:

```bash
pip install pandas matplotlib
```

**2. Executar:**

```bash
python main.py
```

---

## Integrantes

<div align="center">
  <table>
    <tr>
      <td align="center">
        <a href="https://github.com/thejaobiell">
          <img src="https://github.com/thejaobiell.png" width="120px;" alt="João Gabriel Boaventura"/><br>
          <sub><b>João Gabriel Boaventura</b></sub><br>
          <sub>RM554874 • 2ESR</sub>
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/KauaiRosa">
          <img src="https://github.com/KauaiRosa.png" width="120px;" alt="Kauai Rosa de Assis Rocha"/><br>
          <sub><b>Kauai Rosa de Assis Rocha</b></sub><br>
          <sub>RM563256 • 2ESR</sub>
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/TLean07">
          <img src="https://github.com/TLean07.png" width="120px;" alt="Leandro Afonso Silva Santos Junior"/><br>
          <sub><b>Leandro Afonso Silva Santos Junior</b></sub><br>
          <sub>RM561344 • 2ESR</sub>
        </a>
      </td>
    </tr>
  </table>
</div>
