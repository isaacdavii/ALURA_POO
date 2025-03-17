from modelos.carro import Carro
from modelos.moto import Moto

carro1 = Carro('Toyota', 'azul', 2020, 'Corolla', 20_020, 3)
carro2 = Carro('Honda', 'preto', 2019, 'Civic', 19_000, 4)
carro3 = Carro('Ford', 'branco', 2018, 'Focus', 18_000, 2)

moto1 = Moto('Yamaha', 'vermelha', 2021, 'YZF-R3', 9_000, 'esportiva')
moto2 = Moto('Kawasaki', 'amarela', 2020, 'Ninja 400', 20_000, 'casual')
moto3 = Moto('Honda', 'preta', 2019, 'CBR500R', 12_000, 'esportiva')

def main():
    # print(carro1)
    # carro1.alterar_estado()
    # print(carro1)
    # print()
    # print(moto3)
    # print()
    
    Carro.listar_carros()
    print()
    Moto.listar_motos()

if __name__ == '__main__':
    main()
    