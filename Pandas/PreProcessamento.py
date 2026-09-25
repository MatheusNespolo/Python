# Label encoding
# Atribui um número inteiro para cada categoria. É simples, mas cria uma ordem artificial entre as categorias, o que pode confundir angulns algoritmos (ex.: "vermelho"=0, "azul"=1, "verde"=2 sugere uma escala que não existe de verdade).

import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('Pandas/datasets/diabetes_prediction_dataset.csv')

# Carregando e explorando o dataset
print("Explorando o dataset: diabetes_prediction_dataset.csv")

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

# Dados nulos
print('Valores ausentes (NaN)')
print(df.isnull().sum())

# Tratamento de dados categóricos
print('Pré-processamento 1: codificação de variáveis categóricas')

# Label Encoding: smoking_history (ordinal não aparente)
print('\nColunas categóricas encontradas:')
print(df.select_dtypes(include='object').columns.tolist())

encoder = LabelEncoder()

df['smoking_history_encoded'] = encoder.fit_transform(df['smoking_history'])

print('\nLabel Encoding (smoking_history):')
print(f'    Mapeamento: {dict(zip(encoder.classes_, encoder.transform(encoder.classes_)))}')

print(f'    Antes: {df['smoking_history'].unique()[:5]}')
print(f'    Depois: {df['smoking_history_encoded'].unique()[:5]}')

# One-Hot Encoding
# Cria uma coluna binária (0 ou 1) para cada categoria possível, evitando a ordem artificial do Label Encoding. É o mais indicado quando as categorias não têm uma ordem natural entre si.

print('\nOne-Hot encoding (gender):')
print(f'    Categorias: {df['gender'].unique()}')

df_codificado = pd.get_dummies(df, columns=['gender'], drop_first=False)
print(f'    Novas colunas: {[col for col in df_codificado.columns if 'gender' in col]}')
print(f'    Forma após one-hot: {df_codificado.shape}')

# Divisão do conjunto de dados (Treino e Teste)
# Para avaliar um modelo de forma justa, ele não pode ser testado com os mesmos dados usados no treino - senão estaríamos medindo memorização, não aprendizado. Por isso, o dataset é dividido:

print('Pré-processamento 2: Divisão treino/teste')

from sklearn.model_selection import train_test_split

# Remove as colunas que não estão sendo utilizadas (original + encoder)
X = df_codificado.drop(columns=['diabetes', 'smoking_history', 'gender_Female', 'gender_Male']) # features
y = df_codificado['diabetes']

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42
    )
# test_size=0.2 reserva de 20% dos dados para teste (uma proporção comum é 70/30 ou 80/20);
# random_state fixa a "aleatoriedade" da divisão, garantindo que o experimento seja reproduzível
print('\nDivisão 80/20:')
print(f'    X_treino: {X_treino.shape}')
print(f'    X_teste: {X_teste.shape}')
print(f'    y_treino: {y_treino.shape}')
print(f'    y_teste: {y_teste.shape}')

print('\nDistribuição do alvo (diabetes):')
print(f'    Treino: {y_treino.value_counts().to_dict()}')
print(f'    Teste: {y_teste.value_counts().to_dict()}')

# Normalização e Padronização
# Algoritmos baseados em distância (como kNN) ou em otimização por gradiente são sensíveis à escala das variáveis - uma coluna "salário" (na casa dos milhares) pontuaria mais do que uma coluna "idade" (na casa das dezenas) se não forem colocadas na mesma escala.

print('Pré-processamento 3: Normalização e Padronização')

# Normalização e Padronização
# Reescala os valores para o intervalo 0, 1:

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

# FIT apenas com o treino (evitando data leakage)
X_treino_normalizado = scaler.fit_transform(X_treino)
X_teste_normalizado = scaler.transform(X_teste)

print('\nAntes (amostras dos valores de treino):')
print(X_treino.iloc[:3, :5])

print('\nDepois (normalizado entre 0 e 1):')
print(pd.DataFrame(X_treino_normalizado, columns=X_treino.columns).iloc[:3, :5])

print('\nIntervalo min/máx após normalização:')
for i, col in enumerate(X_treino.columns[:5]):
    print(f'    {col}: [{X_treino_normalizado[:, i].min():.4f}, {X_treino_normalizado[:, i].max():.4f}]')

# Resultado Final
print('Resultado Final')

print(f'\nFeatures (X_treino normalizado): {X_treino_normalizado.shape}')
print(f'Target (y_treino): {y_treino.shape}')
print('\nNomes das features')
print(f'    {list(X_treino.columns)}')

print('Dados prontos e pré-processados para treinar um classificador')
