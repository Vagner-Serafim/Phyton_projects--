import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)

df= pd.read_csv('clientes-v2.csv')

print(df.head())

#Codificacão one-hot para 'estado_civil'
df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1)

print("\nDataframe após codificação ordinal para 'nivel_educacao:\n", df.head())

#Codificação ordinal para 'nivel_educacao'
educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Médio': 2, 'Ensino_supeior': 3, 'Pós-graduação': 4}
df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)

print("\nDataFrame após codificação ordinal para 'nivel_educacao:\n", df.head())

#Transforma 'area_atuacao' em em categorias codificadas usando o metodo .cat.codes
df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes

print("\nDataFrame após transformar 'area_atuacao' em códigos numéricos:\n", df.head())

#Label encoder para 'estado'
#LabelEncoder converte cada valor único em números de 0 a n_classes-1
label_encoder = LabelEncoder()
df['estrado_cod'] = label_encoder.fit_transform(df['estado'])

print("\nDataFrame após aplicar LabelEncoder em 'estado':\n", df.head())