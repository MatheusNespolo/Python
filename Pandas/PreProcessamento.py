# Label encoding
# Atribui um número inteiro para cada categoria. É simples, mas cria uma ordem artificial entre as categorias, o que pode confundir angulns algoritmos (ex.: "vermelho"=0, "azul"=1, "verde"=2 sugere uma escala que não existe de verdade).

import pandas as pd
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

df = pd.read_csv('Pandas/dataset.csv')

df['blood_pressure_systolic_encoded'] = encoder.fit_transform(df['blood_pressure_systolic'])

print(df['blood_pressure_systolic_encoded'])

# One-Hot Encoding
# Cria uma coluna binária (0 ou 1) para cada categoria possível, evitando a ordem artificial do Label Encoding. É o mais indicado quando as categorias não têm uma ordem natural entre si.

df_codificado = pd.get_dummies(df, columns=['gender'])

print(df_codificado)

# Divisão do conjunto de dados (Treino e Teste)
# Para avaliar um modelo de forma justa, ele não pode ser testado com os mesmos dados usados no treino - senão estaríamos medindo memorização, não aprendizado. Por isso, o dataset é dividido:

from sklearn.model_selection import train_test_split

X = df.drop(columns='diabetes_risk') # features
y = df['diabetes_risk']

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)
# test_size=0.2 reserva de 20% dos dados para teste (uma proporção comum é 70/30 ou 80/20);
# random_state fixa a "aleatoriedade" da divisão, garantindo que o experimento seja reproduzível

# Normalização e Padronização
# Algoritmos baseados em distância (como kNN) ou em otimização por gradiente são sensíveis à escala das variáveis - uma coluna "salário" (na casa dos milhares) pontuaria mais do que uma coluna "idade" (na casa das dezenas) se não forem colocadas na mesma escala.

# Normalização e Padronização
# Reescala os valores para o intervalo 0, 1:

from sklearn.preprocessing import MinMaxScaler

