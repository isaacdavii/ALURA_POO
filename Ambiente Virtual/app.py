import requests # Import the requests library
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json' # URL of the API
response = requests.get(url) # Make a GET request to the URL//Pegar a informação para trabalhar no projeto
print(response) # Print the response // Deve retornar [200] se a conexão foi bem sucedida
# print(response.json()) # Print the JSON response // Deve retornar o JSON com os restaurantes

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []
        dados_restaurante[nome_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })
    
else:
    print(f'O servidor retornou o erro: {response.status_code}')


print(dados_restaurante['Pizza Hut'])

for nome_restaurante, dados in dados_restaurante.items():
    nome_arquivo = f'{nome_restaurante}.json'
    with open(nome_arquivo, 'w') as arquivo_restaurantes:
        json.dump(dados, arquivo_restaurantes, indent = 4)
        print(f'Arquivo {nome_arquivo} criado com sucesso')
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    