import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

df = pd.read_csv('/data/ecommerce_tratados_ex3.csv')

# Transformação de Qtd_Vendidos usando mapeamento (Ordinal)
mapa_qtd = {
    'Nenhum': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '+5': 5, '+25': 25, '+50': 50, '+100': 100,
    '+1000': 1000, '+10mil': 10000, '+50mil': 50000
}

df['Qtd_Vendidos_Cod'] = df['Qtd_Vendidos'].map(mapa_qtd).astype(float)

#Transformação por frequência do campo Marca
df['Marca_Freq'] = df['Marca'].map(df['Marca'].value_counts(normalize=True))

#Transformação por frequência do Material
contagem_material = df['Material'].value_counts(dropna=True)
total_linhas = len(df) # O denominador fixo inclui as linhas com NaN
frequencia_relativa_total = contagem_material / total_linhas

df['Material_Freq'] = df['Material'].map(frequencia_relativa_total).astype(float)

# Visualização
print(df[['Qtd_Vendidos', 'Qtd_Vendidos_Cod', 'Marca_Freq', 'Material_Freq']].head())
print(df[['Marca_Freq', 'Material_Freq']].dtypes)