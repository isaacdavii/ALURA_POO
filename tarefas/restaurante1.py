class Restaurante:
    nome = ''
    categoria = ''
    ativo = False


restaurante_praca = Restaurante()
restaurante_praca.nome = "Praça"
restaurante_praca.categoria = "Italiana"
#restaurante_praca.ativo = True

restaurante_pizza = Restaurante()
restaurante_pizza.nome = "Pizza Place"
restaurante_pizza.categoria = "Fast food"
#restaurante_pizza.ativo = True

restaurantes = [restaurante_praca, restaurante_pizza]
#print(vars(restaurante_pizza))
#print(dir(restaurante_pizza))
print(restaurante_praca.ativo)