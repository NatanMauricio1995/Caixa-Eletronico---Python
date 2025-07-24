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

def menu():
    #Exibir o menu principal com as escolhas de opções
    print("-"* 40)
    print(f"{" "*13}MENU PRINCIPAL")
    print("-" * 40)
    
    #Imprimir o nome do Usuário

    print("1️⃣  - Consultar Saldo")
    print("2️⃣  - Depositar Dinheiro")
    print("3️⃣  - Sacar Dinheiro")
    print("4️⃣  - Histórico de Transações")
    print("5️⃣  - Relatório Detalhado")
    print("6️⃣  - Sair")
    print("-" * 40)
        
    
#Programa principal

menu()