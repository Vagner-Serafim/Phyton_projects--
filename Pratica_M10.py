import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ecommerce_preparados.csv')

# Configuração estética
sns.set_theme(style="darkgrid")
plt.rcParams["figure.figsize"] = (12, 8)

# Histograma de distribuição de Preços
plt.figure()
sns.histplot(df["Preço"], bins = 100, kde=False, color="blue")
plt.title("Distribuição de preço dos produtos")
plt.xlabel("Preço R$")
plt.ylabel("Frequência")
plt.show()

# Gráfico de dispersão
plt.figure()
sns.scatterplot(data=df, x="Preço", y="Qtd_Vendidos", hue="Material", alpha=0.7)
plt.title("Relação Preço/Vendas")
plt.xlabel("Preço R$")
plt.ylabel("Vendas")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Relação entre variáveis numéricos
plt.figure()
corr = df.select_dtypes(include=['float64', 'int64']).corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlação entre Variáveis')
plt.show()

# Vendas por categoria
vendas_por_cat = df.groupby('Material')['Qtd_Vendidos'].sum().sort_values(ascending=False)

top_20_vendas = vendas_por_cat.head(10)

plt.figure(figsize=(10, 8))
sns.barplot(
    x=top_20_vendas.values,
    y=top_20_vendas.index,
    hue=top_20_vendas.index,
    palette='viridis',
    legend=False)
plt.title('Top 20 Categorias por Quantidade Vendida')
plt.xlabel('Total Vendido')
plt.ylabel('Categoria')
plt.show()

# Pizza
plt.figure(figsize=(8, 8))
df["Material"].value_counts().head(8).plot.pie( # head(10) para não poluir a pizza
    autopct='%1.0f%%',
    startangle=90,
    colors=sns.color_palette('pastel')
)
plt.title("Distribuição Percentual de produtos por Material")
plt.ylabel('') # Remove barra lateral
plt.show()

# Avaliação dos Clientes/ Densidade
plt.figure(figsize=(8, 8))
sns.kdeplot(df["Nota_MinMax"], fill=True, color='red')
plt.title("Densidade de avaliações")
plt.xlabel("Nota da Avaliação")
plt.ylabel("Densidade")
plt.show()

# Gráfico de Regressão Desconto/Vendas
# Converter as colunas para numérico
df['Desconto_MinMax'] = pd.to_numeric(df['Desconto_MinMax'], errors='coerce')
df['Qtd_Vendidos'] = pd.to_numeric(df['Qtd_Vendidos'], errors='coerce')

# Remover linhas que ficaram com valores vazios
df_clean = df.dropna(subset=['Desconto_MinMax', 'Qtd_Vendidos'])

#df_clean
plt.figure(figsize=(10, 6))
sns.regplot(
    data=df_clean,
    x='Desconto_MinMax',
    y='Qtd_Vendidos',
    scatter_kws={'alpha': 0.3},
    line_kws={'color': 'blue'}
)
plt.title('Impacto do Desconto nas Vendas')
plt.xlabel('Desconto (Normalizado)')
plt.ylabel('Quantidade Vendida')
plt.show()