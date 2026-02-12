import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head().to_string())

# Histograma
plt.hist(df['Salário'])
plt.show()

# Histograma - Parâmetros
plt.figure(figsize = (10,6))
plt.hist(df['Salário'], bins = 100, color = 'blue', alpha=0.8)
plt.title('Histograma - Distribuição de Salários')
plt.xlabel('Salário')
plt.xticks(ticks = range(0, int(df['Salário'].max())+2000, 2000))
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

# Múltiplos gráficos
plt.figure(figsize = (10,6))
plt.subplot(2,2,1) # 2 linha, 2 colunas, Gráfico 1
# Gráfico de Dispersão
plt.scatter(df['Salário'], df['Salário'])
plt.title('Dispersão - Salário e Salário')
plt.xlabel('Salário')
plt.ylabel('Salário')

plt.subplot(1,2,2) # linha 1, 2 colunas, gráfico 2
plt.scatter(df['Salário'], df['anos_experiencia'], color='#5883a8', alpha=0.8, s=30) # Cor hexadecimal online
plt.title('Dispersão -Idade e Anos de Experiencia')
plt.xlabel('Salário')
plt.ylabel('Anos de Experiencia')

# Mapa de calor
corr = df[['Salário', 'anos_experiencia']].corr()
plt.subplot(2,2,3) # linha 1, coluna 2, gráfico 1
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title('Correção Salário e Idade')

plt.tight_layout() # Ajustar espaçamentos
plt.show()
