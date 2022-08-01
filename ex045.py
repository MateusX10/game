import colorama
from random import randint
from time import sleep

from pygame import QUIT
colorama.init()
print(f'\033[1;34m{" JOGO DO PEDRA, PAPEL E TESOURA ":=^90}\033[m')
opc = ["PEDRA", "PAPEL", "TESOURA"]
computador = opc[randint(0,2)]
print('''SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogador = int(input("Faça sua escolha: "))
try:
    jogador = opc[jogador]
except:
    print("\033[1;31mJOGADA INVÁLIDA!Tente novamente.")
    quit( )
print('\033[32mJO')
sleep(1)
print("KEN")
sleep(1)
print("PÔ!\033[m")
sleep(0.3)
print(f'Jogador joga {jogador}')
sleep(1)
print(f'Computador joga {computador}')
sleep(1)
if jogador == computador:
    print("\033[33mEMPATE!\033[m")
else:
    print(jogador, computador)
    if jogador == "PEDRA" and computador == "PAPEL" or jogador == "PAPEL" and computador == "TESOURA":
        print("\033[1;31mCOMPUTADOR VENCE!")
    elif jogador == "TESOURA" and computador == "PEDRA":
        print("\033[1;31mCOMPUTADOR VENCE!")
    elif jogador == "PEDRA" and computador == "TESOURA" or jogador == "PAPEL" and computador == "PEDRA":
        print("\033[1;32mJogador vence!")
    elif jogador == "TESOURA" and computador == "PAPEL":
        print(f'\033[1;32mJOGADOR VENCE!')