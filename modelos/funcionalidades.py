import os

from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

def exibir_nome_do_programa():
    print("""
Ｓａｂｏｒ Ｅｘｐｒｅｓｓ
""")

def exibir_opcoes():
    print('1. Cadastrar')
    print('2. Listar')
    print('3. Alterar status do restaurante')
    print('4. Sair\n')
    
def exibir_cadastros():
    print('\n1. Cadastrar restaurante')
    print('2. Cadastrar prato')
    print('3. Cadastrar bebida')
    print('4. Cadastrar sobremesa')
    print('5. Voltar ao menu principal\n')
    
def exibir_listagens():
    print('\n1. Listar restaurantes')
    print('2. Listar pratos')
    print('3. Listar bebidas')
    print('4. Listar sobremesas')
    print('5. Voltar ao menu principal\n')

def escolher_opcao(main_func):
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            escolher_cadastro(main_func)
        elif opcao_escolhida == 2:
            escolher_listagem(main_func)
        elif opcao_escolhida == 3:
            alternar_status_restaurante(main_func)
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida(main_func)
    except ValueError:
        opcao_invalida(main_func)
        
def escolher_cadastro(main_func):
    exibir_cadastros()
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante(main_func)
        elif opcao_escolhida == 2:
            cadastrar_novo_prato(main_func)
        elif opcao_escolhida == 3:
            cadastrar_nova_bebida(main_func)
        elif opcao_escolhida == 4:
            cadastrar_sobremesa(main_func)
        elif opcao_escolhida == 5:
            main_func()
        else:
            opcao_invalida(main_func)
    except ValueError:
        opcao_invalida(main_func)

def escolher_listagem(main_func):
    exibir_listagens()
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            listar_restaurantes(main_func)
        elif opcao_escolhida == 2:
            listar_pratos(main_func)
        elif opcao_escolhida == 3:
            listar_bebidas(main_func)
        elif opcao_escolhida == 4:
            listar_sobremesas(main_func)
        elif opcao_escolhida == 5:
            main_func()
        else:
            opcao_invalida(main_func)
    except ValueError:
        opcao_invalida(main_func)

def opcao_invalida():
    print('Opção inválida!')
    voltar_ao_menu_principal(main)

def voltar_ao_menu_principal(main_func):
    input('\nDigite uma tecla para voltar ao menu principal.\n')
    main_func()
    
def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar(main_func):
    exibir_subtitulo('CADASTRAR!')
    exibir_cadastros()
    escolher_cadastro(main_func)
    
def listar(main_func):
    exibir_subtitulo('LISTAR!')
    exibir_listagens()
    escolher_listagem(main_func)

def cadastrar_novo_restaurante(main_func):
    exibir_subtitulo('CADASTRAR NOVO RESTAURANTE!')
    
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ') 
    dados_do_restaurante = Restaurante(nome_do_restaurante, categoria)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    #Restaurante.restaurantes.append(dados_do_restaurante)
    
    voltar_ao_menu_principal(main_func)

def listar_restaurantes(main_func):
    exibir_subtitulo('LISTANDO RESTAURANTES!')
    
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    
    for restaurante in Restaurante.restaurantes:
        nome_restaurante = restaurante._nome
        categoria = restaurante._categoria
        ativo = 'Ativado' if restaurante._ativo else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    voltar_ao_menu_principal(main_func)

def cadastrar_novo_prato(main_func):
    exibir_subtitulo('CADASTRAR NOVO PRATO!')
    
    nome_do_prato = input('Digite o nome do prato que deseja cadastrar: ')
    preco = float(input(f'Digite o preço do prato {nome_do_prato}: '))
    descricao = input(f'Digite a descrição do prato {nome_do_prato}: ')
    prato = Prato(nome_do_prato, preco, descricao)
    print(f'O prato {nome_do_prato} foi cadastrado com sucesso!')
    #Prato.pratos.append(prato)
    
    voltar_ao_menu_principal(main_func)    
 
