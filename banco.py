class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.extrato = []
        self.saques_diarios = 0
        self.LIMITE_SAQUES_DIARIOS = 3
        self.LIMITE_SAQUE = 500

    def sacar(self, valor):
        if self.saques_diarios >= self.LIMITE_SAQUES_DIARIOS:
            return "Limite de saques diários atingido."
        
        if valor > self.LIMITE_SAQUE:
            return "Valor do saque excede o limite de R$500."
        
        if valor > self.saldo:
            return "Saldo insuficiente."
        
        self.saldo -= valor
        self.extrato.append(f"Saque: R${valor:.2f}")
        self.saques_diarios += 1
        return f"Saque de R${valor:.2f} realizado com sucesso."

    def depositar(self, valor):
        if valor <= 0:
            return "Valor do depósito deve ser positivo."
        
        self.saldo += valor
        self.extrato.append(f"Depósito: R${valor:.2f}")
        return f"Depósito de R${valor:.2f} realizado com sucesso."

    def visualizar_extrato(self):
        extrato = "\n".join(self.extrato) if self.extrato else "Nenhuma transação realizada."
        return f"Extrato:\n{extrato}\nSaldo Atual: R${self.saldo:.2f}"

def main():
    conta = ContaBancaria(1000)
    
    while True:
        print("\nEscolha a operação:")
        print("1. Sacar")
        print("2. Depositar")
        print("3. Visualizar Extrato")
        print("4. Sair")
        
        escolha = input("Digite o número da operação desejada: ")
        
        if escolha == "1":
            valor = float(input("Digite o valor a ser sacado: R$"))
            resultado = conta.sacar(valor)
            print(resultado)
            print(conta.visualizar_extrato())
        elif escolha == "2":
            valor = float(input("Digite o valor a ser depositado: R$"))
            resultado = conta.depositar(valor)
            print(resultado)
            print(conta.visualizar_extrato())
        elif escolha == "3":
            print(conta.visualizar_extrato())
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
