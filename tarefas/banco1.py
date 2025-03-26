class ContaBancaria:
    contas = []

    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        ContaBancaria.contas.append(self)

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return "ON" if self._ativo else "OFF"

    def __str__(self):
        return f"{self._titular.ljust(5)} | {self._saldo} | {self._ativo}"

    def ativar_conta(self):
        self._ativo = not self._ativo

    @classmethod
    def listar_contas(cls):
        print(f"{'Titular'.ljust(7)} | {'Saldo'.ljust(7)} | {'Status'}")
        print("-" * 30)
        for conta in cls.contas:
            print(f"{conta.titular.ljust(7)} | {str(conta.saldo).ljust(7)} | {conta.ativo}")


conta1 = ContaBancaria("João", 1_000)
conta2 = ContaBancaria("Maria", 2_000)

# print(conta1)
# print(conta2)

"""conta1.ativar_conta()
print(conta1.ativo)
conta1.ativar_conta()
print(conta1.ativo)"""

conta1.ativar_conta()
ContaBancaria.listar_contas()


class ClienteBanco:
    clientes = []

    def __init__(self, nome, idade, cpf, endereco, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        ClienteBanco.clientes.append(self)

    @classmethod
    def listar_clientes(cls):
        for cliente in cls.clientes:
            print(f"Nome: {cliente.nome}, Idade: {cliente.idade}, CPF: {cliente.cpf}, Endereço: {cliente.endereco}, Telefone: {cliente.telefone}")


# Instanciando 3 objetos da classe ClienteBanco
cliente1 = ClienteBanco("Carlos", 30, "123.456.789-00", "Rua A, 123", "1111-1111")
cliente2 = ClienteBanco("Ana", 25, "987.654.321-00", "Rua B, 456", "2222-2222")
cliente3 = ClienteBanco("Pedro", 40, "456.789.123-00", "Rua C, 789", "3333-3333")

# Imprimindo o valor da propriedade titular da conta1
print(conta1.titular)

# Listando os clientes
ClienteBanco.listar_clientes()
