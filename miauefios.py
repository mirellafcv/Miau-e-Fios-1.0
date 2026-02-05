#pgzero

import random
HEIGHT = 400
WIDTH = 600
TITLE = "Miau e Fios"
FPS = 30

# criando os personagens
bg = Actor("bg", size=(600, 400))
gaton = Actor("Gaton", size=(100, 100), pos = (300, 350))
gatob = Actor("Gatoc", size=(100, 100))
tesla = Actor("Tesoura Laranja", size=(80, 80))
novbag = Actor("Novelob", size=(80, 80))
tesver = Actor("Tesoura Verde", size=(80, 80))
rodatear = Actor("Rodatear", size=(250, 250), pos=(50, 300))
novaz1 = Actor("Novaz1", size=(80, 80))
novver1 = Actor("Novver1", size=(80, 80))
novam1 = Actor("Novam1", size=(80, 80))
novverm1 = Actor("Novverm1", size=(80, 80))
win = Actor("win", size = (600,400))

# listas
novelos_bons = [novaz1, novver1, novam1, novverm1]
inimigos = [tesla, novbag, tesver]

# valores para o jogo
gaton_hp = 100
gaton_speed = 5
mode = "game"
points = 0
level = 1


# função de desenho
def draw():
    global mode
    global points
    
    bg.draw()
    if level == 1:
        rodatear.draw()
    gaton.draw()
    
    for novelo in novelos_bons:
        novelo.draw()
    for inimigo in inimigos:
        inimigo.draw()

    screen.draw.text(str(gaton_hp), (10,10), color = "black", fontsize = 30)
    screen.draw.text(str(points), (550,10), color = "black", fontsize = 30)

    if mode == "end":
        screen.fill("black")
        screen.draw.text("Perdeu! Sua pontuação final foi de:", (150,150), color = "white", fontsize = 25)
        screen.draw.text(str(points), (150,200), color = "white", fontsize = 30)
        screen.draw.text(("Aperte espaço para reiniciar"), (150,250), color = "white", fontsize = 20)

    if mode == "win":
        win.draw()

# posição inicial aleatória dos novelos bons
for novelo in novelos_bons:
    x = random.randint(50, 550)
    y = random.randint(-550, -50)
    novelo.pos = (x, y)
    novelo.speed = random.randint(2, 8)

# posição inicial aleatória dos inimigos
for inimigo in inimigos:
    x = random.randint(50, 550)
    y = random.randint(-550, -50)
    inimigo.pos = (x, y)
    inimigo.speed = random.randint(3, 10)  # inimigos descem um pouco mais rápido

def update(dt):
    global level
    global gaton_hp
    global mode
    global points
  
    if mode == "game":
        # movimentação horizontal do Gaton
        if keyboard.left:
            gaton.x -= gaton_speed
            if gaton.x < 50:  # limita o movimento à esquerda
                gaton.x = 50
        if keyboard.right:
            gaton.x += gaton_speed
            if gaton.x > WIDTH - 50:  # limita o movimento à direita
                gaton.x = WIDTH - 50
    
        # Atualiza a posição dos novelos bons
        for novelo in novelos_bons:
            novelo.y += novelo.speed
            if novelo.y > HEIGHT + 50:
                novelo.y = random.randint(-200, -50)
                novelo.x = random.randint(50, 550)
                novelo.speed = random.randint(2, 8)
    
        # Atualiza a posição dos inimigos
        for inimigo in inimigos:
            inimigo.y += inimigo.speed
            if inimigo.y > HEIGHT + 100:
                inimigo.y = random.randint(-300, -50)
                inimigo.x = random.randint(50, 550)
                inimigo.speed = random.randint(3, 10)
    
        col = gaton.collidelist(novelos_bons)
        if col != -1:
            gaton_hp += 15
            points += 1
            # reposiciona o novelo
            novelo = novelos_bons[col]
            novelo.y = random.randint(-200, -50)
            novelo.x = random.randint(50, 550)
            novelo.speed = random.randint(2, 8)
    
        coll = gaton.collidelist(inimigos)
        if coll != -1:
            gaton_hp -= 20
            if level == 2:
                gaton_hp -= 25
            if level == 3:
                gaton_hp -= 30
            
            # reposiciona o inimigo
            inimigo = inimigos[coll]
            inimigo.y = random.randint(-200, -50)
            inimigo.x = random.randint(50, 550)
            inimigo.speed = random.randint(2, 8)

    if gaton_hp <= 0:
        mode = "end"

    if mode == "end" or mode == "win" and keyboard.space:
        mode = "game"
        level = 1
        bg.image = "bg"
        points = 0
        gaton_hp = 100

    if level == 1 and points == 20:
        level = 2
        if level == 2:
            bg.image = "Céu Estrelado"
    elif level == 2 and points == 30:
        level = 3
        if level == 3:
            bg.image = "Templo"

    if points >= 50:
        mode = "win"
