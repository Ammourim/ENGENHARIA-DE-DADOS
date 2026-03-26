# 🏥 Pipeline de Dados — Atendimento Hospitalar

## Sobre o projeto

Esse projeto foi desenvolvido com o objetivo de simular, na prática, o trabalho de um engenheiro de dados em um cenário hospitalar.

A ideia foi pegar dados brutos de atendimentos, tratar, organizar e armazenar em um banco de dados, deixando tudo pronto para análise.

---

## O que foi feito

### 📥 Leitura dos dados

Os dados foram lidos a partir de um arquivo CSV utilizando Python e Pandas.

---

### 🧹 Limpeza dos dados

Nessa etapa, fiz alguns tratamentos importantes:

* Remoção de valores nulos em colunas essenciais
* Substituição de valores inválidos (ex: tempos negativos)
* Padronização de textos (como nomes de setores)
* Identificação de valores fora do padrão (outliers)
* Criação de uma coluna (`eh_outlier`) para marcar esses casos

---

### 🧱 Modelagem

Os dados foram organizados em três tabelas:

* **pacientes**
* **setores**
* **atendimentos**

A tabela de atendimentos faz ligação com as outras duas usando chaves estrangeiras, garantindo consistência.

---

### 🗄️ Banco de dados

Utilizei PostgreSQL para armazenar os dados.

* Criação das tabelas via Python
* Uso de chave primária e estrangeira
* Inserção dos dados com `psycopg2`
* Tratamento de duplicidade com `ON CONFLICT`

---

### 🔍 Validação

Depois de inserir os dados, fiz algumas verificações:

* Conferência de nulos
* Verificação de duplicidade
* Checagem de integridade entre tabelas

---

### 📊 Análise com SQL

Uma das análises feitas foi o tempo médio de espera por setor:

```sql
SELECT 
    s.setor,
    ROUND(AVG(a.tempo_espera_min), 2) AS tempo_medio
FROM atendimentos a
JOIN setores s ON a.id_setor = s.id_setor
WHERE a.eh_outlier = false
GROUP BY s.setor
ORDER BY tempo_medio DESC;
```

**Resultado:**

* Ortopedia → ~49 min
* Emergência → ~40 min
* Clínica → ~18 min

---

## O que aprendi com esse projeto

* A importância de tratar dados antes de analisar
* Como modelar dados de forma relacional
* Como garantir consistência usando chaves estrangeiras
* Que um pipeline funcionando não significa dados confiáveis
* A importância de validar sempre os resultados

---

## Tecnologias utilizadas

* Python
* Pandas
* PostgreSQL
* psycopg2

---

## Próximos passos

* Criar um dashboard para visualização dos dados
* Melhorar a forma de inserção (sem usar `iterrows`)
* Automatizar o pipeline
* Testar integração com ferramentas de BI

---

## Objetivo

Esse projeto foi feito com foco em aprendizado prático, simulando situações reais do dia a dia de um engenheiro de dados.
