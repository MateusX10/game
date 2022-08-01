from time import sleep
from math import trunc
import colorama
colorama.init()
def ponto():
    for c in range(1,4):
        sleep(1.1)
        print(".", end='')
    sleep(2)
    print()
def wait():
    sleep(1.5)
def fix():
    global HP_jogador
    HP_jogador *= -1
dano = 1000
venceu = perdeu = False
HP_monstro = 100
HP_jogador = 100
cont = 0
gold = trunc(HP_monstro / 2)
xp = trunc(HP_monstro / 5) + trunc((cont / 5))
for c in range(0, 10):
    cont += 1
    while dano > c:
        print(f'HP: {HP_jogador}')
        dano = int(input(f"Quanto de dano quer dar nessa rodada(0 - {c})? "))
        if dano > c:
            print(f'\033[1;31mVocê só pode dar 0 - {c} dano nessa rodada!\033[m')
        if dano <= c != 0:
            HP_monstro -= dano
    sleep(0.8)
    print("\033[1;34mPOWWWWWW!!!\033[m")
    wait()
    print(f'\033[1mVida do monstro: {trunc(HP_monstro)}')
    if dano == 0:
        sleep(1)
        print("Mas nada aconteceu...")
    if HP_monstro <= 0:
        venceu = True
        print("\033[1;31m* GRRRRRRRRRRRR!!!!")
        wait()
        print("(MONSTRO FALANDO)")
        wait()
        print("* VOCÊ ME VENCEU", end='') 
        ponto()
        print("* DROGAAAAAAAAAAA!!!!")
        sleep(1.5)
        print("(MONSTRO MORRE!)")
        wait()
        break
    else:
        dano_monstro = trunc(HP_monstro / 3) + dano + 50
        if dano == 0:
            print("\033[1m* Monstro parece admirado com sua força!")
            wait()
            print("* Na verdade ele te acha um verdadeiro fracote :)")
        HP_jogador -= dano_monstro
        if dano_monstro > dano_monstro:
            fix()
        print("\033[1;31mPOWWWWWWWWW!\033[m")
        wait()
        print("* Monstro desfere um ataque feroz!")
        if HP_jogador <= 0:
            perdeu = True
            print("\033[1;31m* (Você sente um frio no seu corpo)", end='')
            ponto()
            print("\033[1m* Monstro gargalha de seu semblante de cadáver.")
            wait()
            break
    wait()
    if cont == 4:
        print("\033[1m* Monstro está ficando entediado...")
        wait()
        print("* (Você não dá a mínima)")
        wait()
    elif cont > 4:
        print("* Monstro está ficando muito cansado...")
        wait()
        print('* (Você continua não se importando.)')
        wait()
    if cont % 2 == 0:
        print("* (Você espera pacientemente...)")
    else:
        print("* (Você encara monstro)")
    wait()
    dano = 1000
if venceu:
    print(f"\033[1;32mVOCÊ VENCEU!")
else:
    print(f'\033[1;31mVOCÊ PERDEU!')
    xp = gold = 0
print(f'GANHOU {xp} XP e {gold} ouros.')