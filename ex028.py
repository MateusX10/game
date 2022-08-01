from random import randint
from time import sleep
import colorama
colorama.init()
def line():
    print("-=" * 45)
computador = randint(0,5)
jogador = 9999
line()
print('\033[32mVou pensar em um número entre 0 e 5.Tente adivinhar!\033[m')
line()
while jogador != computador:
    jogador = int(input("Em que número eu pensei? "))
    if jogador == computador:
        print(f'\033[32mVocê me venceu!Eu pensei no número {computador}\033[m')
    else:
        if jogador > computador:
            print('\033[33mMENOS...\033[m')
        else:
            print('\033[33mMAIS\033[m')
