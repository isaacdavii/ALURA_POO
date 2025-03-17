import os

restaurantes = [{'nome': 'EmiciDonaids', 'categoria': 'Fast Food', 'ativo': False},
                {'nome': 'Chicken House', 'categoria': 'Fast Food', 'ativo': True},
                {'nome': 'Sem Nome', 'categoria': 'Restaurante', 'ativo': True}]                

def exibir_nome_do_programa():
    print("""
Ｓａｂｏｒ Ｅｘｐｒｅｓｓ
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar status do restaurante')
    print('4. Sair\n')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_status_restaurante()
        elif opcao_escolhida == 4: 
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

def listar_restaurantes():
    exibir_subtitulo('LISTANDO RESTAURANTES!')
    
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
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
