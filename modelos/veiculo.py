from abc import ABC, abstractmethod

class Veiculo:
    veiculos = []

    def __init__(self, modelo, cor, ano, marca, preco):
        self._modelo = (modelo.title())
        self._cor = (cor.title())
        self._ano = ano
        self._marca = (marca.title())
        self._preco = preco
        self._ligado = False
        Veiculo.veiculos.append(self)

    def __str__(self):
        return f"{self.modelo} | {self.cor} | {self.ano} | {self.marca} | {self.preco} | {self.ligado}"

    @classmethod
    def listar_veiculos(cls):
        print(f"{'Modelo'.ljust(15)} | {'Cor'.ljust(15)} | {'Ano'.ljust(15)} | {'Marca'.ljust(15)} | {'Preco'.ljust(10)} | {'Ligado'}")
        print("-" * 93)
        for veiculo in cls.veiculos:
            print(f"{veiculo.modelo.ljust(15)} | {veiculo.cor.ljust(15)} | {str(veiculo.ano).ljust(15)} | {veiculo.marca.ljust(15)} | {str(veiculo.preco).ljust(10)} | {veiculo.ligado}")

    @property
    def ligado(self):
        return 'ON' if self._ligado else 'OFF'
    @property
    def modelo(self):
        return self._modelo
    @property
    def cor(self):
        return self._cor
    @property
    def ano(self):
        return self._ano
    @property
    def marca(self):
        return self._marca
    @property
    def preco(self):
        return self._preco

    # def alterar_estado(self):
    #     self._ligado = not self._ligado
        
    @abstractmethod
    def ligar(self):
        pass
        
        
        
        
        
        
        
        

# Para teste de funções
# veiculo1 = Veiculo("Gol", "Branco", 2019, "Volkswagen", 50_000)
# veiculo2 = Veiculo("Civic", "Preto", 2019, "Honda", 80_000)
# veiculo3 = Veiculo("Onix", "Prata", 2019, "Chevrolet", 60_000)
# veiculo4 = Veiculo("HB20", "Azul", 2019, "Hyundai", 55_000)

# Veiculo.listar_veiculos()
# veiculo1.ligar()
# print()
# Veiculo.listar_veiculos()
