# Caixa Eletrônico - Python

Sistema simples de caixa eletrônico desenvolvido durante meus estudos de Python na FAETERJ.

## Sobre o Projeto

Este projeto foi desenvolvido como parte dos meus estudos em **Tecnologia da Informação**, focando em:
- Lógica de programação
- Estruturas condicionais e de repetição
- Validação de entrada do usuário
- Organização de código em funções

## Funcionalidades

- **Consultar saldo** - Visualiza o saldo atual da conta
- **Depositar dinheiro** - Adiciona valores ao saldo
- **Sacar dinheiro** - Remove valores do saldo (com validação)
- **Validação de entradas** - Impede valores inválidos
- **Interface amigável** - Menu intuitivo e organizado
- **Tratamento de erros** - Previne crashes por entrada incorreta

## Tecnologias Utilizadas

- **Python 3.x**
- Estruturas condicionais (`if`, `elif`, `else`)
- Loops de repetição (`while`)
- Funções personalizadas
- Tratamento de exceções (`try/except`)
- Formatação de strings (f-strings)

## Como Executar

1. **Pré-requisitos:**
   - Python 3.x instalado no sistema

2. **Executar o programa:**
   ```bash
   python caixa_eletronico.py
   ```

3. **Uso:**
   - Digite seu nome quando solicitado
   - Escolha as opções do menu (1-4)
   - Siga as instruções na tela

## Conceitos de Programação Aplicados

### **Estruturas de Controle:**
```python
# Loop principal do programa
while escolha != 4:
    # Código do menu
```

### **Validação de Entrada:**
```python
# Valida se o valor é positivo
while valor_deposito < 0:
    valor_deposito = float(input("Digite o valor: "))
```

### **Tratamento de Exceções:**
```python
try:
    escolha = int(input("Escolha: "))
except ValueError:
    print("Digite apenas números!")
```

## Demonstração

```
========================================
     CAIXA ELETRÔNICO     
========================================
Usuario: Natan Mauricio
----------------------------------------

MENU DE OPCOES:
  1 - Verificar saldo
  2 - Depositar dinheiro
  3 - Sacar dinheiro
  4 - Sair
----------------------------------------
Escolha sua opcao (1-4):
```

## Aprendizados

Este projeto me permitiu praticar:

- **Lógica de programação básica**
- **Estruturação de código** em funções
- **Validação robusta** de entrada do usuário
- **Interface de usuário** em terminal
- **Tratamento de erros** para evitar crashes
- **Documentação** de código com comentários

## Próximas Melhorias

- Adicionar sistema de login com CPF
- Implementar histórico de transações
- Criar limite diário de saque
- Adicionar diferentes tipos de conta
- Salvar dados em arquivo

## Autor

**Natan Mauricio Santos**
- Tecnólogo em Tecnologia da Informação - FAETERJ
- Petrópolis - RJ
- natanmauriciosantos@hotmail.com
- [LinkedIn](https://linkedin.com/in/seu-perfil)

## Licença

Este projeto está sob licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**"Cada linha de código é um passo na minha jornada de aprendizado!"**
