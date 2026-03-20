# Projeto de Engenharia de Dados — Dados Hospitalares

## Sobre o projeto

Esse projeto foi criado com o objetivo de praticar conceitos fundamentais de engenharia de dados usando um cenário simples de atendimentos hospitalares.

A ideia é simular um fluxo real:

* dados brutos
* limpeza
* modelagem
* armazenamento
* (futuramente) pipeline automatizado

---

## Estrutura do projeto

```
projeto-dados-hospital/
│
├── data/
│   ├── raw/
│   │   └── atendimentos.csv
│
├── src/
│   ├── limpeza.py
│   ├── modelagem.py
│
├── README.md
└── pyproject.toml
```

---

## O que já foi feito

### 1. Limpeza de dados

Foram tratados alguns problemas comuns:

* valores nulos em campos obrigatórios
* padronização de texto (ex: nomes de setores)
* remoção de duplicados
* tratamento de valores negativos
* identificação de outliers

Sobre os outliers:

* não foram removidos
* foi criada uma coluna `eh_outlier` para marcar esses casos

A ideia foi manter o dado original e deixar a decisão para análise depois.

---

### 2. Modelagem

Os dados foram separados em:

**Tabela fato (atendimentos)**
Contém os eventos:

* id_atendimento
* id_paciente
* id_setor
* tempo_espera_min
* data_atendimento
* eh_outlier

**Dimensão pacientes**

* id_paciente
* paciente_nome

**Dimensão setores**

* id_setor
* setor

Para isso:

* removi duplicados para criar entidades únicas
* gerei IDs
* usei merge para relacionar os dados

---

### 3. Validação

Antes de seguir, validei:

* ausência de valores nulos nas chaves
* ausência de IDs duplicados
* consistência dos dados

---

## Próximos passos

* criar as tabelas no banco de dados
* inserir os dados via Python
* escrever queries SQL
* montar um pipeline automatizado

---

## Tecnologias

* Python
* Pandas
* Poetry
* (em breve) PostgreSQL

---

## Observações

Esse projeto é focado em aprendizado, então algumas decisões foram simplificadas.
A ideia é evoluir ele aos poucos até chegar mais próximo de um cenário real.

---

## Autor

Alan Amorim
