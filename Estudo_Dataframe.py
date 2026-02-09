import pandas as pd


#lista: uma coleção de elementos que podem ser de qualquer tipo
lista_nomes =['Ana','Marcos','carlos']
print ('lista_nomes: \n', lista_nomes)
print ('Primeiro elemento da lista: \n', lista_nomes[0])

#Dicionário: Estrutura composta de pares chave_valor
dicionario_pessoa = {
    'nome':'Ana',
    'idade':20,
    "cidade": 'São Paulo'
}
print('dicionario_pessoa: \n', dicionario_pessoa)
print("Atributo do dicionário: \n", dicionario_pessoa.get('nome'))

#Lista de dicionários: Estrutura que combina listas é dicionários
dados = [
    {'nome':'Ana', 'idade':20, 'cidade': 'São paulo'},
    {'nome': 'Marcos', 'idade': 25, 'cidade': 'São josé dos campos'},
    {'nome': 'carlos', 'idade': 35, 'cidade': 'Rio de janeiro'}
]

#Dataframe: Estrutura de dados bidimensional
df= pd.DataFrame(dados)
print('Dataframe; \n', df)

# Selecionar coluna
print(df['nome'])

# Seleciona várias colúnas
print(df[['nome', 'idade']])

# Seleciona linhas pelo índice
print('Primeira linha \n', df.iloc[0])

# Adicionar nova coluna
df['salario'] = [4100, 3600, 5200]

# Adicionar um novo registro
df.loc[len(df)] = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'Taubaté',
    'salario': 4800
}
print('Dataframe Atual \n', df)


# Removendo uma coluna
df.drop('salario', axis=1, inplace=True)

# Filtrando pessoas com mais de 29 anos
filtro_idade = df[df['idade'] >= 30]
print('filtro \n', filtro_idade)

# Salvando dataframe em CSV
df.to_csv('dados.csv', index=False)

# Lendo arquivos CSV em DataFrame
df_lido = pd.read_csv('dados.csv')
print('\n Leitura do CSV \n', df_lido)