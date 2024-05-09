import json
import urllib.request

# Solicitar ao usuario o CEP
cep = input("Digite o CEP: ")

# Construir na URL de consulta
url = f" https://viacep.com.br/ws/{cep}/json/"

try:
    # Fazer a requisição
    response = urllib.request.urlopen(url)

    # Ler o conteudo da resposta 
    data = response.read().decode('utf-8')

    # Converter JSON em dicionario Python
    endereco = json.loads(data)

    # Verificarse a consulta foi bem-sucedida
    if endereco.get('erro'):
         print("CEP não encontrado")
    else:
        # Armazenar informações em variáveis 
        logradouro = endereco['logradouro']
        complemento = endereco['complemento']
        bairro = endereco['bairro']
        cidade = endereco['localidade']
        estado = endereco['uf']

        # Exibir informações do endereço de tela
        print(f"Logradouro: {logradouro}")
        print(f"Complemento: {complemento}")
        print(f"Cidade: {cidade}")
        print(f"Estado: {estado}")
        # Fechar conexão 
        response.close() 
except Exception as e:
       print(f"Erro: {e}")