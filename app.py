# Programa Principal
import os

from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa
from modelos.funcionalidades import escolher_opcao, exibir_nome_do_programa, exibir_opcoes

# Teste de adicionar restaurante
restaurante_praca = Restaurante("praça", "gourmet")
restaurante_mexicano = Restaurante("ariba mex", "mexicana")
restaurante_japones = Restaurante("katana", "japonesa")
restaurante_tailandes = Restaurante("sukho thai", "tailandesa")
restaurante_pizza = Restaurante("pizza place", "italiana")

# Teste de adicionar prato
prato1 = Prato("Yakisoba", 30.43, "Macarrão frito com legumes e carne")
prato1.aplicar_desconto()
prato2 = Prato("Sushi", 50.98, "Peixe cru com arroz")
prato3 = Prato("Pad Thai", 40.50, "Macarrão de arroz frito com camarão")
prato4 = Prato("Pizza de Calabresa", 35.67, "Pizza com calabresa e cebola")

# Teste de adicionar bebida
bebida1 = Bebida("Coca-Cola Zero", 9.00, "600ml")
bebida2 = Bebida("Suco de Laranja", 8.00, "500ml")
bebida3 = Bebida("Água", 3.00, "500ml")
bebida3.aplicar_desconto()
bebida4 = Bebida("Guaraná", 6.00, "600ml")

# Teste de alterar estado
# restaurante_praca.alterar_estado()
# restaurante_mexicano.alterar_estado
# restaurante_japones.alterar_estado()

# Teste de adicionar avaliação
restaurante_mexicano.adicionar_avaliacao("João", 5)
restaurante_japones.adicionar_avaliacao("Maria", 4)
restaurante_praca.adicionar_avaliacao("José", 3)
restaurante_praca.adicionar_avaliacao("Ana", 5)
restaurante_praca.adicionar_avaliacao("Carlos", 4)
restaurante_mexicano.adicionar_avaliacao("Marta", 2)

# # Teste de adicionar bebida ao cardápio
# restaurante_praca.adicionar_bebida_cardapio(bebida1)
# restaurante_tailandes.adicionar_bebida_cardapio(bebida2)

# # Teste de adicionar prato ao cardápio
# restaurante_mexicano.adicionar_prato_cardapio(prato1)
# restaurante_pizza.adicionar_prato_cardapio(prato2)

# Teste de adicionar ao cardapio
restaurante_mexicano.adicionar_item_cardapio(prato1)
restaurante_mexicano.adicionar_item_cardapio(bebida3)
restaurante_pizza.adicionar_item_cardapio(prato2)
restaurante_praca.adicionar_item_cardapio(bebida1)
restaurante_tailandes.adicionar_item_cardapio(bebida2)

# Teste de adicionar sobremesa
sobremesa1 = Sobremesa("Pudim", 10.00, "Doce de leite", "Pequeno", "Pudim de leite condensado")
sobremesa2 = Sobremesa("Sorvete", 8.00, "Chocolate", "Grande", "Sorvete de chocolate")
sobremesa3 = Sobremesa("Bolo de Chocolate", 15.00, "Chocolate", "Médio", "Bolo de chocolate com cobertura")
sobremesa4 = Sobremesa("Torta de Limão", 12.00, "Limão", "Pequeno", "Torta de limão com merengue")

# Agora, devo adicionar as sobremesas ao cardápio
restaurante_pizza.adicionar_item_cardapio(sobremesa1)
restaurante_praca.adicionar_item_cardapio(sobremesa2)
restaurante_mexicano.adicionar_item_cardapio(sobremesa3)
restaurante_japones.adicionar_item_cardapio(sobremesa4)


def main():
    os.system('cls') #usada para limpar a tela
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao(main_func = main)

if __name__ == "__main__":
    main()

# def main():
#     # Restaurante.listar_restaurantes()
#     # # print(prato1)
#     # print()
#     # # print(bebida1)
#     # # print()
#     # Prato.listar_pratos()
#     # print()
#     # Bebida.listar_bebidas()
#     restaurante_praca.exibir_cardapio()
#     print()
#     restaurante_mexicano.exibir_cardapio()
#     print()
#     restaurante_tailandes.exibir_cardapio()
#     print()
#     restaurante_pizza.exibir_cardapio()
#     print()
#     restaurante_japones.exibir_cardapio()
#     print()
#     restaurante_mexicano.listar_avaliacoes()
#     print()
#     restaurante_praca.listar_avaliacoes()
#     print()
#     restaurante_praca.media_avaliacoes
#     print()



# if __name__ == "__main__":
#     main()
