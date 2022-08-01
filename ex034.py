salário = float(input("Salário do funcionário: R$"))
if salário <= 1250:
    aumento = salário + (salário * 15 / 100)
else:
    aumento = salário + (salário * 10 / 100)
print(f'Quem tinha um salário de R${salário:.2f}, agora passa a ganhar R${aumento:.2f}')