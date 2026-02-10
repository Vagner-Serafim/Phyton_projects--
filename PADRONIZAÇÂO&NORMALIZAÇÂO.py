import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Exemplo de DataFrame
data = {'idade': [25,45,35,50],
        'salario': [50000, 100000, 75000, 120000]
        }
df = pd.DataFrame(data)

# Padronização
scaler = MinMaxScaler()
df['idade_padronizada'] = scaler.fit_transform(df[['idade']])
df['salario_padronizada'] = scaler.fit_transform(df[['salario']])

# Normalização
min_max_scaler = MinMaxScaler()
df['idade_normalizada'] = min_max_scaler.fit_transform(df[['idade']])
df['salario_normalizada'] = min_max_scaler.fit_transform(df[['salario']])

print(df)