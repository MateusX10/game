import colorama
colorama.init()
valor_casa = float(input("Valor da casa: R$"))
salário = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento: "))
prestação_mensal = valor_casa / (anos * 12)
print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos a prestação será de R${prestação_mensal:.2f}')
if prestação_mensal > (salário * 30 / 100):
    print('\033[31EMPRÉSTIMO NEGADO!')
else:
    print("\033[32mEMPRÉSTIMO APROVADO")