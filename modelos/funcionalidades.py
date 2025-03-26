import os

from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa
from modelos.avaliacao import Avaliacao

def exibir_nome_do_programa():
    print("""
Ｓａｂｏｒ Ｅｘｐｒｅｓｓ
""")

def exibir_opcoes():
    print('1. Cadastrar')
    print('2. Listar')
    print('3. Adicionar avaliação a um restaurante')
    print('4. Mostrar cardápio de um restaurante')
    print('5. Adicionar item ao cardápio de um restaurante')
    print('6. Alterar status do restaurante')
    print('7. Sair\n')
    
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
    print('5. Listar TODAS as avaliações por restaurante')
    print('6. Listar MÉDIA das avaliações por restaurante')
    print('7. Voltar ao menu principal\n')

def escolher_opcao(main_func):
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            escolher_cadastro(main_func)
        elif opcao_escolhida == 2:
            escolher_listagem(main_func)
        elif opcao_escolhida == 3:
            adicionar_avaliacao(main_func)
        elif opcao_escolhida == 4:
            mostrar_cardapio(main_func)
        elif opcao_escolhida == 5:
            adicionar_item_ao_cardapio_de_restaurante(main_func)
        elif opcao_escolhida == 6:
            alternar_status_restaurante(main_func)
        elif opcao_escolhida == 7:
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
            listar_todas_avaliacoes(main_func)
        elif opcao_escolhida == 6:
            listar_media_avaliacoes(main_func)
        elif opcao_escolhida == 7:
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

def adicionar_avaliacao(main_func):
    exibir_subtitulo('ADICIONANDO AVALIAÇÃO AO RESTAURANTE')
    
    nome_restaurante = input('Digite o nome do restaurante que deseja avaliar: ')
    restaurante_encontrado = False
    
    for restaurante in Restaurante.restaurantes:
        if nome_restaurante == restaurante._nome:
            restaurante_encontrado = True
            cliente = input('Digite o nome do cliente: ')
            nota = int(input('Digite a nota da avaliação (de 1 a 5): '))
            if nota not in range(1, 6):
                print('Nota inválida!')
                nota = int(input('Digite a nota da avaliação (de 1 a 5): '))
            avaliacao = Avaliacao(cliente, nota)
            restaurante._avaliacao.append(avaliacao)
            print(f'A avaliação do cliente {cliente} foi adicionada com sucesso!')
            break
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')
    
    voltar_ao_menu_principal(main_func)
            
def listar_todas_avaliacoes(main_func):
    exibir_subtitulo('LISTANDO TODAS AS AVALIAÇÕES POR RESTAURANTE')
    
    nome_restaurante = input('Digite o nome do restaurante que deseja ver as avaliações: ')
    restaurante_encontrado = False
    
    for restaurante in Restaurante.restaurantes:
        if restaurante._nome == nome_restaurante:
            restaurante_encontrado = True
            print(f'\nAvaliações do restaurante {restaurante._nome}')
            print(f'{"Cliente".ljust(20)} | {"Nota".ljust(10)}')
            print('-' * 30)
            for avaliacao in restaurante._avaliacao:
                print(f'{avaliacao._cliente.ljust(20)} | {str(avaliacao._nota).ljust(10)}')
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')
        
    voltar_ao_menu_principal(main_func)
    
def listar_media_avaliacoes(main_func):
    exibir_subtitulo('LISTANDO MÉDIA DAS AVALIAÇÕES POR RESTAURANTE')
    
    for restaurante in Restaurante.restaurantes:
        if not restaurante._avaliacao:
            media = '-'
        else:
            soma_notas = sum([avaliacao._nota for avaliacao in restaurante._avaliacao])
            media = round(soma_notas / len(restaurante._avaliacao), 1)
        print(f'A média das avaliações do restaurante {restaurante._nome} é {media}')
        
    voltar_ao_menu_principal(main_func)

