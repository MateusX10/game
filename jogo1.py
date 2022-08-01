import pygame
from time import sleep
from random import randint

pygame.init() #inicia o pygame

def restart():
    global x,y,x2,y2,x3,y3, x4, y4, x5, y5, x6, y6,x7, y7, preso, cont, tempo_seg, texto
    x4 = 480
    x5 = 712
    x6 = 590
    y5 = y4 = y6 = 666
    x7 = 1020
    y7 = 620
    preso = cont = tempo_seg = 0
    if not kill_car1:
        x = 600
        y = 550
        janela.blit(carro, (x,y))
    if not kill_car2:
        x2 = y2 = 550
        janela.blit(carro2, (x2,y2))
    if not kill_car3:
        x3 = 650
        y3 = 530
        janela.blit(carro3, (x3,y3))
    texto = font.render("Tempo: "+str(tempo_seg), True, (255, 255, 255), (0,0,0))
    colisão(carro, velocidadein, correrin, True)
    colisão(carro2, velocidadein2, correrin2, True)
    colisão(carro3, velocidadein3, correrin3, True)
    pygame.mixer.music.load("naruto.mp3")
    pygame.mixer.music.play()
    pygame.display.update()
def espera():
    for event in pygame.event.get(): #tela não fecha
        if event.type == pygame.QUIT:
            global janela_aberta
            janela_aberta = False
        if comandos[pygame.K_r]:
            restart()
        if comandos[pygame.K_q]:
            quit()
def music():
    pygame.mixer.music.load("sirene.mp3")
    pygame.mixer.music.play()

def naruto():
    pygame.mixer.music.load("naruto.mp3")
    pygame.mixer.music.play()

def sirene(automovel, horiz=450, vert=550):
    global preso, x3, y3
    preso += 1
    music()
    if horiz >= 810:
        janela.blit(carro3, (horiz-63, vert))
    else:
        janela.blit(policia, (horiz+63, vert))
    pygame.display.update()
    sleep(7)
    if preso >= 3:
        death()
    if automovel == carro:
        global x, y
        y = 550
        x = 450
        janela.blit(automovel, (x,y))
    else:
        global x2, y2
        x2 = y2 = 550
        janela.blit(automovel, (x, y))
    naruto()

def life(preso):
    x = 30
    x2 = 60
    x3 = 90
    y = y2 = y3 = 50
    janela.blit(vida, (x,y))
    if preso != 2:
        janela.blit(vida, (x2,y2))
    if preso == 0:
        janela.blit(vida, (x3,y3))
    pygame.display.update()
def colisão(car,vel0, correr0, passou=False):
    global velocidade, velocidade2, velocidade3, correr, correr2, correr3, carros
    if passou:
        '''for pos, v in enumerate(carros):
            if car == carros[pos]:
                velocidades[pos] = vel0
                corrers[pos] = correr0'''
        if car == carro:
            velocidade = vel0
            correr = correr0
        if car == carro2:
            velocidade2 = vel0
            correr2 = correr0
        if car == carro3:
            velocidade3 = vel0
            correr3 = correr0
    else:
        if car == carro:    
            velocidade = 5
            correr = 0
        if car == carro2:
            velocidade2 = 5
            correr2 = 0
        if car == carro3:
            velocidade3 = 5
            correr3 = 0
def death():
    janela.blit(gangue,(0,0))
    pygame.display.update()
    sleep(9)
    quit()

def atualizar():
    pygame.display.update()

def coordenadas_outros():
    global y4, y5, y6
    y4 -= velocidade_outros +2 #ambulância
    y5 -= velocidade_outros +4 #carro amarelo
    y6 -= velocidade_outros + 3 #carro cinza

