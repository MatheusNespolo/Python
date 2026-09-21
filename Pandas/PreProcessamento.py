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
