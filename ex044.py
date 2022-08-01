import colorama
colorama.init()
print(f'\033[1;34m{" LOJAS IRMÃO DO ZINHO ":=^90}\033[m')
preço = float(input("Preço das compras: R$"))
total = preço
print('''FORMAS DE PAGAMENTO
[ 1 ] - à vista dinheiro/cheque
[ 2 ] - à vista cartão
[ 3 ] - 2x no cartão
[ 4 ] - 3x ou mais no cartão
''')
choice = int(input("Qual é a opção? "))
if choice == 1:
    total = preço - (preço * 10 / 100)
elif choice == 2:
    total = preço - (preço * 5 / 100)
elif choice == 3:
    parcela = preço / 2
    print(f'Sua compra será parcelado em 2x de R${parcela:.2f}')
elif choice == 4:
    totparcelas = int(input("Quantas parcelas? "))
    total = (preço +  preço * 20 / 100)
    parcela = total / totparcelas
    print(f'''Sua compra será parcelada em {totparcelas}x de R${parcela:.2f} COM JUROS''')
else:
    total = 0
    print(f'\033[31m"{choice}" é uma opção inválida!')
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final')
if choice > 4:
    print("\033[1;31mPor favor, reinicia sua compra!")

