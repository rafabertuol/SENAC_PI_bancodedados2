# 📊 Projeto Integrador — Apoio Decisório aos Negócios

## 🗄️ Banco de Dados MySQL + ETL + OLAP + Streamlit

---

# 📚 **Sumário**

1. [Introdução](#introdução)
2. [Objetivos](#objetivos)

   * 2.1 [Objetivo Geral](#objetivo-geral)
   * 2.2 [Objetivos Específicos](#objetivos-específicos)
3. [Justificativa](#justificativa)
4. [Metodologia](#metodologia)
5. [Tecnologias Utilizadas](#tecnologias-utilizadas)
6. [Estrutura do Banco de Dados](#estrutura-do-banco-de-dados)

   * 6.1 [Modelo Relacional](#modelo-relacional)
   * 6.2 [Modelo Dimensional (Star Schema)](#modelo-dimensional-star-schema)
   * 6.3 [Views Analíticas](#views-analíticas)
7. [Scripts Desenvolvidos](#scripts-desenvolvidos)
8. [Operações OLAP Implementadas](#operações-olap-implementadas)
9. [DataFrames para Streamlit](#dataframes-para-streamlit)
10. [Como Executar](#como-executar)
11. [Validação dos Dados](#validação-dos-dados)
12. [Integrantes](#integrantes)

---

# 🧭 **1. Introdução**

Este projeto integra conceitos de **banco de dados, análise de dados, ETL e BI**.
Utiliza uma base de vendas automotivas para:

* Construir um **banco MySQL**
* Criar um **modelo dimensional**
* Aplicar **consultas OLAP**
* Gerar **DataFrames** para visualização no **Streamlit**

A base contém **470 veículos** com informações de preço, quilometragem, motor, consumo, avaliação e status de venda.

---

# 🎯 **2. Objetivos**

## 2.1 Objetivo Geral

Aplicar técnicas de Business Intelligence para estruturar, analisar e interpretar dados automotivos, gerando insights úteis ao processo decisório.

## 2.2 Objetivos Específicos

* Realizar limpeza e tratamento dos dados
* Investigar atributos de performance e mercado
* Desenvolver análises estatísticas e comparativas
* Criar visualizações e métricas
* Estruturar o banco e pipelines de forma replicável

---

# 📝 **3. Justificativa**

O setor automotivo possui forte competitividade e volume de dados.
A análise é essencial para:

* Compreender padrões de consumo
* Avaliar desvalorização
* Comparar marcas e modelos
* Identificar oportunidades de negócio

Este projeto usa BI para transformar dados brutos em informação estratégica.

---

# 🔍 **4. Metodologia**

A solução foi dividida em etapas:

1. **Modelagem do banco relacional e dimensional**
2. **Criação do banco e tabelas via SQL (DDL)**
3. **Carga e transformação dos dados (DML + Python)**
4. **Implementação de operações OLAP**
5. **Geração de DataFrames para Streamlit**
6. **Validação e análise dos resultados**

---

# 🛠️ **5. Tecnologias Utilizadas**

| Tecnologia                 | Versão | Finalidade                |
| -------------------------- | ------ | ------------------------- |
| **MySQL**                  | 8.0+   | Armazenamento e consultas |
| **Python**                 | 3.11   | ETL e análises            |
| **Pandas**                 | Latest | Manipulação de dados      |
| **mysql-connector-python** | Latest | Interface Python ⇄ MySQL  |
| **Streamlit**              | Latest | Visualização e dashboard  |

---

# 🏗️ **6. Estrutura do Banco de Dados**

## 6.1 **Modelo Relacional**

### Tabela Principal: `car_sales`

Armazena todas as vendas de carros.

| Coluna        | Tipo           | Descrição       |
| ------------- | -------------- | --------------- |
| car_id        | VARCHAR(20) PK | ID único        |
| sale_date     | DATE           | Data da venda   |
| customer_name | VARCHAR(100)   | Nome do cliente |
| gender        | ENUM           | Sexo            |
| annual_income | DECIMAL        | Renda           |
| phone         | BIGINT         | Telefone        |
| dealer_name   | VARCHAR(100)   | Concessionária  |
| dealer_no     | VARCHAR(20)    | Número          |
| dealer_region | VARCHAR(50)    | Região          |
| company       | VARCHAR(50)    | Marca           |
| model         | VARCHAR(100)   | Modelo          |
| body_style    | VARCHAR(30)    | Tipo            |
| engine        | VARCHAR(50)    | Motor           |
| transmission  | VARCHAR(20)    | Câmbio          |
| color         | VARCHAR(30)    | Cor             |
| price         | DECIMAL        | Preço           |

### Índices Criados

* `idx_sale_date`
* `idx_dealer_region`
* `idx_company`
* `idx_model`
* `idx_gender`
* `idx_price`
* `idx_annual_income`

---

## 6.2 **Modelo Dimensional (Star Schema)**

### Dimensões:

* **`dim_time`** – informações temporais
* **`dim_customer`** – dados do cliente
* **`dim_dealer`** – concessionárias
* **`dim_vehicle`** – detalhes do veículo

### Tabela Fato:

**`fact_sales`**

Campos principais:

* chaves das dimensões
* `price`
* `annual_income`
* `financial_effort_ratio`

---

## 6.3 **Views Analíticas**

1. `vw_sales_performance`
2. `vw_sales_by_model`
3. `vw_regional_analysis`
4. `vw_customer_profile`
5. `vw_income_preferences`
6. `vw_dealer_ranking`

---

# 📄 **7. Scripts Desenvolvidos**

## **1. `car_sales_ddl.sql`**

Criação do banco, tabelas e views.

Execução:

```bash
mysql -u root -p < car_sales_ddl.sql
```

## **2. `car_sales_dml.sql`**

Carga e manipulação dos dados.

Execução:

```bash
mysql -u root -p car_sales_db < car_sales_dml.sql
```

## **3. `load_data.py`**

Carga do CSV → MySQL via Python.

Execução:

```bash
python3 load_data.py
```

## **4. `generate_dataframes.py`**

Gera 20 DataFrames para o Streamlit.

Execução:

```bash
python3 generate_dataframes.py
```

---

# 📊 **8. Operações OLAP Implementadas**

Inclui:

* Roll-Up
* Drill-Down
* Slice
* Dice
* Pivot
* Ranking
* ROLLUP()

Consultas incluem análises:

* por modelo, marca, região
* perfil do cliente
* sazonalidade
* ticket médio
* esforço financeiro

---

# 📦 **9. DataFrames para Streamlit**

Foram gerados **20 DataFrames**, organizados em:

### **Vendas (5)**

* df_total
* df_receita_total
* df_vendas_mes
* df_modelos_vendidos
* df_sazonalidade

### **Perfil do Cliente (5)**

* df_agrupar_faixa_renda
* df_genero
* df_renda_x_modelo
* df_preferencias
* df_esforco_financeiro

### **Regional (4)**

* df_receita_regiao
* df_ticket_medio_concessionaria
* df_ranking
* df_comparacao_regioes

### **Extras (6)**

* body_style, transmissão, cor, top marcas, evolução temporal, correlação

### Exemplo de uso no Streamlit:

```python
with open('dataframes.pkl', 'rb') as f:
    dfs = pickle.load(f)

st.metric("Total de Vendas", dfs['df_total']['Valor'][0])
st.dataframe(dfs['df_modelos_vendidos'].head(10))
```

---

# ▶️ **10. Como Executar**

1. Criar banco
2. Executar DDL
3. Executar DML
4. Rodar `load_data.py`
5. Rodar `generate_dataframes.py`
6. Usar arquivos no Streamlit

---

# ✔️ **11. Validação dos Dados**

Foram validados:

* tipos
* chaves
* consistência entre tabelas
* totais entre fato e staging
* integridade referencial
* estatísticas comparativas

---

# 👥 **12. Integrantes**

* Aguinaldo de Marcenes Vieira
* Aline Freire Anholete Morais
* Ana Luisa Andrade Vasconcelos
* Arcanjo Ricardo Souza da Silva
* David Exposito de Carvalho
* Edna Miranda Santana
* Gabriela Carvalho Semensato
* Rafaela Bertuol

---
