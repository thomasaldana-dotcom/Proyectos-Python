import pygame
import random
import math
import io
import sys
import os

from pygame import mixer

pygame.init()

def ruta_recurso(ruta_relativa):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, ruta_relativa)


# Ventana
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego de la nave")

icono = pygame.image.load(ruta_recurso("assets/icono.png"))
pygame.display.set_icon(icono)

fondo = pygame.image.load(ruta_recurso("assets/fondo.jpg"))
fondo = pygame.transform.scale(fondo, (800, 600))

# Música
mixer.music.load(ruta_recurso("assets/MusicaFondo.mp3"))
mixer.music.set_volume(0.5)
mixer.music.play(-1)

# Jugador
img_jugador = pygame.image.load(ruta_recurso("assets/jugador_meteoro.png"))
img_jugador = pygame.transform.scale(img_jugador, (50, 50))

jugador_x = 370
jugador_y = 520
jugador_x_cambio = 0

# Enemigos
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []

cantidad_enemigos = 8
velocidad_enemigo = 0.8

for i in range(cantidad_enemigos):
    img = pygame.image.load(ruta_recurso("assets/enemigo.png"))
    img = pygame.transform.scale(img, (50, 50))
    img_enemigo.append(img)

    enemigo_x.append(random.randint(0, 750))
    enemigo_y.append(random.randint(50, 150))
    enemigo_x_cambio.append(velocidad_enemigo)
    enemigo_y_cambio.append(40)

# Balas múltiples
balas = []
img_bala = pygame.image.load(ruta_recurso("assets/bala.png"))
img_bala = pygame.transform.scale(img_bala, (80, 80))

# Puntaje

def fuente_bytes(fuente):
    with io.open(fuente, "rb") as f:
        return io.BytesIO(f.read())


puntaje = 0
fuente_como_byte = fuente_bytes(ruta_recurso("FreeSansBold.ttf"))
fuente = pygame.font.Font(fuente_como_byte, 32)
fuente_final = pygame.font.Font(fuente_como_byte, 64)

def mostrar_puntaje():
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    screen.blit(texto, (10, 10))

def texto_final():
    texto = fuente_final.render("FIN DEL JUEGO", True, (255, 255, 255))
    screen.blit(texto, (200, 250))

def jugador(x, y):
    screen.blit(img_jugador, (x, y))

def enemigo(x, y, i):
    screen.blit(img_enemigo[i], (x, y))

def hay_colision(ex, ey, bx, by):
    distancia = math.sqrt((ex - bx) ** 2 + (ey - by) ** 2)
    return distancia < 27

# Loop principal
running = True
game_over = False

def reiniciar_juego():
    global puntaje, balas, jugador_x, jugador_x_cambio, game_over

    puntaje = 0
    balas.clear()
    jugador_x = 370
    jugador_x_cambio = 0
    game_over = False

    for i in range(cantidad_enemigos):
        enemigo_x[i] = random.randint(0, 750)
        enemigo_y[i] = random.randint(50, 150)
        enemigo_x_cambio[i] = velocidad_enemigo


while running:
    screen.blit(fondo, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jugador_x_cambio = -1
            if event.key == pygame.K_RIGHT:
                jugador_x_cambio = 1
            if event.key == pygame.K_SPACE:
                if game_over:
                    reiniciar_juego()
                else:
                    sonido_bala = mixer.Sound(ruta_recurso("assets/disparo.mp3"))
                    sonido_bala.play()
                    balas.append({
                        "x": jugador_x,
                        "y": jugador_y,
                    "velocidad": -5
                })

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                jugador_x_cambio = 0

    # Movimiento jugador
    jugador_x += jugador_x_cambio
    jugador_x = max(0, min(jugador_x, 750))

    # Enemigos
    for i in range(cantidad_enemigos):

        if enemigo_y[i] >= 450:
            for j in range(cantidad_enemigos):
                enemigo_y[j] = 2000
            
            balas.clear()
            game_over = True
            break
            
            

        enemigo_x[i] += enemigo_x_cambio[i]

        if enemigo_x[i] <= 0:
            enemigo_x_cambio[i] = velocidad_enemigo
            enemigo_y[i] += enemigo_y_cambio[i]
        elif enemigo_x[i] >= 750:
            enemigo_x_cambio[i] = -velocidad_enemigo
            enemigo_y[i] += enemigo_y_cambio[i]

        for bala in balas[:]:
            if hay_colision(enemigo_x[i], enemigo_y[i], bala["x"], bala["y"]):
                sonido = mixer.Sound(ruta_recurso("assets/Golpe.mp3"))
                sonido.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_x[i] = random.randint(0, 750)
                enemigo_y[i] = random.randint(50, 150)
                break

        enemigo(enemigo_x[i], enemigo_y[i], i)

    # Balas
    for bala in balas[:]:
        bala["y"] += bala["velocidad"]
        screen.blit(img_bala, (bala["x"] - 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)

    jugador(jugador_x, jugador_y)
    mostrar_puntaje()

    if game_over:
        texto_final()

    pygame.display.update()

pygame.quit()

