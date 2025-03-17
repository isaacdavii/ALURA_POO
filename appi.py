import os

restaurantes = [{'nome': 'EmiciDonaids', 'categoria': 'Fast Food', 'ativo': False},
                {'nome': 'Chicken House', 'categoria': 'Fast Food', 'ativo': True},
                {'nome': 'Sem Nome', 'categoria': 'Restaurante', 'ativo': True}]   

pratos = [{'nome': 'X-Bacon', 'preco': 15.00, 'descricao': 'Pão, hambúrguer, bacon, queijo, alface, tomate e maionese'},
          {'nome': 'X-Tudo', 'preco': 20.00, 'descricao': 'Pão, hambúrguer e tudo o que você tem direito'},
          {'nome': 'X-Salada', 'preco': 12.00, 'descricao': 'Pão, hambúrguer, queijo, alface, tomate e maionese'}]   

bebidas = [{'nome': 'Coca-Cola', 'preco': 5.00, 'descricao': 'Lata 350ml'},
           {'nome': 'Guaraná', 'preco': 5.00, 'descricao': 'Lata 350ml'},
           {'nome': 'Fanta', 'preco': 12.00, 'descricao': 'Garrafa 2L'}]          

def exibir_nome_do_programa():
    print("""
Ｓａｂｏｒ Ｅｘｐｒｅｓｓ
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Cadastrar prato')
    print('4. Listar pratos')
    print('5. Cadastrar bebida')
    print('6. Listar bebidas')
    print('7. Alternar status do restaurante')
    print('8. Sair\n')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3:
            cadastrar_novo_prato()
        elif opcao_escolhida == 4:
            listar_pratos()
        elif opcao_escolhida == 5:
            cadastrar_nova_bebida()
        elif opcao_escolhida == 6:
            listar_bebidas()
        elif opcao_escolhida == 7: 
            alternar_status_restaurante()
        elif opcao_escolhida == 8: 
            finalizar_app()
        else: 
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def opcao_invalida():
    print('Opção inválida!')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal.\n')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('CADASTRAR NOVO RESTAURANTE!')
    
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ') 
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    restaurantes.append(dados_do_restaurante)
    
    voltar_ao_menu_principal()
    
def cadastrar_novo_prato():
    exibir_subtitulo('CADASTRAR NOVO PRATO!')
    
    nome_do_prato = input('Digite o nome do prato que deseja cadastrar: ')
    preco = float(input(f'Digite o preço do prato {nome_do_prato}: '))
    descricao = input(f'Digite a descrição do prato {nome_do_prato}: ')
    prato = {'nome': nome_do_prato, 'preco': preco, 'descricao': descricao}
    print(f'O prato {nome_do_prato} foi cadastrado com sucesso!')
    pratos.append(prato)
    
    voltar_ao_menu_principal()    
    
def cadastrar_nova_bebida():
    exibir_subtitulo('CADASTRAR NOVA BEBIDA!')
    
    nome_da_bebida = input('Digite o nome da bebida que deseja cadastrar: ')
    preco = float(input(f'Digite o preço da bebida {nome_da_bebida}: '))
    descricao = input(f'Digite a descrição da bebida {nome_da_bebida}: ')
    bebida = {'nome': nome_da_bebida, 'preco': preco, 'descricao': descricao}
    print(f'A bebida {nome_da_bebida} foi cadastrada com sucesso!')
    bebidas.append(bebida)
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('LISTANDO RESTAURANTES!')
    
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    voltar_ao_menu_principal()
    
def listar_pratos():
    exibir_subtitulo('LISTANDO PRATOS!')
    
    print(f'{'Nome do prato'.ljust(22)} | {'Preço'.ljust(10)} | {'Descrição'}')
    
    for prato in pratos:
        nome_prato = prato['nome']
        preco = prato['preco']
        descricao = prato['descricao']
        print(f'- {nome_prato.ljust(20)} | {str(preco).ljust(10)} | {descricao}')
    
    voltar_ao_menu_principal()
    
def listar_bebidas():
    exibir_subtitulo('LISTANDO BEBIDAS!')
    
    print(f'{'Nome da bebida'.ljust(22)} | {'Preço'.ljust(10)} | {'Descrição'}')
    
    for bebida in bebidas:
        nome_bebida = bebida['nome']
        preco = bebida['preco']
        descricao = bebida['descricao']
        print(f'- {nome_bebida.ljust(20)} | {str(preco).ljust(10)} | {descricao}')
    
    voltar_ao_menu_principal()

def alternar_status_restaurante():
    exibir_subtitulo('ALTERANDO STATUS DO RESTAURANTE')
    
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o status: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')
    
    voltar_ao_menu_principal()    

def finalizar_app():
    exibir_subtitulo('Finalizando o aplicativo!')

def main():
    os.system('cls') #usada para limpar a tela
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
