def calcular_venda_desconto_pagamento():
    print("============================")
    print("=== Isaura Lauton Ateliê ===")
    print("============================")
    # Entrada dos dados do cliente
    nome = input("Digite o nome completo do cliente: ")
    cpf = input("Digite o CPF do cliente (somente números): ")
    
    # Dados da venda
    valor_venda = float(input("Digite o valor da venda: R$ "))

    # Escolha da forma de pagamento
    print("\nEscolha a forma de pagamento:")
    print("1 - Dinheiro (10% de desconto)")
    print("2 - Cartão à vista (5% de desconto)")
    print("3 - Cartão parcelado (sem desconto)")
    print("4 - Pix (10% de desconto)")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        desconto_percentual = 10
        forma_pagamento = "Dinheiro"
        parcelas = 1
    elif opcao == "2":
        desconto_percentual = 5
        forma_pagamento = "Cartão à vista"
        parcelas = 1
    elif opcao == "3":
        desconto_percentual = 0
        forma_pagamento = "Cartão parcelado"
        # Pergunta o número de parcelas para cartão parcelado
        while True:
            try:
                parcelas = int(input("Quantas parcelas? (1 a 12): "))
                if 1 <= parcelas <= 12:
                    break
                else:
                    print("Por favor, informe um número entre 1 e 12.")
            except ValueError:
                print("Por favor, informe um número válido.")
    elif opcao == "4":
        desconto_percentual = 10
        forma_pagamento = "Pix"
        parcelas = 1
    else:
        print("Opção inválida! Nenhum desconto será aplicado.")
        desconto_percentual = 0
        forma_pagamento = "Indefinida"
        parcelas = 1

    desconto = (desconto_percentual / 100) * valor_venda
    valor_final = valor_venda - desconto

    print("\n=== Resumo da Venda ===")
    print(f"Cliente: {nome}")
    print(f"CPF: {cpf}")
    print(f"Forma de pagamento: {forma_pagamento}")
    print(f"Valor original: R$ {valor_venda:.2f}")
    print(f"Desconto aplicado: {desconto_percentual}% (R$ {desconto:.2f})")
    print(f"Valor final a pagar: R$ {valor_final:.2f}")

    if parcelas > 1:
        valor_parcela = valor_final / parcelas
        print(f"Parcelamento: {parcelas}x de R$ {valor_parcela:.2f} (sem juros)")
    else:
        print("Pagamento à vista.")

if __name__ == "__main__":
    calcular_venda_desconto_pagamento()


