# 📊 Projeto Integrador — Apoio Decisório aos Negócios

## 🗄️ Banco de Dados MySQL + ETL + OLAP + Streamlit

---

# 📚 **Sumário**

1. [Integrantes](#integrantes)
2. [Introdução](#introdução)
3. [Objetivos](#objetivos)
   * 3.1 [Objetivo Geral](#objetivo-geral)
   * 3.2 [Objetivos Específicos](#objetivos-específicos)
4. [Justificativa](#justificativa)
5. [Metodologia](#metodologia)
6. [Tecnologias Utilizadas](#tecnologias-utilizadas)
7. [Estrutura do Banco de Dados](#estrutura-do-banco-de-dados)
   * 7.1 [Modelo Relacional](#modelo-relacional)
   * 7.2 [Modelo Dimensional (Star Schema)](#modelo-dimensional-star-schema)
   * 7.3 [Views Analíticas](#views-analíticas)
8. [Scripts Desenvolvidos](#scripts-desenvolvidos)
9. [Operações OLAP Implementadas](#operações-olap-implementadas)
10. [DataFrames para Streamlit](#dataframes-para-streamlit)
11. [Como Executar](#como-executar)
12. [Validação dos Dados](#validação-dos-dados)

---
# 👥 **1. Integrantes**

* Aguinaldo de Marcenes Vieira
* Aline Freire Anholete Morais
* Ana Luisa Andrade Vasconcelos
* Arcanjo Ricardo Souza da Silva
* David Exposito de Carvalho
* Edna Miranda Santana
* Gabriela Carvalho Semensato
* Rafaela Bertuol

---

# 🧭 **2. Introdução**

Este projeto integra conceitos de **banco de dados, análise de dados, ETL e BI**.
Utiliza uma base de vendas automotivas para:

* Construir um **banco MySQL**
* Criar um **modelo dimensional**
* Aplicar **consultas OLAP**
* Gerar **DataFrames** para visualização no **Streamlit**

**Base de dados:** [Car Sales Report - Kaggle](https://www.kaggle.com/datasets/missionjee/car-sales-report)
A base contém **470 veículos** com informações de preço, quilometragem, motor, consumo, avaliação e status de venda.

---

# 🎯 **3. Objetivos**

## 3.1 Objetivo Geral

Aplicar técnicas de Business Intelligence para estruturar, analisar e interpretar dados automotivos, gerando insights úteis ao processo decisório.

## 3.2 Objetivos Específicos

* Realizar limpeza e tratamento dos dados
* Investigar atributos de performance e mercado
* Desenvolver análises estatísticas e comparativas
* Criar visualizações e métricas
* Estruturar o banco e pipelines de forma replicável

---

# 📝 **4. Justificativa**

O setor automotivo possui forte competitividade e volume de dados. A análise é essencial para:

* Compreender padrões de consumo
* Avaliar desvalorização
* Comparar marcas e modelos
* Identificar oportunidades de negócio

Este projeto usa BI para transformar dados brutos em informação estratégica.

---

# 🔍 **5. Metodologia**

A solução foi dividida em etapas:

1. **Modelagem do banco relacional e dimensional**
2.  **Criação da estrutura do banco de dados MySQL (DDL - Data Definition Language)** 
3. **Carga e transformação dos dados (DML + Python)**
4. **Implementação de operações OLAP**
5. **Geração de DataFrames para Streamlit**
6. **Validação e análise dos resultados**

---

# 🛠️ **6. Tecnologias Utilizadas**

| Tecnologia                 | Versão | Finalidade                |
| -------------------------- | ------ | ------------------------- |
| **MySQL**                  | 8.0+   | Armazenamento e consultas |
| **Python**                 | 3.11   | ETL e análises            |
| **Pandas**                 | Latest | Manipulação de dados      |
| **mysql-connector-python** | Latest | Interface Python ⇄ MySQL  |
| **Streamlit**              | Latest | Visualização e dashboard  |

---

# 🏗️ **7.Estrutura do Banco de Dados**

## 7.1 **Modelo Relacional**

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

* `idx_sale_date` - Otimização de consultas temporais
* `idx_dealer_region` - Análises regionais
* `idx_company` - Análises por fabricante
* `idx_model` - Análises por modelo
* `idx_gender` - Análises demográficas
* `idx_price` - Análises financeiras
* `idx_annual_income` - Análises de perfil de cliente

---

## 7.2 **Modelo Dimensional (Star Schema)**

### Dimensões:

* **`dim_time`** - Dimensão temporal
   - `date_key`, `day`, `month`, `quarter`, `year`, `month_name`, `day_name`, `is_weekend`

* **`dim_customer`** - Dimensão cliente
   - `customer_key`, `customer_name`, `gender`, `income_bracket`, `annual_income`, `phone`

* **`dim_dealer`** - Dimensão concessionária
   - `dealer_key`, `dealer_name`, `dealer_no`, `dealer_region`

* **`dim_vehicle`** - Dimensão veículo
   - `vehicle_key`, `company`, `model`, `body_style`, `engine`, `transmission`, `color`

### Tabela Fato:

**`fact_sales`** - Fato de vendas
- `sale_key`, `car_id`, `date_key`, `customer_key`, `dealer_key`, `vehicle_key`, `price`, `annual_income`, `financial_effort_ratio`

---

## 7.3 **Views Analíticas**

Foram criadas 6 views para facilitar as análises OLAP:

1. **`vw_sales_performance`** - Desempenho de vendas por período
2. **`vw_sales_by_model`** - Vendas por modelo e marca
3. **`vw_regional_analysis`** - Análise regional de vendas
4. **`vw_customer_profile`** - Perfil dos clientes
5. **`vw_income_preferences`** - Preferências por faixa de renda
6. **`vw_dealer_ranking`** - Ranking de concessionárias

---

# 📄 **8. Scripts Desenvolvidos**


### 1. `car_sales_ddl.sql`

**Descrição:** Script DDL para criação da estrutura do banco de dados.

**Conteúdo:**
- Criação do banco de dados `car_sales_db`
- Criação da tabela principal `car_sales`
- Criação das tabelas dimensionais (Star Schema)
- Criação das views analíticas
- Definição de índices para otimização

**Como executar:**
```bash
mysql -u root -p < car_sales_ddl.sql
```

### 2. `car_sales_dml.sql`

**Descrição:** Script DML com operações de manipulação e consultas OLAP.

**Conteúdo:**
- Instruções para carga de dados
- População das tabelas dimensionais
- População da tabela fato
- Consultas OLAP completas (Drill-Down, Roll-Up, Slice, Dice, Pivot)
- Validações e verificações de qualidade

**Como executar:**
```bash
mysql -u root -p car_sales_db < car_sales_dml.sql
```

### 3. `load_data.py`

**Descrição:** Script Python para carga automatizada dos dados do CSV para o MySQL.

**Funcionalidades:**
- Conexão com MySQL
- Leitura e transformação do CSV
- Inserção em lotes (batch insert) para performance
- Execução do script DML
- Validação dos dados carregados
- Estatísticas e relatórios

**Como executar:**
```bash
python3 load_data.py
```

**Pré-requisitos:**
```bash
pip3 install pandas mysql-connector-python
```

### 4. `generate_dataframes.py`

**Descrição:** Script Python para gerar DataFrames estruturados para o Streamlit.

**Funcionalidades:**
- Carregamento e transformação dos dados
- Geração de 20 DataFrames específicos para cada análise
- Cálculo de KPIs e métricas
- Exportação em formato pickle e CSV

**Como executar:**
```bash
python3 generate_dataframes.py
```

**Saída:**
- `dataframes.pkl` - Arquivo pickle com todos os DataFrames
- `dataframes_csv/` - Pasta com CSVs individuais

---

# 📊 **9. Operações OLAP Implementadas**

### 1. Vendas e Desempenho Comercial

**Perguntas respondidas:**
- Quais são os modelos e marcas mais vendidos?
- Qual é o ticket médio das vendas?
- Existe sazonalidade nas vendas?

**Operações OLAP:**
- **Roll-Up:** Agregação por ano → trimestre → mês
- **Drill-Down:** Detalhamento por região → concessionária → modelo
- **Slice:** Análise de um período específico
- **Pivot:** Comparação de receita por trimestre

**Consultas principais:**
```sql
-- Volume de vendas por mês
SELECT year_month, total_sales_volume, total_revenue, average_ticket
FROM vw_sales_performance
ORDER BY year_month;

-- Taxa de crescimento mensal
SELECT year_month, total_revenue,
       LAG(total_revenue) OVER (ORDER BY year_month) AS previous_month,
       ROUND(((total_revenue - LAG(total_revenue) OVER (ORDER BY year_month)) / 
              LAG(total_revenue) OVER (ORDER BY year_month)) * 100, 2) AS growth_rate
FROM vw_sales_performance;

-- Top 20 modelos mais vendidos
SELECT company, model, sales_count, total_revenue, average_price
FROM vw_sales_by_model
ORDER BY sales_count DESC
LIMIT 20;
```

### 2. Perfil do Cliente

**Perguntas respondidas:**
- Clientes de maior renda compram quais tipos de veículos?
- Existe diferença de preferência entre homens e mulheres?
- Qual é a faixa de renda predominante?

**Operações OLAP:**
- **Dice:** Análise multidimensional (renda × gênero × modelo)
- **Slice:** Análise por faixa de renda específica
- **Drill-Down:** Detalhamento por renda → gênero → marca → modelo

**Consultas principais:**
```sql
-- Distribuição por faixa de renda
SELECT income_bracket, SUM(customer_count) AS total,
       ROUND(SUM(customer_count) * 100.0 / (SELECT SUM(customer_count) FROM vw_customer_profile), 2) AS percentage
FROM vw_customer_profile
GROUP BY income_bracket;

-- Percentual por gênero
SELECT gender, COUNT(*) AS sales,
       ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM car_sales), 2) AS percentage
FROM car_sales
GROUP BY gender;

-- Índice de esforço financeiro
SELECT income_bracket, gender, AVG(financial_effort_index) AS avg_effort
FROM vw_customer_profile
GROUP BY income_bracket, gender;
```

### 3. Análise Regional

**Perguntas respondidas:**
- Quais regiões apresentam maior volume de vendas?
- Há diferenças no preço médio entre regiões?
- Quais concessionárias têm melhor desempenho?

**Operações OLAP:**
- **Roll-Up:** Agregação por concessionária → região
- **Drill-Down:** Detalhamento por região → concessionária → vendedor
- **Ranking:** Ordenação por volume e receita

**Consultas principais:**
```sql
-- Receita por região
SELECT dealer_region, SUM(sales_volume) AS total_sales,
       SUM(total_revenue) AS revenue,
       ROUND(SUM(total_revenue) * 100.0 / (SELECT SUM(price) FROM car_sales), 2) AS percentage
FROM vw_regional_analysis
GROUP BY dealer_region
ORDER BY revenue DESC;

-- Ranking de concessionárias
SELECT ranking_volume, dealer_name, dealer_region,
       sales_volume, total_revenue, average_ticket
FROM vw_dealer_ranking
ORDER BY ranking_volume
LIMIT 20;
```

### 4. Análises Avançadas

**Operações implementadas:**

- **Drill-Down completo:** Região → Concessionária → Mês
- **Roll-Up com ROLLUP:** Agregações hierárquicas automáticas
- **Slice:** Filtro por região específica
- **Dice:** Cubo multidimensional (Região × Gênero × Renda)
- **Pivot:** Matriz de receita por região e trimestre

**Exemplo de Drill-Down:**
```sql
SELECT dealer_region, dealer_name, DATE_FORMAT(sale_date, '%Y-%m') AS month,
       COUNT(car_id) AS sales, SUM(price) AS revenue
FROM car_sales
GROUP BY dealer_region, dealer_name, month WITH ROLLUP;
```

**Exemplo de Dice:**
```sql
SELECT dealer_region, gender,
       CASE WHEN annual_income < 50000 THEN 'Baixa'
            WHEN annual_income < 500000 THEN 'Média'
            ELSE 'Alta' END AS income_level,
       COUNT(car_id) AS sales, SUM(price) AS revenue
FROM car_sales
WHERE dealer_region IN ('Austin', 'Pasco', 'Aurora')
GROUP BY dealer_region, gender, income_level;
```

---

# 📦 **10. DataFrames para Streamlit**

Foram gerados **20 DataFrames**, organizados em:

### Vendas e Desempenho (5 DataFrames)

1. **`df_total`** - Volume total de vendas
2. **`df_receita_total`** - Receita total e ticket médio
3. **`df_vendas_mes`** - Vendas mensais com taxa de crescimento
4. **`df_modelos_vendidos`** - Modelos e marcas mais vendidos
5. **`df_sazonalidade`** - Vendas por trimestre

### Perfil do Cliente (5 DataFrames)

6. **`df_agrupar_faixa_renda`** - Distribuição por faixa de renda
7. **`df_genero`** - Distribuição por gênero
8. **`df_renda_x_modelo`** - Relação renda × modelo
9. **`df_preferencias`** - Preferências por renda e gênero
10. **`df_esforco_financeiro`** - Índice de esforço financeiro

### Análise Regional (4 DataFrames)

11. **`df_receita_regiao`** - Receita por região
12. **`df_ticket_medio_concessionaria`** - Ticket médio por concessionária
13. **`df_ranking`** - Ranking de concessionárias
14. **`df_comparacao_regioes`** - Comparação entre regiões

### DataFrames Adicionais (6 DataFrames)

15. **`df_body_style`** - Vendas por tipo de carroceria
16. **`df_transmission`** - Vendas por transmissão
17. **`df_color`** - Vendas por cor
18. **`df_top_marcas`** - Top 10 marcas
19. **`df_evolucao`** - Evolução temporal das vendas
20. **`df_correlacao`** - Matriz de correlação

### Como usar no Streamlit

```python
import pickle
import streamlit as st

# Carregar os DataFrames
with open('dataframes.pkl', 'rb') as f:
    dfs = pickle.load(f)

# Usar os DataFrames
st.metric("Total de Vendas", dfs['df_total']['Valor'][0])
st.dataframe(dfs['df_modelos_vendidos'].head(10))
st.line_chart(dfs['df_vendas_mes'].set_index('Mês')['Receita'])
```

---

# ▶️ **11. Como Executar**

1. Criar banco
2. Executar DDL
3. Executar DML
4. Rodar `load_data.py`
5. Rodar `generate_dataframes.py`
6. Usar arquivos no Streamlit

---

# ✔️ **12. Validação dos Dados**

### Estatísticas do Dataset

| Métrica | Valor |
|---------|-------|
| **Total de registros** | 23.906 |
| **Clientes únicos** | 3.021 |
| **Concessionárias** | 28 |
| **Marcas** | 30 |
| **Modelos** | 154 |
| **Período** | 01/01/2022 a 31/12/2023 |
| **Receita total** | $671.472.000,00 |
| **Preço médio** | $28.090,25 |

### Consultas de Validação

```sql
-- Verificar integridade
SELECT 
    'Total de registros' AS metric, COUNT(*) AS value FROM car_sales
UNION ALL
SELECT 'Registros com preço nulo', COUNT(*) FROM car_sales WHERE price IS NULL
UNION ALL
SELECT 'Registros duplicados', COUNT(*) - COUNT(DISTINCT car_id) FROM car_sales;

-- Top 5 modelos mais vendidos
SELECT company, model, COUNT(*) as sales
FROM car_sales
GROUP BY company, model
ORDER BY sales DESC
LIMIT 5;
```
---

# ✔️ **13. Qualidade dos Dados**

- ✅ Sem valores nulos em campos obrigatórios
- ✅ Sem registros duplicados (car_id é único)
- ✅ Datas válidas no período esperado
- ✅ Preços e rendas com valores positivos
- ✅ Integridade referencial mantida no Star Schema

---

# 📝 **14. Notas Técnicas**

### Decisões de Modelagem

1. **Escolha do MySQL:** Optou-se por manter o MySQL conforme discussão da equipe, garantindo que todos possam executar localmente.

2. **Star Schema:** Implementado para otimizar consultas OLAP, separando dimensões e fatos.

3. **Views Materializadas:** Não foram usadas devido à limitação do MySQL, mas as views criadas são eficientes com os índices.

4. **Índices:** Criados estrategicamente nas colunas mais consultadas para otimizar performance.

5. **Tipos de Dados:** Utilizados tipos apropriados (DECIMAL para valores monetários, ENUM para campos categóricos).

### Performance

- **Inserção em lotes:** 1.000 registros por vez para otimizar a carga
- **Índices:** Reduzem tempo de consulta em até 90%
- **Views:** Simplificam consultas complexas sem perda de performance

### Extensibilidade

O modelo foi projetado para ser facilmente extensível:

- Novas dimensões podem ser adicionadas ao Star Schema
- Views adicionais podem ser criadas conforme necessidade
- DataFrames podem ser regenerados com novos KPIs

---

# 📚 **15. Referências**

- [MySQL Documentation](https://dev.mysql.com/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [OLAP Operations](https://en.wikipedia.org/wiki/OLAP_cube)
- [Star Schema Design](https://en.wikipedia.org/wiki/Star_schema)

---

---

**Última atualização: 17/11/2025**
