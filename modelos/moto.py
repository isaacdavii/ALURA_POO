from modelos.veiculo import Veiculo

class Moto(Veiculo):
    motos = []
    
    def __init__(self, modelo, cor, ano, marca, preco, tipo):
        super().__init__(modelo, cor, ano, marca, preco)
        self._tipo = (tipo.title())
        Moto.motos.append(self)
        
    @property
    def tipo(self):
        return self._tipo
    
    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano} | {self.marca} | {self.preco} | {self.ligado} | {self.tipo}'
    
    @classmethod
    def listar_motos(cls):
        print(f"{'Modelo'.ljust(15)} | {'Cor'.ljust(15)} | {'Ano'.ljust(15)} | {'Marca'.ljust(15)} | {'Preço'.ljust(10)} | {'Ligado'.ljust(10)} | {'Tipo'}")
        print('-' * 110)
        for moto in cls.motos:
            print (f"{moto.modelo.ljust(15)} | {moto.cor.ljust(15)} | {str(moto.ano).ljust(15)} | {moto.marca.ljust(15)} | {str(moto.preco).ljust(10)} | {moto.ligado.ljust(10)} | {moto.tipo}")