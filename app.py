from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_praca.receber_avaliacao("Joao", 9)
restaurante_praca.receber_avaliacao("Emy", 5)
restaurante_praca.receber_avaliacao("Ana", 6.5)
restaurante_japones = Restaurante("Iwata", "Japones")

"""restaurante_mexicano = Restaurante("Mechi Can", "Mexicano")
restaurante_japones.alternar_estado()"""


def main():
    Restaurante.listar_restaurantes()


if __name__ == "__main__":
    main()
