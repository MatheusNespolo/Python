# O kNN é o classificador mais intuitivo para começar: para prever a classe de uma nvoa amostra, ele mede a distância dela até todas as amostras conhecidas. É um algoritmo preguiçoso em que o dataset inteiro é a própria memória do modelo.

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('Pandas/datasets/heart.csv')

# Carregando e explorando o dataset
print('Explorando o datset: heart.csv')

# .shape retorna uma tupla representando as dimensões do DataFrame (linhas e colunas)
print(f'\nForma: {df.shape[0]} linhas, {df.shape[1]} colunas\n')

# Linhas iniciais
print('Primeiras 5 linhas:')
print(df.head())

# Info geral
print('Informações do dataset')
print(df.info())

# Estatísticas descritivas
print('Estatísticas numéricas')
print(df.describe())

# Separação dos dados de entrada e saída
X = df.drop(columns='target')
y = df['target']

# Divisão entre treino e teste (70/30)
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.3, random_state=42
)
# test_size=0.2 reserva de 20% dos dados para teste (uma proporção comum é 70/30 ou 80/20)
# random_state fixa a "aleatoriedade" da divisão, garantindo que o experimento seja reproduzível

# Cenário 1: Sem normalização / Padronização
modelo_knn = KNeighborsClassifier(n_neighbors=5)
modelo_knn.fit(X_treino, y_treino)

previsoes = modelo_knn.predict(X_teste)
print(f'\nPrevisões do modelo:{previsoes}')

acuracia_sem = modelo_knn.score(X_treino, y_treino)
print(f'\nAcurácia SEM escala: {acuracia_sem * 100:.2f}%')

# Cenário 2: Padronizado
scaler = StandardScaler()
X_treino_pad = scaler.fit_transform(X_treino)
X_teste_pad = scaler.fit_transform(X_teste)

modelo_knn.fit(X_treino_pad, y_treino)
previsoes = modelo_knn.predict(X_teste)
print(f'\nPrevisões do modelo:{previsoes}')

acuracia_com = modelo_knn.score(X_treino_pad, y_treino)
print(f'\nAcurácia COM StandardScaler: {acuracia_com * 100:.2f}%')

# Regressão Logística
# Apesar do nome, é um algoritmo de classificação, não de regressão. APlica uma função sobre uma combinação linear, produzindo sempre algo entre 0 e 1.

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

modelo_logreg = LogisticRegression(max_iter=1000, random_state=42)

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Padronização: a regressão linear usa otimização por gradiente e regularização, então também se beneficia de features na mesma escala
X_treino_pad = scaler.fit_transform(X_treino)
X_teste_pad = scaler.fit_transform(X_teste)

modelo_logreg.fit(X_treino_pad, y_treino)

previsoes = modelo_logreg.predict(X_teste_pad)
print(f'\nAcurácia: {accuracy_score(y_teste, previsoes) * 100:.2f}%')

print('\nMatriz de confusão (linhas = real, colunas = previsão):')
print(confusion_matrix(y_teste, previsoes))

print('\nRelatório de classificação:')
print(classification_report(y_teste, previsoes, target_names=['Sem doença', 'Com doença']))

# Interpretação: coeficientes positivos aumentam a chance de doenças, negativos diminuem. Comos os dados foram padronizados, os coeficientes são comparáveis entre si (quanto maior o valor absoluto, maior a influência)


