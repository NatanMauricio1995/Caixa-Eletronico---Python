"""
SISTEMA CAIXA ELETRÔNICO
========================
Desenvolvido por: Natan Maurício Santos
Curso: Tecnologia da Informação - FAETERJ
Data: 2025

Funcionalidades:
- Consultar saldo
- Depositar dinheiro  
- Sacar dinheiro
- Validação de valores
- Interface amigável
"""

# Dados iniciais
saldo = 1000.00
nome_usuario = ""

def exibir_cabecalho():
    """Exibe o cabeçalho do sistema"""
    print("=" * 40)
    print("            CAIXA ELETRÔNICO     ")
    print("=" * 40)
    if nome_usuario:
        print(f"Usuario: {nome_usuario}")
        print("-" * 40)

def exibir_menu():
    """Exibe o menu de opções"""
    print("\nMENU DE OPCOES:")
    print("  1 - Verificar saldo")
    print("  2 - Depositar dinheiro")
    print("  3 - Sacar dinheiro")
    print("  4 - Sair")
    print("-" * 40)

def verificar_saldo():
    """Exibe o saldo atual"""
    print("\n" + "=" * 50)
    print("CONSULTA DE SALDO")
    print("=" * 50)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=" * 50)

def depositar_dinheiro():
    """Realiza depósito de dinheiro"""
    global saldo
    
    print("\n" + "=" * 50)
    print("DEPOSITO")
    print("=" * 50)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("-" * 50)
    
    # Validação do valor de depósito
    valor_deposito = -1
    while valor_deposito < 0:
        try:
            valor_deposito = float(input("Digite o valor para deposito: R$ "))
            if valor_deposito < 0:
                print("Valor invalido! Digite um valor positivo.")
        except ValueError:
            print("Digite apenas numeros!")
            valor_deposito = -1
    
    # Confirma a operação
    if valor_deposito > 0:
        saldo = saldo + valor_deposito
        print(f"\nDeposito realizado com sucesso!")
        print(f"Valor depositado: R$ {valor_deposito:.2f}")
        print(f"Novo saldo: R$ {saldo:.2f}")
    else:
        print("Operacao cancelada.")
    
    print("=" * 50)

def sacar_dinheiro():
    """Realiza saque de dinheiro"""
    global saldo
    
    print("\n" + "=" * 50)
    print("SAQUE")
    print("=" * 50)
    print(f"Saldo disponivel: R$ {saldo:.2f}")
    print("-" * 50)
    
    # Validação do valor de saque
    valor_saque = -1
    while (valor_saque < 0) or (valor_saque > saldo):
        try:
            valor_saque = float(input("Digite o valor para saque: R$ "))
            if valor_saque < 0:
                print("Valor invalido! Digite um valor positivo.")
            elif valor_saque > saldo:
                print(f"Saldo insuficiente! Disponivel: R$ {saldo:.2f}")
        except ValueError:
            print("Digite apenas numeros!")
            valor_saque = -1
    
    # Confirma a operação
    if valor_saque > 0:
        saldo = saldo - valor_saque
        print(f"\nSaque realizado com sucesso!")
        print(f"Valor sacado: R$ {valor_saque:.2f}")
        print(f"Saldo restante: R$ {saldo:.2f}")
    else:
        print("Operacao cancelada.")
    
    print("=" * 50)

def main():
    """Função principal do programa"""
    global nome_usuario
    
    # Boas-vindas
    print("Iniciando Sistema Caixa Eletronico...")
    print("\nBem-vindo ao Caixa Eletronico!")
    nome_usuario = input("Digite seu nome: ").strip()
    
    if not nome_usuario:
        nome_usuario = "Usuario"
    
    print(f"\nOlá, {nome_usuario}! Vamos comecar?")
    input("Pressione ENTER para continuar...")
    
    # Loop principal
    escolha = 0
    
    while escolha != 4:
        # Limpa a tela (simulado com quebras de linha)
        print("\n" * 3)
        
        # Exibe interface
        exibir_cabecalho()
        exibir_menu()
        
        # Captura opção do usuário
        escolha = 0
        while (escolha < 1) or (escolha > 4):
            try:
                escolha = int(input("Escolha sua opcao (1-4): "))
                if (escolha < 1) or (escolha > 4):
                    print("Opcao invalida! Digite um numero de 1 a 4.")
            except ValueError:
                print("Digite apenas numeros!")
                escolha = 0
        
        # Executa a opção escolhida
        if escolha == 1:
            verificar_saldo()
            
        elif escolha == 2:
            depositar_dinheiro()
            
        elif escolha == 3:
            sacar_dinheiro()
            
        elif escolha == 4:
            print("\n" + "=" * 50)
            print("OBRIGADO POR USAR NOSSOS SERVICOS!")
            print(f"Ate logo, {nome_usuario}!")
            print("Sessao encerrada com seguranca.")
            print("=" * 50)
            break
        
        # Pausa antes de voltar ao menu
        if escolha != 4:
            input("\nPressione ENTER para voltar ao menu...")

# Execução do programa
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSistema encerrado pelo usuario.")
        print("Ate logo!")
    except Exception as e:
        print(f"\nErro inesperado: {e}")
        print("Entre em contato com o suporte se o problema persistir.")