timer = tempo_seg = cont = cont2 = cont3 = cont4 = cont5 = cont6 = preso = vida = ultimo = xult = yult = ciclo = alvox1 = alvoy1 = distanciax1 = distanciay1 = configpasso_x = configpasso_y = 0
x = 591 #carro vermelho
y = 550 #carro vermelho
x2 = y2 = 550 #carro amarelo
x3 = 650 #policia
y3 = 540 #policia
x4 = 480 #ambulância
y4 = y5 = y6 =  800 #ambulância, carro amarelo, carro cinza
x5 = 712 #carro amarelo
x6 = 590 #carro cinza
x7 = 1020    #650
y7 = 620   #20
x8 = xult
y8 = 700
velocidade = velocidadein = velocidade2 = velocidadein2 = velocidade3 = velocidadein3 =  10 #quantos pixels a nossa figura vai andar quando for pressionada --> quantos pixels pra cima, baixo...
velocidade_outros = 6
correr = correrin = 48
correr2 = correrin2 = 25
correr3 = correrin3 = 8 
kill_car1 = kill_car2 = kill_car3 = kill_bola = morte = marca_alvo = limitecima_x1 = limitebaixo_x1 =  limitecima_y1 = limitebaixo_y1 =  False
musica = ""
naruto()

fundo = pygame.image.load('ESTRADA.png')
carro = pygame.image.load("carro10.png")
carro2 = pygame.image.load("carro4.png")
carro3 = pygame.image.load("policia10.png")
policia = pygame.image.load("policia10.png")
ambu = pygame.image.load("ambulancia.png")
carro4 = pygame.image.load("carroamarelo.png")
carro5 = pygame.image.load("carrocinza.png")
bob = pygame.image.load("espiao.png")
eu = pygame.image.load('fotoespreita.png')
zinho = pygame.image.load("fotolider.png")
vida = pygame.image.load("heart.png")
gangue = pygame.image.load("gangue.png")
torre = pygame.image.load("torreright.png")

carros = [carro, carro2, carro3]
velocidades = [velocidade, velocidade2, velocidade3]
corrers = [correr, correr2, correr3]

font = pygame.font.SysFont("arial black", 30) #criou um objeto fonte, usou o método fonte do pygame.SysFont: busca as fontes do sistema.Fonte arial black, tamanho 30
texto = font.render("Tempo: "+str(tempo_seg), True, (255, 255, 255), (0,0,0)) #método render = recebe uma string no primeiro parâmetro, True: máscara que é criada (true ou false não muda nada) ---> é ele que coloca o fundo do tempo (o retangulo preto)
pos_texto = texto.get_rect() #define a posição do texto com o get rect (retangulo que fica atras do texto)
pos_texto.center = (75,20) #pos do texto na coordenada 65 no x e 50 no y

janela = pygame.display.set_mode((1180, 666 ), pygame.FULLSCREEN) #define o tamanho da janela1000 666
pygame.display.set_caption("carros ambulantes")#"título" da janela do jogo
janela_aberta = True

