import requests
from bs4 import BeautifulSoup
import pandas
response = requests.get('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa')
print(response.text[:1000])

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:9000])





print('pandas: ')
url_dados = pandas.read_html('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa')
print(url_dados[0].head(10))