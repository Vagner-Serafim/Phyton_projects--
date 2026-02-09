import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler


pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes-v2.csv')

print(df.head())

df = df.drop(['data', 'estado', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao'], axis=1)

#Normalização - MinMaxScaler
scaler = MinMaxScaler()
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(0, 1))
df['idadeMinMaxScaler'] = min_max_scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler'] = min_max_scaler.fit_transform(df[['salario']])

#Padronização - StandardScaler
scaler = StandardScaler()
df['idadeStandardScaler'] = scaler.fit_transform(df[['idade']])
df['SalarioStandardScaler'] = scaler.fit_transform(df[['salario']])

# Padronização - RobustScaler
scaler = RobustScaler()
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])

print(df.head(15))

print('MinMaxScaler(De 0 a 1):')
print("idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4}".format(df['idadeMinMaxScaler'].min(), df['idadeMinMaxScaler'].max(), df['idadeMinMaxScaler'].mean(), df['idadeMinMaxScaler'].std()))
print("salário - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4}".format(df['salarioMinMaxScaler'].min(), df['salarioMinMaxScaler'].max(), df['salarioMinMaxScaler'].mean(), df['salarioMinMaxScaler'].std()))
