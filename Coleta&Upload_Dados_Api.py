import requests

#ENVIA O ARQUIVO
def enviar_arquivo():
    # Caminho para upload
    caminho = "C:/Users/vagne/Downloads/produtos_informatica.xlsx"

    #enviar arquivo
    requisicao = requests.post(
        url='https://upload.gofile.io/uploadFile', files={'file': open(caminho, 'rb')})


    saida_requisicao = requisicao.json()
    print(saida_requisicao)
    url = saida_requisicao['data']['downloadPage']
    print('Arquivo enviado. Link para acesso', url)