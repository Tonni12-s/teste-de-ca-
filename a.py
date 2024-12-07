# class  Carro:
#     def __init__(self, cor, modelo, ano, marca):
#         self.cor = cor
#         self.modelo = modelo
#         self.ano = ano
#         self.marca = marca
#         self.ligado = False
#         self.capacidade = 50
#         self.tanque = 0
#     def ligar(self):
#         self.ligado = True
#
#     def abastecer(self, qtd):
#         if(self.tanque + qtd <= self.capacidade):
#             self.tanque += qtd
#         else:
#             print("Não é possivel abastecer")
# carro1 = Carro (cor='vermelho', modelo='supra mk4', ano=2018, marca='toyota')
# carro1.ligar()
#
# print(carro1.cor, carro1.ano, carro1.modelo, carro1.ano, carro1.marca)
# print(carro1.tanque)
# carro1.abastecer(40)
# print(carro1.tanque)
class Conta_bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.salario = 0

    def depositar(self,valor):
        if(self.salario + valor > self.saldo ):
            self.saldo +=valor

        else:
            print("caiu no")

    def sacar(self, saque):
        if(self.saldo >=500):
            self.saldo -= saque



conta1 = Conta_bancaria (titular='Tonni', saldo=0)


print (conta1.titular, conta1.saldo)
conta1.depositar(1200)
conta1.sacar(1500)

print(conta1.s
aldo)