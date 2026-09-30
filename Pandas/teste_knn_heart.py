# kNN com e sem normalizacao/padronizacao no dataset heart.csv
# O kNN usa distancia euclidiana, entao colunas com escalas grandes (chol, trestbps)
# dominam colunas com escalas pequenas (oldpeak, age) quando nao ha escalonamento.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.read_csv('Pandas/datasets/heart.csv')

print(f"Formato: {df.shape}")
print(f"Linhas duplicadas: {df.duplicated().sum()}")
print("\nAmplitude (max - min) de algumas colunas:")
print((df[['age', 'trestbps', 'chol', 'thalach', 'oldpeak']].max() - df[['age', 'trestbps', 'chol', 'thalach', 'oldpeak']].min()))

X = df.drop(columns='target')
y = df['target']

# stratify=y mantem a proporcao das classes no treino e no teste
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Cenario A: sem escala
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_treino, y_treino)
acc_sem = knn.score(X_teste, y_teste)

# Cenario B: normalizacao (MinMaxScaler) -> valores entre 0 e 1
# O scaler e ajustado (fit) APENAS no treino, para nao vazar informacao do teste
minmax = MinMaxScaler()
X_treino_mm = minmax.fit_transform(X_treino)
X_teste_mm = minmax.transform(X_teste)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_treino_mm, y_treino)
acc_mm = knn.score(X_teste_mm, y_teste)

# Cenario C: padronizacao (StandardScaler) -> media 0 e desvio padrao 1
padrao = StandardScaler()
X_treino_ss = padrao.fit_transform(X_treino)
X_teste_ss = padrao.transform(X_teste)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_treino_ss, y_treino)
acc_ss = knn.score(X_teste_ss, y_teste)

print("\nAcuracia do kNN (k=5) no conjunto de teste:")
print(f"  Sem escala:     {acc_sem * 100:.2f}%")
print(f"  MinMaxScaler:   {acc_mm * 100:.2f}%")
print(f"  StandardScaler: {acc_ss * 100:.2f}%")

# Bonus: testando varios valores de k com os dados padronizados
print("\nAcuracia por valor de k (StandardScaler):")
for k in [1, 3, 5, 7, 9, 11, 15, 21]:
    modelo = KNeighborsClassifier(n_neighbors=k).fit(X_treino_ss, y_treino)
    print(f"  k={k:>2}: {modelo.score(X_teste_ss, y_teste) * 100:.2f}%")