def listar_pratos(main_func):
    exibir_subtitulo('LISTANDO PRATOS!')
    
    print(f'{'Nome do prato'.ljust(22)} | {'Preço'.ljust(20)} | {'Descrição'}')
    
    for prato in Prato.pratos:
        nome_prato = prato._nome
        preco = prato._preco
        descricao = prato._descricao
        print(f'- {nome_prato.ljust(20)} | {str(preco).ljust(20)} | {descricao}')
    
    voltar_ao_menu_principal(main_func)

def cadastrar_nova_bebida(main_func):
    exibir_subtitulo('CADASTRAR NOVA BEBIDA!')
    
    nome_da_bebida = input('Digite o nome da bebida que deseja cadastrar: ')
    preco = float(input(f'Digite o preço da bebida {nome_da_bebida}: '))
    tamanho = input(f'Digite a descrição da bebida {nome_da_bebida}: ')
    bebida = Bebida(nome_da_bebida, preco, tamanho)
    print(f'A bebida {nome_da_bebida} foi cadastrada com sucesso!')
    #Bebida.bebidas.append(bebida)
    
    voltar_ao_menu_principal(main_func)

def listar_bebidas(main_func):
    exibir_subtitulo('LISTANDO BEBIDAS!')
    
    print(f'{'Nome da bebida'.ljust(22)} | {'Preço'.ljust(20)} | {'Descrição'}')
    
    for bebida in Bebida.bebidas:
        nome_bebida = bebida._nome
        preco = bebida._preco
        tamanho = bebida._tamanho
        print(f'- {nome_bebida.ljust(20)} | {str(preco).ljust(20)} | {tamanho}')
    
    voltar_ao_menu_principal(main_func)   

def cadastrar_sobremesa(main_func):
    exibir_subtitulo('CADASTRAR NOVA SOBREMESA!')
    
    nome_sobremesa = input('Digite o nome da sobremesa que deseja cadastrar: ')
    preco = float(input(f'Digite o preço da sobremesa {nome_sobremesa}: '))
    tipo = input(f'Digite o tipo da sobremesa {nome_sobremesa}: ')
    tamanho = input(f'Digite o tamanho da sobremesa {nome_sobremesa}: ')
    descricao = input(f'Digite a descrição da sobremesa {nome_sobremesa}: ')
    sobremesa = Sobremesa(nome_sobremesa, preco, tipo, tamanho, descricao)
    print(f'A sobremesa {nome_sobremesa} foi cadastrada com sucesso!')
    #Sobremesa.sobremesas.append(sobremesa)
    
    voltar_ao_menu_principal(main_func)

def listar_sobremesas(main_func):
    exibir_subtitulo('LISTANDO SOBREMESAS!')
    
    print(f'{'Nome da sobremesa'.ljust(22)} | {'Preço'.ljust(20)} | {'Tipo'.ljust(20)} | {'Tamanho'.ljust(20)} | {'Descrição'}')
    for sobremesa in Sobremesa.sobremesas:
        nome_sobremesa = sobremesa._nome
        preco = sobremesa._preco
        tipo = sobremesa._tipo
        tamanho = sobremesa._tamanho
        descricao = sobremesa._descricao
        print(f'- {nome_sobremesa.ljust(20)} | {str(preco).ljust(20)} | {tipo.ljust(20)} | {tamanho.ljust(20)} | {descricao}')
    
    voltar_ao_menu_principal(main_func)


def alternar_status_restaurante(main_func):
    exibir_subtitulo('ALTERANDO STATUS DO RESTAURANTE')
    
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o status: ')
    restaurante_encontrado = False
    
    for restaurante in Restaurante.restaurantes:
        if nome_restaurante == restaurante._nome:
            restaurante_encontrado = True
            restaurante._ativo = not restaurante._ativo
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante._ativo else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')
    
    voltar_ao_menu_principal(main_func) 

def finalizar_app():
    exibir_subtitulo('Finalizando o aplicativo!')




#feat: adicionar avaliação ao restaurante
#feat: listar a média de avaliação do restaurante
#feat: listar as avaliações do restaurante
#feat: adicionar item (prato, bebida, sobremesa) ao cardápio de um restaurante

        
        