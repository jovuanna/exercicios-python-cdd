class Contas:

    def __init__(self, num_conta, nome, saldo, tipo_conta, status_conta=False):
        self.num_conta = num_conta
        self.nome = nome
        self.saldo = saldo
        self.tipo_conta = tipo_conta
        self.status_conta = status_conta


    def dados(self):
        print(f"Titular da conta: {self.nome}")
        print(f"Número da conta: {self.num_conta}")
        print(f"Tipo de conta: {self.tipo_conta}")


    def desativar(self):
        if self.status_conta == True:
            print("Status da conta: ativa.")
            while True:
                opcao = input("Deseja desativar a conta? ")
                if opcao == "Sim" or opcao == "sim" or opcao == "S" or opcao == "s" or opcao == "SIM" and self.saldo > 0:
                    self.status_conta = False
                    self.saldo = 0
                    print(f"Seu saldo agora é R${self.saldo} Sua conta está desativada.")
                    print("Fim do programa!")
                    break
                else:
                    break


    def ativar(self):
        print("Status da conta: desativada.")
        self.saldo = 0
        while self.status_conta == False:
            opcao = input("Deseja ativar a conta? ")
            if opcao == "Sim" or opcao == "sim" or opcao == "S" or opcao == "s" or opcao == "SIM":
                self.status_conta = True
                print(f"Sua conta está ativada! Seja bem-vinda(o) {self.nome}!")
                break
            else:
                print("Fim do programa!")
                break


    def depositar(self):
        while self.status_conta == True:
            opcao = input("Deseja fazer algum depósito? ")
            if opcao == "Sim" or opcao == "sim" or opcao == "S" or opcao == "s" or opcao == "SIM":
                deposito = float(input("Quanto deseja depositar na sua conta? "))
                self.saldo += deposito
                print(f"Depósito efetuado.")
                break
            else:
                break



    def sacar(self):
        while self.status_conta == True and self.saldo > 0:
            opcao = input("Deseja sacar dinheiro? ")
            if opcao == "Sim" or opcao == "sim" or opcao == "S" or opcao == "s" or opcao == "SIM":
                saque = float(input("Quanto deseja sacar da sua conta? "))
                self.saldo -= saque
                print(f"Seu saldo agora é {self.saldo}.")
                break
            else:
                break



    def saldo_conta(self):
        while self.status_conta == True and self.saldo > 0:
            opcao = input("Deseja verificar o saldo? ")
            if opcao == "Sim" or opcao == "sim" or opcao == "S" or opcao == "s" or opcao == "SIM":
                print(f"Saldo: R$", {self.saldo})
                print("Fim do programa!")
                break
            else:
                print("Fim do programa!")
                break
def introducao():
    print('-'*20)
    print("       BANCO")
    print('-'*20)
    print("Informações:")
    print('=-'*10)

introducao()
conta1 = Contas(12345, "Giovanna Giselli", 0, "Corrente", status_conta=True)
conta1.dados()
conta1.desativar()
conta1.depositar()
conta1.sacar()
conta1.saldo_conta()

introducao()
conta2 = Contas(67894, "Isadora dos Santos", 4567.54, "Poupança", status_conta=True)
conta2.dados()
conta2.desativar()
conta2.depositar()
conta2.sacar()
conta2.saldo_conta()
