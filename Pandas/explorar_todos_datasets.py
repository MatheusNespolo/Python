# Script para Explorar TODOS os 6 Datasets do Kaggle

import pandas as pd
import os

# Lista dos datasets baixados
datasets = {
    '1. Diabetes Prediction': 'Pandas/datasets/diabetes_prediction_dataset.csv',
    '2. Titanic Survival': 'Pandas/datasets/Titanic-Dataset.csv',
    '3. Adult Census Income': 'Pandas/datasets/adult.csv',
    '4. Stroke Prediction': 'Pandas/datasets/healthcare-dataset-stroke-data.csv',
    '5. Heart Disease': 'Pandas/datasets/heart.csv',
    '6. Loan Approval': 'Pandas/datasets/loan_approval_dataset.csv'
}

print("=" * 100)
print("EXPLORAÇÃO RÁPIDA DE TODOS OS DATASETS")
print("=" * 100)

for nome, caminho in datasets.items():
    print(f"\n{'=' * 100}")
    print(f"{nome}")
    print("=" * 100)
    
    try:
        # Carregar dataset
        df = pd.read_csv(caminho)
        
        # Informações básicas
        print(f"\n[FORMA] {df.shape[0]:,} linhas x {df.shape[1]} colunas")
        
        # Tipos de colunas
        print(f"\n[TIPOS DE DADOS]")
        tipos = df.dtypes.value_counts()
        for tipo, count in tipos.items():
            print(f"   - {tipo}: {count} colunas")
        
        # Colunas categóricas vs numéricas
        cat_cols = df.select_dtypes(include=['object', 'str']).columns.tolist()
        num_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        
        print(f"\n[CATEGORICAS] ({len(cat_cols)}): {cat_cols[:5]}" + (" ..." if len(cat_cols) > 5 else ""))
        print(f"[NUMERICAS] ({len(num_cols)}): {num_cols[:5]}" + (" ..." if len(num_cols) > 5 else ""))
        
        # Valores nulos
        nulos = df.isnull().sum()
        total_nulos = nulos.sum()
        if total_nulos > 0:
            print(f"\n[ALERTA] Valores ausentes: {total_nulos:,} ({total_nulos/df.size*100:.2f}% do total)")
            print(f"   Colunas com NaN: {nulos[nulos > 0].to_dict()}")
        else:
            print(f"\n[OK] Sem valores ausentes (dataset completo)")
        
        # Amostra dos dados
        print(f"\n[AMOSTRA] Primeiras 3 linhas:")
        print(df.head(3).to_string(max_cols=8, show_dimensions=False))
        
        # Detectar possível coluna target
        possivel_target = None
        for col in df.columns:
            if any(keyword in col.lower() for keyword in ['target', 'survived', 'diabetes', 'stroke', 'income', 'status', 'label', 'class']):
                possivel_target = col
                break
        
        if possivel_target:
            print(f"\n[TARGET] Possivel coluna alvo: '{possivel_target}'")
            if possivel_target in df.columns:
                valores = df[possivel_target].value_counts()
                print(f"   Distribuicao:")
                for val, count in valores.head(5).items():
                    print(f"      {val}: {count:,} ({count/len(df)*100:.1f}%)")
        
        # Tamanho em disco
        file_size = os.path.getsize(caminho) / 1024  # KB
        print(f"\n[DISCO] Tamanho: {file_size:,.1f} KB")
        
        # Recomendação de uso
        print(f"\n[RECOMENDACAO] Use este dataset para:")
        if len(cat_cols) > 3:
            print("   - Praticar LabelEncoder e get_dummies (muitas categoricas)")
        if total_nulos > 0:
            print("   - Tratar valores ausentes (dropna/fillna)")
        if len(num_cols) > 5:
            print("   - Normalizacao com MinMaxScaler/StandardScaler")
        if possivel_target and df[possivel_target].nunique() == 2:
            print("   - Classificacao binaria (LogisticRegression, RandomForest)")
        
    except Exception as e:
        print(f"\n[ERRO] Falha ao carregar: {e}")

print("\n" + "=" * 100)
print("RESUMO FINAL")
print("=" * 100)
print(f"\n[OK] Total de datasets: {len(datasets)}")
print(f"[PASTA] Localizacao: C:\\Users\\matheusn\\Documents\\GitHub\\Python\\Pandas\\datasets\\")
print(f"\n[PROXIMOS PASSOS]")
print("   1. Escolha um dataset (recomendo 'Diabetes Prediction' para comecar)")
print("   2. Execute: python Pandas/exemplo_diabetes_dataset.py")
print("   3. Adapte PreProcessamento.py para os outros datasets")
print("   4. Treine seu primeiro modelo ML!")
print("\n[FIM] Bons estudos!")
