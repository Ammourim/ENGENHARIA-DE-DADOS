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

**Visão Geral e KPIs:**
<img width="1920" height="698" alt="Image" src="https://github.com/user-attachments/assets/fa0257c4-24e3-410e-aaeb-0ff243e90b5a" />
<img width="1920" height="907" alt="Image" src="https://github.com/user-attachments/assets/3bbc1e59-2976-4e40-b1e2-47595ed28cb0" />
<img width="1920" height="914" alt="Image" src="https://github.com/user-attachments/assets/7a223ced-065b-4fb5-8cc8-26af5e8dd199" />

**Análise de Tempo por Setor e Distribuição:**
<img width="1920" height="912" alt="Image" src="https://github.com/user-attachments/assets/19c3e51e-7cd7-44ee-b9d7-9ecbc4f8e607" />
<img width="1920" height="914" alt="Image" src="https://github.com/user-attachments/assets/6106ecb4-3480-4e20-964d-f59226f064e9" />
<img width="1920" height="914" alt="Image" src="https://github.com/user-attachments/assets/be6f21a5-3aa6-4e51-b433-e7272f7a8175" />
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

## Objetivo

Esse projeto foi feito com foco em aprendizado prático, simulando situações reais do dia a dia de um engenheiro de dados, indo desde a extração do dado bruto até a entrega de valor visual para o usuário final.
