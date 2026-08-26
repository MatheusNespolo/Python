# Pandas para Ciência de Dados

import pandas as pd

# Lendo um arquivo CSV (Como o "Vinho.csv" u "healthcare-dataset" da Aula 2)
df = pd.read_csv('Pandas/dataset.csv')

# Mostra as primeiras 5 linhas
print(df.head())

# Tipos de dados de cada coluna e contagem de valores não-nulos
print(df.info())

# Estatísticas descritivas das colunas numéricas
print(df.describe())

# Selecionando dados
#Selecionar uma coluna (retorna uma Series)
idade = df["age"]

# Selecionar por posição (linha, coluna) - iloc
primeira_linha = df.iloc[0]

# Selecionar por rótulo (nome do índice/colune) - loc
linha_especifica = df.loc[0, "age"]

# Filtrar linhas com uma condição (máscara booleana)
maiores_de_idade = df[df["age"] >= 18]

# Agrupando e agregando dados
# Equivalente a um "GROUP BY" do SQL
media_por_categoria = df.groupby('income_bracket')['age'].mean()

# Contar valores únicos de uma coluna
print(df["income_bracket"].value_counts())

# Tratando dados ausentes
# Verificar quantos valores nulos existem por coluna
print(df.isna().sum())

# Remoover linhas com qualquer valor nulo
df_limpo = df.dropna()

# Ou preencher os nulos com um valor (ex: a média da coluna)
df['age'] = df['age'].fillna(df['age'].mean())
