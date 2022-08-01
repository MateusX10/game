from time import sleep
num = int(input("Informe um número: "))
num = str(num)
unidade = dezena = centena = milhar = 0
if len(num) >= 4:
    milhar = num[-4]
if len(num) >= 3:
    centena = num[-3]
if len(num) >= 2:
    dezena = num[-2]
if len(num) >= 1:
    unidade =  num[-1]
print(f'Analisando o número {num}...')
sleep(1.3)
print(f'Unidade: {unidade} \nDezena: {dezena} \nCentena: {centena} \nMilhar: {milhar}')