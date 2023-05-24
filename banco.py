class Contas:

    def __init__(self, num_conta, nome, saldo, tipo_conta, status_conta=False):
        self.num_conta = num_conta
        self.nome = nome
        self.saldo = saldo
        self.tipo_conta = tipo_conta
        self.status_conta = status_conta


    def status(self):
        if self.status_conta == False:
            print("Status da conta: Desativada")
        else:
            print("Status da conta: Ativa")

    def saldo_conta(self):
        while self.status_conta == True:
            opcao = input("Deseja verificar o saldo? ")
            if opcao == "Sim" or opcao == "sim" or opcao == "S" or opcao == "s" or opcao == "SIM":
                print(f"Saldo: ", {self.saldo})
                break
            else:
                print("Saldo: ****")
                break


    def depositar(self):
        while self.status_conta == True:
            opcao = input("Deseja fazer algum depósito? ")
            if opcao == "Sim" or opcao == "sim" or opcao == "S" or opcao == "s" or opcao == "SIM":
                deposito = float(input("Quanto deseja depositar na sua conta? "))
                self.saldo += deposito
                print(f"Seu saldo agora é {self.saldo}.")
            break


    def sacar(self):
        while self.status_conta == True:
            opcao = input("Deseja sacar dinheiro? ")
            if opcao == "Sim" or opcao == "sim" or opcao == "S" or opcao == "s" or opcao == "SIM":
                saque = float(input("Quanto deseja sacar da sua conta? "))
                self.saldo -= saque
                print(f"Seu saldo agora é {self.saldo}.")
            break


    def desativar(self):
        if self.status_conta == True:
            print("Sua conta está ativa.")
            while True:
                opcao = input("Deseja desativar a conta? ")
                if opcao == "Sim" or opcao == "sim" or opcao == "S" or opcao == "s" or opcao == "SIM":
                    self.status_conta = False
                    if self.saldo > 0:
                        self.saldo = 0
                        print(f"Seu saldo agora é {self.saldo}. Sua conta está desativada.")
                break


    def ativar(self):
        print("Sua conta está desativada.")
        while self.status_conta == False:
            opcao = input("Deseja ativar a conta? ")
            if opcao == "Sim" or opcao == "sim" or opcao == "S" or opcao == "s" or opcao == "SIM":
                self.status_conta = True
                print(f"Sua conta está ativada! Seja bem-vinda(o) {self.nome}!")
                break



conta1 = Contas(12345, "Giovanna Giselli", 0, "Corrente", status_conta=False)
print(f"Titular da conta: {conta1.nome}")
conta1.desativar()
conta1.ativar()
conta1.saldo_conta()
conta1.depositar()
conta1.sacar()
