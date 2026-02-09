import pandas as pd

df = pd.read_csv('clientes.csv')

#verificar primeiros registros
print (df.head().to_string())

# Verifica os últimos registros
print (df.tail().to_string())

# Verificar qtd de linhas e colunas
print ('Qtd: ', df.shape)

# Verifica tipos de dados
print ('Tipagem:\n', df.dtypes)

# Checar valores nulos
print ('Valores nulos:\n', df.isnull().sum())
