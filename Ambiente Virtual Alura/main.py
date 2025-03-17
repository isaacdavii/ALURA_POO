from fastapi import FastAPI, Query
import requests

app = FastAPI() # Create an instance of FastAPI

@app.get('/api/hello') # Define a route // IP:8000/api/hello 
def hello_world():
    '''
    Endpoint que exibe a mensagem "Hello World"
    '''
    return {'Hello': 'World'} 
# To run: " uvicorn main:app --reload "

@app.get('/api/restaurantes/') # Define a route // IP:8000/api/restaurantes
def restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint que exibe os restaurantes e seus cardápios
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json' # URL of the API
    response = requests.get(url) # Make a GET request to the URL//Pegar a informação para trabalhar no projeto
    print(response) # Print the response // Deve retornar [200] se a conexão foi bem sucedida
    # print(response.json()) # Print the JSON response // Deve retornar o JSON com os restaurantes

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}

        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                    })
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
    else:
        return{'Erro': f'O servidor retornou o erro: {response.status_code} - {response.text}'}
        









