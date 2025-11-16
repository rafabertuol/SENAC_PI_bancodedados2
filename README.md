# 📊 Projeto Integrador - Apoio Decisório aos Negócios

**Base de dados:** [Car Sales Report - Kaggle](https://www.kaggle.com/datasets/missionjee/car-sales-report)

Projeto acadêmico desenvolvido para a segunda entrega do Projeto Integrador. O objetivo é modelar, implementar e alimentar um banco de dados relacional, demonstrando conceitos de normalização, integridade referencial e consultas avançadas.

## Funcionalidades

- Criação de esquemas de banco de dados (tabelas, chaves primárias e estrangeiras);  
- Scripts de inserção de dados (seeds); 
- Consultas SQL demonstrativas (relatórios, junções, agregações) ; 
- Procedimentos de armazenados.

## Tecnologias

- Banco de dados: MySQL
- Linguagem para scripts: Python
- Ferramentas: MySQL Workbench
- Linguagem backend ou aplicação cliente:

## Diagrama Entidade-Relacionamento (ER)


## Como executar

1. Certifique-se de ter o Python 3.12.1 instalado
2. Instale o Streamlit; `senac_pi_bd2`
3. Execute a aplicação Streamlit usando o comando:
   streamlit run homepage.py
4.  Para configurar o banco de dados:
   psql -U usuario -d senac_pi_bd2 -f scripts/create_tables.sql
   psql -U usuario -d senac_pi_bd2 -f scripts/insert_data.sql
