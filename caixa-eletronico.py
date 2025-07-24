"""
SISTEMA CAIXA ELETRÔNICO PROFISSIONAL
=====================================
Desenvolvido em Python - Versão 2.0
Autor: Natan Mauricio Santos
Data: 07/2025

Funcionalidades:
✅ Consultar saldo
✅ Realizar depósitos  
✅ Sacar dinheiro
✅ Histórico de transações
✅ Validação de CPF
✅ Sistema de senhas
✅ Relatórios detalhados
"""
"""
Pendências
 - Exibir o nome do usuário logado no menu principal    
    """
def menu():
    #Exibir o menu principal com as escolhas de opções
    print("-"* 40)
    print(f"{" "*13}MENU PRINCIPAL")
    print("-" * 40)

    print("1️⃣  - Consultar Saldo")
    print("2️⃣  - Depósito")
    print("3️⃣  - Saque")
    print("4️⃣  - Histórico de Transações")
    print("5️⃣  - Relatório Detalhado")
    print("6️⃣  - Sair")
    print("-" * 40)
    
def escolha():
    while (opcao != 6):
        menu()
        try:
            opcao = int(input("Digite a opção desejada:"))
            '''
            if (opcao == 1):
                #Consultar saldo
            elif (opcao == 2):
                #Depósito
            elif (opcao == 3):
                #Saque
            elif (opcao == 4):
                #Histório de transições
            elif (opcao == 5):
                #Relatório Detalhado
            elif (opcao == 6):
                #Sair
            else:
                print("❌ Opção inválida! Digite um número de 1 a 6.")
                input("\n Pressione ENTER para continuar...")
            '''
        except KeyboardInterrupt:
            print("\n\n🛑 Sistema interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            input("\n📱 Pressione ENTER para continuar...")
    
    

        

    
#Programa principal

escolha()