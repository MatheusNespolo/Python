# Exemplo: Usando diabetes_prediction_dataset.csv com PreProcessamento.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split

# ============================================================================
# 1. CARREGANDO E EXPLORANDO O DATASET
# ============================================================================

df = pd.read_csv('Pandas/datasets/diabetes_prediction_dataset.csv')

print("=" * 70)
print("EXPLORANDO O DATASET: diabetes_prediction_dataset.csv")
print("=" * 70)
print(f"\nForma: {df.shape[0]} linhas, {df.shape[1]} colunas\n")

# Primeiras 5 linhas
print("Primeiras 5 linhas:")
print(df.head())

# Info geral
print("\n" + "=" * 70)
print("INFORMAÇÕES DO DATASET")
print("=" * 70)
print(df.info())

# Estatísticas descritivas
print("\n" + "=" * 70)
print("ESTATÍSTICAS NUMÉRICAS")
print("=" * 70)
print(df.describe())

# Dados faltantes
print("\n" + "=" * 70)
print("VALORES AUSENTES (NaN)")
print("=" * 70)
print(df.isnull().sum())

# ============================================================================
# 2. TRATAMENTO DE DADOS CATEGÓRICOS
# ============================================================================

print("\n" + "=" * 70)
print("PRÉ-PROCESSAMENTO 1: CODIFICAÇÃO DE VARIÁVEIS CATEGÓRICAS")
print("=" * 70)

# Label Encoding: smoking_history (ordinal não-aparente)
print("\nColunas categóricas encontradas:")
print(df.select_dtypes(include='object').columns.tolist())

encoder = LabelEncoder()
df['smoking_history_encoded'] = encoder.fit_transform(df['smoking_history'])

print("\nLabel Encoding (smoking_history):")
print(f"  Mapeamento: {dict(zip(encoder.classes_, encoder.transform(encoder.classes_)))}")
print(f"  Antes: {df['smoking_history'].unique()[:5]}")
print(f"  Depois: {df['smoking_history_encoded'].unique()[:5]}")

# One-Hot Encoding: gender (melhor prática para variáveis sem ordem)
print("\nOne-Hot Encoding (gender):")
print(f"  Categorias: {df['gender'].unique()}")
df_codificado = pd.get_dummies(df, columns=['gender'], drop_first=False)
print(f"  Novas colunas: {[col for col in df_codificado.columns if 'gender' in col]}")
print(f"  Forma após one-hot: {df_codificado.shape}")

# ============================================================================
# 3. PREPARAÇÃO PARA MODELO (TRAIN/TEST SPLIT)
# ============================================================================

print("\n" + "=" * 70)
print("PRÉ-PROCESSAMENTO 2: DIVISÃO TREINO/TESTE")
print("=" * 70)

# Remover colunas não usadas (original + encoded)
X = df_codificado.drop(columns=['diabetes', 'smoking_history', 'gender_Female', 'gender_Male'])
y = df_codificado['diabetes']

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nDivisão 80/20:")
print(f"  X_treino: {X_treino.shape}")
print(f"  X_teste:  {X_teste.shape}")
print(f"  y_treino: {y_treino.shape}")
print(f"  y_teste:  {y_teste.shape}")

print(f"\nDistribuição do alvo (diabetes):")
print(f"  Treino: {y_treino.value_counts().to_dict()}")
print(f"  Teste:  {y_teste.value_counts().to_dict()}")

# ============================================================================
# 4. NORMALIZAÇÃO/PADRONIZAÇÃO (MinMaxScaler)
# ============================================================================

print("\n" + "=" * 70)
print("PRÉ-PROCESSAMENTO 3: NORMALIZAÇÃO (MinMaxScaler)")
print("=" * 70)

scaler = MinMaxScaler()

# FIT apenas com treino (evitar data leakage)
X_treino_normalizado = scaler.fit_transform(X_treino)
X_teste_normalizado = scaler.transform(X_teste)

print(f"\nAntes (amostras dos valores de treino):")
print(X_treino.iloc[:3, :5])

print(f"\nDepois (normalizado entre 0 e 1):")
print(pd.DataFrame(X_treino_normalizado, columns=X_treino.columns).iloc[:3, :5])

print(f"\nIntervalo min/max após normalização:")
for i, col in enumerate(X_treino.columns[:5]):
    print(f"  {col}: [{X_treino_normalizado[:, i].min():.4f}, {X_treino_normalizado[:, i].max():.4f}]")

# ============================================================================
# 5. RESULTADO FINAL
# ============================================================================

print("\n" + "=" * 70)
print("RESULTADO FINAL - PRONTO PARA MODELO ML")
print("=" * 70)

print(f"\nFeatures (X_treino normalizado): {X_treino_normalizado.shape}")
print(f"Target (y_treino): {y_treino.shape}")
print(f"\nNomes das features:")
print(f"  {list(X_treino.columns)}")

print("\n✅ Dados pré-processados e prontos para treinar um classificador!")
print("   Ex: LogisticRegression, RandomForest, SVM, etc.")
