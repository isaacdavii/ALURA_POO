# Adicionar numero de portas
from modelos.veiculo import Veiculo

class Carro(Veiculo):
    carros = []
    
    def __init__(self, modelo, cor, ano, marca, preco, portas):
        super().__init__(modelo, cor, ano, marca, preco)
        self._portas = portas
        Carro.carros.append(self)
        
    @property
    def portas(self):
        return self._portas
    
    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano} | {self.marca} | {self.preco} | {self.ligado} | {self.portas}'
    
    @classmethod
    def listar_carros(cls):
        print(f"{'Modelo'.ljust(15)} | {'Cor'.ljust(15)} | {'Ano'.ljust(15)} | {'Marca'.ljust(15)} | {'Preço'.ljust(10)} | {'Ligado'.ljust(10)} | {'Nº Portas'}")
        print('-' * 110)
        for carro in cls.carros:
            print(f"{carro.modelo.ljust(15)} | {carro.cor.ljust(15)} | {str(carro.ano).ljust(15)} | {carro.marca.ljust(15)} | {str(carro.preco).ljust(10)} | {carro.ligado.ljust(10)} | {carro.portas}")