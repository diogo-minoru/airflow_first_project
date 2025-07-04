# Airflow Primeiro Projeto

Projeto com o objetivo de automatizar a execução de tarefas utilizando o airflow como orquestrador.
O projeto consiste em utilizar o airbyte para fazer a injestão dos dados de uma planilha no google sheets em um banco de dados PostgreSQL hospedado no Render.
Após feita a injestão dos dados, é feito o tratamento dos dados utilizando o dbt-cloud, organizando as tabelas em bronze, silver e gold.

![imagem.png](Esquema)