while janela_aberta:
    comandos = pygame.key.get_pressed()
    espera()
    coordenadas_outros()

    if kill_car1 and kill_car2 and kill_car3:
        if ciclo == 0:
            morte = True
            music()
            ciclo = 1
        elif ciclo == 3:
            death()

    if not kill_car1:
        if comandos[pygame.K_u] or comandos[pygame.K_UP]:              #jogador1- mover para cima
            y-= velocidade
            if comandos[pygame.K_g]:
                y-= correr
            if y <= -100:
                y =  725
        
        if comandos[pygame.K_j] or comandos[pygame.K_DOWN]:
            y+= velocidade
            if comandos[pygame.K_g]:           #jogador1- mover para baixo
                y+= correr
            if y >= 725:
                y = -105

        if comandos[pygame.K_h] or comandos[pygame.K_LEFT]:
            x-= velocidade                      #jogador1- mover para esquerda
            if comandos[pygame.K_g]:
                x-= correr
            if  365 >= x:
                sirene(carro, x, y)

        if comandos[pygame.K_k] or comandos[pygame.K_RIGHT]:
            x+= velocidade                      #jogador1- mover para direita
            if comandos[pygame.K_g]:
                x+= correr
            if x >= 870:
                sirene(carro, x, y)

    if not kill_car2:

        if comandos[pygame.K_w]:
            y2-= velocidade2                   #jogador2- mover para cima
            if comandos[pygame.K_f]:
                y2-= correr2
            if y2 <= -100:
                y2 = 720


        if comandos[pygame.K_s]:
            y2+= velocidade2
            if comandos[pygame.K_f]:            #jogador2- mover para baixo
                y2+= correr2
            if y2 >= 725:
                y2 = -105

        if comandos[pygame.K_a]:        
            x2-= velocidade2                    #jogador2- mover para esquerda
            if comandos[pygame.K_f]:
                x2-= correr2
            if x2 <= 350:
                sirene(carro2,x2,y2)

        if comandos[pygame.K_d]:
            x2+= velocidade2                     #jogador2- mover para direita
            if comandos[pygame.K_f]:
                x2+= correr2
            if x2 >= 870:
                sirene(carro2, x2, y2)

    if not kill_car3:

        if comandos[pygame.K_i]:
            y3-= velocidade3
            if comandos[pygame.K_p]:
                y3-=correr3
            if y3 <= -120:
                y3 = 725

        if comandos[pygame.K_o]:
            y3+= velocidade3
            if comandos[pygame.K_p]:
                y3+=correr3
            if y3 >= 725:
                y3 = -120
        
        if comandos[pygame.K_n]:
            x3 -= velocidade3
            if comandos[pygame.K_p]:
                x3 -= correr3
            if x3 <= -55:
                x3 = 1170
        
        if comandos[pygame.K_m]:
            x3 += velocidade3
            if comandos[pygame.K_p]:
                x3 += correr3
            if x3 >= 1180:
                x3 = -48 
    '''if comandos[pygame.K_e]:  # opção de "cancelar" os efeitos da colisão dos carros (opção reservada para manuntenção)
        colisão(carro, velocidadein, correrin, True)
        colisão(carro2, velocidadein2, correrin2, True)
        colisão(carro3, velocidadein3, correrin3, True)'''

    if cont+5 == tempo_seg:
        colisão(carro, velocidadein, correrin, True)
    
    if cont2+5 == tempo_seg:
        colisão(carro2, velocidadein2, correrin2, True)

    if cont3+5 == tempo_seg:
        colisão(carro3, velocidadein3, correrin3, True)

    if tempo_seg > 2:

        #detecta colisão com a ambulância
        if x4+60 > x+50 > x4 and y4+128 > y+110 > y4 or x4-60 < x-50 < x4+5 and y4-128 < y-110 < y4+20:
            cont = tempo_seg
            colisão(carro, velocidadein, correrin)

        if x4+60 > x2+55 > x4 and y4+128 > y2+110 > y4 or x4-60 < x2-55 < x4 and y4-128 < y2-113 < y4+15:
            cont2 = tempo_seg
            colisão(carro2, velocidadein2, correrin2)

        if x4+60 > x3+58 > x4 and y4+128 > y3+124 > y4 or x4-60 < x3-58 < x4 and y4-128 < y3-124 < y4:
            cont3 = tempo_seg 
            colisão(carro3, velocidadein3, correrin3)
        #amarelo/cinza: 55X112, policia: 58x124, preto: 55X113, vermelho: 50X110
        #detecta colisão com o carro amarelo
        if x5+55 > x+50 > x5 and y5+112 > y+110 > y5 or x5-55 < x-50 < x5 and y5-112 < y-110 < y5:
            cont = tempo_seg
            colisão(carro, velocidadein, correrin)

        if x5+55 > x2+50 > x5 and y5+112 > y2+113 > y5 or x5-55 < x2-50 < x5 and y5-112 < y2-113 < y5:
            cont2 = tempo_seg
            colisão(carro2, velocidadein2, correrin2)

        if x5+55 > x3+50 > x5 and y5+112 > y3+111 > y5 or x5-55 < x3-50 < x5 and y5-112 < y3-111 < y5:
            cont3 = tempo_seg
            colisão(carro3, velocidadein3, correrin3)

        #detecta colisão com o carro cinza
        if x6+55 > x+50 > x6 and y6+112 > y+110 > y6 or x6-55 < x-50 < x6 and y6-112 < y-110 < y6:
            cont = tempo_seg
            colisão(carro, velocidadein, correrin)

        if x6+55 > x2+50 > x6 and y6+112 > y2+113 > y6 or x6-55 < x2-50 < x6 and y6-112 < y2-113 < y6:
            cont2 = tempo_seg
            colisão(carro2, velocidadein2, correrin2)

        if x6+55 > x3+50 > x6 and y6+112 > y3+111 > y6 or x6-55 < x3-50 < x6 and y6-112 < y3-111 < y6:
            cont3 = tempo_seg
            colisão(carro3, velocidadein3, correrin3)
    
    if x < x7-9 < x+50 and 500 < y < 631 and not kill_car1: #colisão carro1 com a bala
        x -= 60
        kill_car1 = True
        if kill_car2 and kill_car3:
            ultimo = carro
            xult = x
            yult = y

    if x2 < x7-9 < x2+55 and 500 < y2 < 631 and not kill_car2: #colisão carro 2 com a bala
        x2 -= 60
        kill_car2 = True
        if kill_car1 and kill_car3:
            ultimo = carro2
            xult = x2
            yult = y2
    if x3 < x7-9 < x3+58 and 500 < y3 < 631 and not kill_car3: #colisão carro 3 com a bala
        x3 -= 60
        kill_car3 = True
        if kill_car1 and kill_car2:
            ultimo = carro3
            xult = x3
            yult = y3

    if y4 <= -100:
        y4 = randint(666, 2000) #define em que posição(y) os carros aparecerão ao passar do fim da tela
    if y5 <= -100:
        y5 = randint(666, 2000)
    if y6 <= -100:
        y6 = randint(666, 2000)
    if y7 >= 725:
        y7 = -120

    if kill_car1:
        carro = pygame.image.load("sangue.png")
        eu = pygame.image.load("transparente.png")

    if kill_car2:
        carro2 = pygame.image.load("sangue.png")
        zinho = pygame.image.load("transparente.png")

    if kill_car3:
        carro3 = pygame.image.load("sangue.png")
        bob = pygame.image.load("transparente.png")

    if timer < 10:
        timer+=1
    else:
        if tempo_seg == 55:
            naruto()
        tempo_seg += 1
        timer = 0
        texto = font.render("Tempo: "+str(tempo_seg), True, (255,255,255), (0,0,0))

    coordenadas_outros()
    if not marca_alvo:
        alvox1 = x
        alvoy1 = y
        marca_alvo = True
        distanciay1 = y7 - alvoy1
        distanciax1 = x7 - alvox1
        
        if distanciay1 < 0:
            distanciay1 = distanciay1 * -1
        configpasso_y = distanciay1 / 8
        configpasso_x = distanciax1 / 8
    
    if y7 > alvoy1 and cont6 < configpasso_y :
        y7 -= 8
        cont6 += 1
    x7 -= 8

    if x7 < -55:
        if not kill_bola:
            cont4 = tempo_seg
            kill_bola = True
        if cont4+5 == tempo_seg:
            x7 = 1010
            y7 = 620
            kill_bola = marca_alvo = False
    
    if morte and ciclo != 3:
        y8 -= velocidade_outros - 6
        if y8 <= yult:
            y8 = yult
            ciclo = 3
            sleep(2)
    
    janela.blit(fundo,(0,0))
    janela.blit(carro, (x,y))
    janela.blit(carro2, (x2+2,y2))
    janela.blit(carro3, (x3, y3))
    janela.blit(bob, (x3+7, y3-67))
    janela.blit(eu, (x+5, y-65))
    janela.blit(zinho, (x2+11, y2-61))
    janela.blit(ambu, (x4, y4))
    janela.blit(carro4, (x5, y5))
    janela.blit(carro5, (x6,y6))
    janela.blit(policia, (xult+80, y8))
    janela.blit(torre, (600, 478))
    life(preso)
    janela.blit(texto, (pos_texto))
    pygame.draw.circle(janela, (255, 0, 0), (x7, y7), 10)
#parâmetro 1: onde esse circulo vai aparecer; parâmetro 2: RGB ; parâmetro 3: pixels (posição do circulo); ultimo parâmetro: raio
    pygame.display.update()
pygame.quit()
