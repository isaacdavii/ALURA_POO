# ALURA_POO

Este repositório contém materiais e exercícios relacionados ao curso de **Programação Orientada a Objetos (POO)** oferecido pela Alura. O objetivo do projeto é aplicar os conceitos fundamentais da POO em Python por meio de exemplos práticos e desafios. O projeto utiliza **FastAPI** para criar endpoints REST, incluindo um endpoint para listar restaurantes e seus cardápios.

## Estrutura do Repositório

A estrutura do repositório é composta pelos seguintes diretórios e arquivos:

### Diretórios
- `__pycache__` - Contém os arquivos de cache gerados pelo Python.
- `modelos` - Abriga as definições das classes utilizadas no projeto para `app.py`, `biblioteca.py` e `main.py`.
- `tarefas` - Contém exercícios ou tarefas práticas realizadas durante o curso.

### Arquivos
- `app.py` - Arquivo principal que possui as funcionalidades referente ao cadastro de restaurantes, bebidas, pratos, avaliação.
- `appi.py` - Contém a interface de um aplicativo que que cadastra, lista e restaurantes.
- `biblioteca.py` - Arquivo principal para o exercício referente a um sistema de Biblioteca.
- `main.py` - Arquivo principal para o exercício referente a visualização e cadastro de veículos.
- `requirements.txt` - Lista de dependências necessárias para executar o projeto. Isso diz respeito à criação do ambiente virtual.

## Funcionalidades

- Implementação de classes e objetos.
- Definição de métodos e atributos.
- Exercícios práticos para reforçar os conceitos de POO.
- Estrutura modular para facilitar o aprendizado e a manutenção do código.

## Tecnologias Utilizadas

- Python 3.13.2
- FastAPI
- Requests
- Uvicorn

## Dependências

Para rodar o projeto, instale as dependências listadas em `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Endpoints da API

### `GET /api/hello`
Retorna uma mensagem de boas-vindas.

### `GET /api/restaurantes/`
Busca informações sobre restaurantes e seus cardápios:
- Sem parâmetro: retorna todos os restaurantes.
- Com `?restaurante=nome`: retorna o cardápio do restaurante especificado.

## Como Executar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/isaacdavii/ALURA_POO.git
   ```
   
2. **Navegue até o diretório do projeto**:   
   ```bash
   cd ALURA_POO
   ```
   
3. **Execute o arquivo principal**:
   ```bash
   python app.py
   ```
   
   *Observação*: Caso o arquivo `main.py` seja o ponto de entrada principal, substitua `app.py` por `main.py` no comando acima.

4. **Execute o servidor FastAPI**:
   ```bash
   uvicorn main:app --reload
   ```

## Como Contribuir

1. Faça um fork do projeto.

2. Crie uma nova branch com a sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Commit suas mudanças:
   ```bash
   git commit -m 'Adiciona minha feature'
   ```
4. Faça um push para a branch:
   ```bash
   git push origin minha-feature
   ```
5. Envie um Pull Request.

## Contato

Para mais informações, entre em contato pelo email: izaacddavid98@gmail.com.

## Referências

- [Documentação do Python](https://docs.python.org/pt-br/3/)
- [Documentação oficial do FastAPI](https://fastapi.tiangolo.com/)