import colorama
colorama.init()
peso = float(input("Peso(Kg): "))
alt = float(input("Altura(m): "))
IMC = peso / (alt ** 2)
print(f'Seu IMC é de {IMC:.1f}')
if IMC < 18.5:
    print('\033[31mCUIDADO!Você está \033[1;31mABAIXO DO PESO!\033[m')
elif IMC < 25:
    print("\033[1;32mPESO IDEAL!Continue cuidando de sua saúde!\033[m")
elif IMC < 30:
    print("\033[1;31mATENÇÃO!Voce está com SOBREPESO!")
elif IMC < 40:
    print("\033[1;31mCUIDADO!Você está com OBESIDADE!")
else:
    print("\033[1;31mPERIGO!Você está com OBESIDADE MÓRBIDA!")