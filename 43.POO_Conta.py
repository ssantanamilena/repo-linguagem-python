class ContaCorrente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    def consultar_saldo(self):
        print(f"Seu saldo é de {self.saldo:.2f}")

    def depositar(self, valor):
        self.saldo += valor

    def sacar_dinheiro(self, valor):
        self.saldo -= valor


# Programa
conta_milena = ContaCorrente("Milena", "460.074.108.03")
conta_milena.consultar_saldo()
# depositar
conta_milena.depositar(1000)
conta_milena.consultar_saldo()
# retirar
conta_milena.sacar_dinheiro(100)
conta_milena.consultar_saldo()

print(conta_milena.saldo)
print(conta_milena.cpf)