def mostrar_cardapio(main_func):
    exibir_subtitulo('MOSTRANDO CARDAPIO')
    
    nome_restaurante = input('Digite o nome do restaurante que deseja ver o cardáopio: ')
    restaurante_encontrado = False
    
    for restaurante in Restaurante.restaurantes:
        if nome_restaurante == restaurante._nome:
            restaurante_encontrado = True
            print(f'\nCardárpio do restaurante {restaurante._nome}')
            print('-' * 50)
            for i, item in enumerate(restaurante._cardapio, start = 1):
                if hasattr(item, 'descricao'):
                    mensagem_prato = f'{i}. Nome: {item.nome.ljust(20)} | Preço: R${str(item.preco).ljust(10)} | Descrição: {item.descricao} '
                    print(mensagem_prato)
                else:
                    mensagem_bebida = f'{i}. Nome: {item.nome.ljust(20)} | Preço: R${str(item.preco).ljust(10)} | Tamanho: {item.tamanho}'
                    print(mensagem_bebida)
        
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')
    
    voltar_ao_menu_principal(main_func)

def adicionar_item_ao_cardapio_de_restaurante(main_func):
    nome_restaurante = input('Digite o nome do restaurante que deseja adicionar um item ao cardápio: ')
    restaurante_encontrado = False
    
    for restaurante in Restaurante.restaurantes:
        if nome_restaurante == restaurante._nome:
            restaurante_encontrado = True
            tipo_item = input("""Digite o tipo do item que deseja adicionar ao cardápio
1. Prato
2. Bebida
3. Sobremesa
Insira o tipo: """)
            if tipo_item == '1':
                nome_prato = input('Digite o nome do prato que deseja adicionar ao cardápio: ')
                preco_prato = float(input(f'Digite o preço do prato {nome_prato}: '))
                descricao_prato = input(f'Digite a descrição do prato {nome_prato}: ')
                prato = Prato(nome_prato, preco_prato, descricao_prato)
                restaurante._cardapio.append(prato)
                print(f'O prato {nome_prato} foi adicionado ao cardápio do restaurante {nome_restaurante} com sucesso!')
            elif tipo_item == '2':
                nome_bebida = input('Digite o nome da bebida que deseja adicionar ao cardápio: ')
                preco_bebida = float(input(f'Digite o preço da bebida {nome_bebida}: '))
                tamanho_bebida = input(f'Digite o tamanho da bebida {nome_bebida}: ')
                bebida = Bebida(nome_bebida, preco_bebida, tamanho_bebida)
                restaurante._cardapio.append(bebida)
                print(f'A bebida {nome_bebida} foi adicionada ao cardápio do restaurante {nome_restaurante} com sucesso!')
            elif tipo_item == '3':
                nome_sobremesa = input('Digite o nome da sobremesa que deseja adicionar ao cardápio: ')
                preco_sobremesa = float(input(f'Digite o preço da sobremesa {nome_sobremesa}: '))
                tipo_sobremesa = input(f'Digite o tipo da sobremesa {nome_sobremesa}: ')
                tamanho_sobremesa = input(f'Digite o tamanho da sobremesa {nome_sobremesa}: ')
                descricao_sobremesa = input(f'Digite a descrição da sobremesa {nome_sobremesa}: ')
                sobremesa = Sobremesa(nome_sobremesa, preco_sobremesa, tipo_sobremesa, tamanho_sobremesa, descricao_sobremesa)
                restaurante._cardapio.append(sobremesa)
                print(f'A sobremesa {nome_sobremesa} foi adicionada ao cardápio do restaurante {nome_restaurante} com sucesso!')
            else:
                print('Opção inválida!')
                tipo_item = input("""Digite o tipo do item que deseja adicionar ao cardápio
1. Prato
2. Bebida
3. Sobremesa
Insira o tipo: """)
    
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')
        
    voltar_ao_menu_principal(main_func)
        
        