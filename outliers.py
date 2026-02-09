import pandas as pd
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes_limpeza.csv')

df_filtro_basico = df[df['idade'] > 100]

print('filtro basico \n', df_filtro_basico[['nome', 'idade']])

#identificar outliers com Z-score
z_scores = stats.zscore(df['idade'].dropna())
outliers_z = df[z_scores >= 3]
print('outliers pelo z \n', outliers_z)

# Filtrar outliers com Z-score
df_zscore = df[(stats.zscore(df['idade']) > 3)]

#Identificar outliers com iQR
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR
limite_auto = Q3 + 1.5 * IQR

print('Limites baixo IQR: ', limite_baixo)
print('Limite auto IQR: ', limite_auto)

outliers_iqr = df[(df['idade'] > limite_baixo) | (df['idade'] > limite_auto)]
print('outliers IQR:\n ', outliers_iqr)

#Filtrar outliers com iqr
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_auto)]

limite_baixo = 1
limite_auto = 100
df = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_auto)]

# Filtrar endereços inválidos
df['endereco'] = df['endereco'].apply(lambda x: 'endereço inválido' if len(x.split('\n')) < 3 else x)

# Tratar campos de texto
df['nome'] = df['nome'].apply(lambda x: 'Nome inválido' if isinstance(x, str) and len(x) > 50 else x)
print('Quantidade de registros com nomes grandes: ', (df['nome'] == 'nome inválido').sum())

print('Dados com outliers tratados: \n', df)

#Salvar dataframe
df.to_csv('clientes_limpeza_outliers.csv', index=True)