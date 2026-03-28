# Pipeline de Dados — Atendimento Hospitalar

## Sobre o projeto

Esse projeto foi desenvolvido com o objetivo de simular, na prática, o trabalho de um engenheiro de dados em um cenário hospitalar.

A ideia foi pegar dados brutos de atendimentos, tratar, organizar, armazenar em um banco de dados relacional e, por fim, disponibilizar essas informações em um dashboard interativo para análise de performance.

---

## O que foi feito

### Leitura dos dados
Os dados foram lidos a partir de um arquivo CSV utilizando Python e Pandas.

### Limpeza dos dados
Nessa etapa, fiz alguns tratamentos importantes:
* Remoção de valores nulos em colunas essenciais
* Substituição de valores inválidos (ex: tempos negativos)
* Padronização de textos (como nomes de setores)
* Identificação de valores fora do padrão (outliers)
* Criação de uma coluna (`eh_outlier`) para marcar esses casos

### Modelagem
Os dados foram organizados em três tabelas: **pacientes**, **setores** e **atendimentos**. A tabela de atendimentos faz ligação com as outras duas usando chaves estrangeiras, garantindo consistência.

### Banco de dados
Utilizei PostgreSQL para armazenar os dados de forma robusta:
* Conexão e gerenciamento via **SQLAlchemy** (substituindo o uso cru do psycopg2).
* Criação das tabelas via Python de forma automatizada.

### Dashboard Analítico (Streamlit)
Desenvolvimento de uma interface web para consumo dos dados:
* Filtros dinâmicos por setor na barra lateral.
* KPIs em tempo real (Tempo Médio, Total de Atendimentos, Pacientes Únicos).
* Gráficos interativos utilizando **Plotly** (Gráfico de barras horizontais para médias e Histograma para distribuição do tempo de espera).
* Conexão direta com o banco PostgreSQL via cache (`@st.cache_data`) para otimizar o carregamento.

---

## Visuais do Dashboard
img/image-1.png img/image-2.png img/image-3.png img/image-4.png img/image-5.png img/image.png


**Visão Geral e KPIs:**
`[Insira sua imagem aqui]`

**Análise de Tempo por Setor e Distribuição:**
`[Insira sua imagem aqui]`

---

## O que aprendi com esse projeto

* A importância de tratar dados antes de analisar.
* Como modelar dados de forma relacional e garantir consistência usando chaves estrangeiras.
* A evolução de scripts simples para bibliotecas de ORM e conexão de alto nível (SQLAlchemy).
* Como construir visualizações de dados interativas direto do Python com Streamlit e Plotly.
* Gestão de ambientes virtuais e dependências utilizando **Poetry**.

---

## Tecnologias utilizadas

* **Python** (Pandas, python-dotenv)
* **PostgreSQL** (Banco de Dados)
* **SQLAlchemy & psycopg2** (Conexão e ORM)
* **Streamlit** (Criação do Dashboard Web)
* **Plotly** (Visualização de Dados)
* **Poetry** (Gerenciamento de Pacotes e Ambiente Virtual)

---

## Próximos passos (Evolução do Projeto)

* **Orquestração:** Automatizar o pipeline de ETL utilizando ferramentas como Apache Airflow ou Mage.ai.
* **Containerização:** Colocar a aplicação e o banco de dados em containers Docker para facilitar a execução em qualquer máquina.
* **Deploy Cloud:** Hospedar o banco de dados (ex: AWS RDS) e o Streamlit (Streamlit Cloud ou Render) para acesso público.

---

## Objetivo

Esse projeto foi feito com foco em aprendizado prático, simulando situações reais do dia a dia de um engenheiro de dados, indo desde a extração do dado bruto até a entrega de valor visual para o usuário final.