#O ano é bissexto quando é divisível por 4, mas não por 100. Contudo, mesmo que ele seja d
#Para saber se um ano é bissexto, devemos verificar se ele se encaixa em um dos casos:
#Caso 1) É um número divisível por 4, mas não é divisível por 100.
#Caso 2) É um número divisível por 4, por 100 e por 400.
from datetime import date
ano = int(input("Qual ano quer analisar? Coloque 0 para analisar o ano atual: "))
verificação = False
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or  ano % 400 == 0:
    verificação = True
if verificação:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} não é BISSEXTO')