import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

#exibir texto
print (extracao.text.strip())

#filtrar a exibição pela teg
for linha_texto in extracao.find_all ('h2, p'):
    titulo = linha_texto.text.strip()
    print('titulo: ', titulo)

#Contar quantidade de parágrafos e títulos
contar_titulos = 0
contar_paragrafos = 0

#Filtrar tags
for linha_texto in extracao.find_all(['h2, p']):
    if linha_texto.name == 'h2':
        contar_titulos += 1
        print ('titulo: \n', contar_titulos)
    elif linha_texto.name == 'p':
        contar_paragrafos += 1
        print ('parágrafos: \n', contar_paragrafos)