# 📊 Projeto Integrador - Apoio Decisório aos Negócios

**Base de dados:** [Car Sales Report - Kaggle](https://www.kaggle.com/datasets/missionjee/car-sales-report)

---

## 🚗5.1. Vendas e Desempenho Comercial

### Perguntas de negócio

* **Quais são os modelos e marcas mais vendidos no período analisado?**
* **Qual é o ticket médio das vendas por região ou concessionária?**
* **Existe sazonalidade nas vendas ao longo do tempo?**

---

### KPIs sugeridos

* **Volume de vendas (número de carros vendidos)**

  ```python
  df_total = contagem dos [Car_id]
  ```

* **Receita total e ticket médio de venda**

  ```python
  df_receita_total = Soma da coluna[Price ($)]
  df_media_receita_ano = Média da coluna[Price ($)]
  ```

* **Taxa de crescimento das vendas por mês/trimestre**
    ```python
    df_tx_crescimento = {[vendas mês atual [Price ($)] - vendas mês anterior [Price ($)]]/vendas mês anterior[Price ($)]}*100
    ```

---

## 👥 5.2. Perfil do Cliente

### Perguntas de negócio

* **Clientes de maior renda compram quais tipos de veículos?**
* **Existe diferença de preferência entre homens e mulheres?**
* **Qual é a faixa de renda predominante dos compradores em cada região?**

---

### KPIs sugeridos

* Distribuição de clientes por faixa de renda

  ```python
  df_agrupar_faixa_renda = Agrupar por [faixa de renda] contagem de linha [Car_id] e fazer a procentagem encima do total
  ```

* Percentual de vendas por gênero

  ```python
  df_genero = Porcentagem que tem de homens e mulheres na coluna genero (Gender / df_total)
  ```

* Índice de esforço financeiro (preço do carro ÷ renda anual)

  ```python
  df_renda_x_modelo = Criar uma nova coluna [faixa de renda] do comprador [Annual Income], agrupar por [Model]
  ```

---

## 🌍 5.3. Análise Regional

### Perguntas de negócio

* Quais regiões apresentam maior volume de vendas?
* Há diferenças significativas no preço médio entre regiões?
* Quais concessionárias têm melhor desempenho de receita?

---

### KPIs sugeridos

* Receita total por região

    ```python
    df_receita_regiao = agrupar por [Dealer_Region] somar [Price ($)]
    ```

* Ticket médio por concessionária

    ```python
    df_ticket_medio_concessionária = agrupar por [Dealer_Name] média [Price ($)]
    ```

* Ranking de concessionárias por volume de vendas

    ```python
    df_ranking = agrupar por [Dealer_Name] contar [Car_id] ordenar do maior para o menos
    ```

---

## 📈 5.4. Suporte a Estratégias de Marketing e Expansão

### Perguntas de negócio

* Em quais regiões vale a pena expandir a rede de concessionárias?
* Quais perfis de cliente devem ser priorizados em campanhas de marketing?
* Existe correlação entre perfil socioeconômico e características do veículo adquirido?

---

### KPIs sugeridos

* Taxa de penetração de mercado (vendas ÷ potencial de clientes)
* Segmentação de clientes por perfil (*clusterização*)
* ROI estimado de campanhas regionais


https://d3js.org/

https://observablehq.com/@d3/gallery?utm_source=d3js-org&utm_medium=hero&utm_campaign=try-observable

https://seaborn.pydata.org/examples/index.html