# Regressao Logistica no dataset heart.csv
# Alvo binario: target (1 = doenca cardiaca, 0 = sem doenca)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv('Pandas/datasets/heart.csv')

print(f"Formato: {df.shape}")
print(f"Valores nulos: {df.isna().sum().sum()}")
print(f"Linhas duplicadas: {df.duplicated().sum()}")
print("\nDistribuicao do alvo:")
print(df['target'].value_counts())

X = df.drop(columns='target')
y = df['target']

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Padronizacao: a regressao logistica usa otimizacao por gradiente e regularizacao,
# entao tambem se beneficia de features na mesma escala
scaler = StandardScaler()
X_treino_esc = scaler.fit_transform(X_treino)
X_teste_esc = scaler.transform(X_teste)

modelo = LogisticRegression(max_iter=1000, random_state=42)
modelo.fit(X_treino_esc, y_treino)

y_pred = modelo.predict(X_teste_esc)

print(f"\nAcuracia: {accuracy_score(y_teste, y_pred) * 100:.2f}%")

print("\nMatriz de confusao (linhas = real, colunas = previsto):")
print(confusion_matrix(y_teste, y_pred))

print("\nRelatorio de classificacao:")
print(classification_report(y_teste, y_pred, target_names=['Sem doenca', 'Com doenca']))

# Interpretacao: coeficientes positivos aumentam a chance de doenca,
# negativos diminuem. Como os dados foram padronizados, os coeficientes
# sao comparaveis entre si (quanto maior o valor absoluto, maior a influencia).
coeficientes = pd.Series(modelo.coef_[0], index=X.columns).sort_values(key=abs, ascending=False)
print("\nCoeficientes (ordenados por influencia):")
print(coeficientes.round(3))

# Odds ratio: quanto a chance (odds) de doenca muda a cada +1 desvio padrao na variavel
print("\nOdds ratio por +1 desvio padrao:")
print(coeficientes.apply(lambda c: 2.718281828 ** c).round(3))

# Probabilidades previstas para as 5 primeiras amostras de teste
probs = modelo.predict_proba(X_teste_esc)[:5, 1]
print("\nProbabilidade prevista de doenca (5 primeiras amostras de teste):")
print(pd.DataFrame({'prob_doenca': probs.round(3), 'real': y_teste.iloc[:5].values}))
