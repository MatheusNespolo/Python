# 📚 Índice de Datasets para Prática de Machine Learning

## 🎯 Recomendação Principal

### ✅ **Melhor Match com seu código:** `diabetes_prediction_dataset.csv`

```python
# Use diretamente com PreProcessamento.py substituindo:
df = pd.read_csv('Pandas/datasets/diabetes_prediction_dataset.csv')
```

**Por quê?**
- ✅ Tem colunas categóricas: `gender`, `smoking_history`
- ✅ Tem colunas numéricas: `age`, `bmi`, `blood_glucose_level`, `HbA1c_level`
- ✅ Alvo binário: `diabetes` (0/1)
- ✅ ~100k linhas, sem valores ausentes
- ✅ Script de exemplo pronto: `exemplo_diabetes_dataset.py`

---

## 📊 Catálogo Completo

| Dataset | Domínio | Alvo | Colunas Cat. | Colunas Num. | Linhas | Indicado para |
|---------|---------|------|--------------|--------------|--------|---------------|
| **diabetes_prediction_dataset.csv** | Saúde | `diabetes` (0/1) | gender, smoking_history | age, bmi, glucose, etc. | ~100k | ⭐ Label/OneHot + normalização |
| **Titanic-Dataset.csv** | Transporte | `Survived` (0/1) | Sex, Embarked, Pclass | Age, Fare | ~891 | Tratamento de NaN + encoding |
| **adult.csv** | Censo | `income` (<=50K/>50K) | workclass, education, occupation, etc. | age, fnlwgt, hours.per.week | ~32k | Muitas categóricas |
| **healthcare-dataset-stroke-data.csv** | Saúde | `stroke` (0/1) | gender, work_type, smoking_status | age, avg_glucose_level, bmi | ~5.1k | Similar ao original |
| **heart.csv** | Saúde | `target` (0/1) | Nenhuma (todas numéricas) | age, trestbps, chol, etc. | ~303 | Focar em MinMaxScaler |
| **loan_approval_dataset.csv** | Finanças | `loan_status` (Approved/Rejected) | education, self_employed | income_annum, loan_amount, cibil_score | ~4.3k | Domínio diferente |

---

## 🚀 Como Começar

### Opção 1: Usar o exemplo pronto
```bash
python Pandas/exemplo_diabetes_dataset.py
```

### Opção 2: Adaptar seu PreProcessamento.py

```python
# Em PreProcessamento.py, linha 9:
# ANTES:
df = pd.read_csv('Pandas/dataset.csv')

# DEPOIS:
df = pd.read_csv('Pandas/datasets/diabetes_prediction_dataset.csv')

# Linha 11-12 (corrigir Label Encoding):
# ANTES:
df['blood_pressure_systolic_encoded'] = encoder.fit_transform(df['blood_pressure_systolic'])

# DEPOIS:
df['smoking_history_encoded'] = encoder.fit_transform(df['smoking_history'])

# Linha 27-28 (corrigir target):
# ANTES:
X = df.drop(columns='diabetes_risk')
y = df['diabetes_risk']

# DEPOIS:
X = df.drop(columns='diabetes')
y = df['diabetes']
```

### Opção 3: Explorar com CienciaDeDados.py

```python
# Substitua o dataset.csv em CienciaDeDados.py (linha 6):
df = pd.read_csv('Pandas/datasets/Titanic-Dataset.csv')  # ou qualquer outro

print(df.head())
print(df.info())
print(df.isnull().sum())  # Verificar NaN
```

---

## 📋 Estrutura de Arquivos

```
C:\Users\matheusn\Documents\GitHub\Python\Pandas\
│
├── CienciaDeDados.py            ← Exploração básica de dados
├── PreProcessamento.py          ← Label/OneHot encoding + train/test
├── exemplo_diabetes_dataset.py  ← Script completo com diabetes dataset ⭐
├── dataset.csv                  ← Dataset original (healthcare India)
│
└── datasets/                    ← 6 datasets do Kaggle (ignorados no git)
    ├── README.md                ← Guia detalhado de cada dataset
    ├── diabetes_prediction_dataset.csv   ⭐ Principal
    ├── Titanic-Dataset.csv
    ├── adult.csv
    ├── healthcare-dataset-stroke-data.csv
    ├── heart.csv
    └── loan_approval_dataset.csv
```

---

## 💡 Desafios Progressivos

### Nível 1: Básico
1. Carregue `diabetes_prediction_dataset.csv`
2. Use `df.head()`, `df.info()`, `df.describe()`
3. Verifique se há valores nulos: `df.isnull().sum()`

### Nível 2: Pré-processamento
1. Aplique `LabelEncoder` em `smoking_history`
2. Aplique `get_dummies` em `gender`
3. Divida em treino/teste (80/20)

### Nível 3: Normalização
1. Complete o `MinMaxScaler` no PreProcessamento.py
2. Normalize as colunas numéricas (`age`, `bmi`, etc.)
3. Verifique se os valores ficaram entre 0 e 1

### Nível 4: Modelo ML
1. Treine um `LogisticRegression` ou `RandomForestClassifier`
2. Avalie com `accuracy_score` no conjunto de teste
3. Plote a matriz de confusão (instale `matplotlib`/`seaborn` se necessário)

### Nível 5: Experimentos
1. Teste todos os 6 datasets
2. Compare a acurácia entre eles
3. Documente qual pré-processamento funcionou melhor para cada um

---

## 📦 Dependências Necessárias

```bash
pip install pandas scikit-learn

# Opcional (para visualizações):
pip install matplotlib seaborn
```

**Status atual:**
- ✅ pandas 3.0.6
- ✅ scikit-learn 1.9.1
- ⏳ matplotlib/seaborn (não instalados)

---

## ⚙️ Configuração Kaggle CLI

Caso precise baixar mais datasets no futuro:

```bash
pip install kaggle

# 1. Gere o token em: https://www.kaggle.com/settings → "Create New API Token"
# 2. Coloque kaggle.json em: C:\Users\matheusn\.kaggle\kaggle.json
# 3. Baixe com:
kaggle datasets download -d <dataset-slug> -p Pandas/datasets --unzip
```

---

## 🔗 Links dos Datasets no Kaggle

- [diabetes-prediction-dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset) ⭐
- [titanic-dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)
- [adult-census-income](https://www.kaggle.com/datasets/uciml/adult-census-income)
- [stroke-prediction-dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
- [heart-disease-dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)
- [loan-approval-prediction](https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset)

---

**Pronto para começar! 🚀**
