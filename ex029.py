import colorama
colorama.init()
velocidade_carro = float(input("Velocidade do carro (em Km): "))
multa = 7 * (velocidade_carro - 80)
if velocidade_carro > 80:
    print(f'''\033[31mVocê foi multado pois excedeu o limite permitido de 80Km/h!
Terá de pagar uma multa de R${multa:.2f}!\n\033[33m Tenha um bom dia!Dirija com segurança!\033[m''')
else:
    print("\033[33mTenha um bom dia!Dirija com segurança!\033[m")