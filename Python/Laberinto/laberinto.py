import pygame
import random
import os

# Inicializamos Pygame
pygame.init()

# Definimos el tamaño de la pantalla
ANCHO_VENTANA = 950
ALTO_VENTANA = 950
TAM_CELDA = 15
N = ANCHO_VENTANA // TAM_CELDA
M = ALTO_VENTANA // TAM_CELDA

# Definimos los colores
NEGRO = (0,0,0)
BLANCO = (255,255,255)
ROJO = (255,0,0)
AZUL = (0,0,255)

# Iniciar pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Juego del Laberinto")

#Crear laberinto aleatorio
def generar_laberinto():
    laberinto = [[1] * N for _ in range(M)]
    
    # funcion recursiva para generar el laberinto
    def generar (x,y):
        direcciones = [(0,1),(1,0),(0,-1),(-1,0)]
        random.shuffle(direcciones)

        for dx, dy in direcciones:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < N and 0 <= ny < M and laberinto[ny][nx] == 1:
                laberinto[ny][nx] = 0
                laberinto[y+dy][x+dx] =0
                generar(nx, ny)

    # iniciar generacion desde 1,1
    laberinto[1][1] = 0
    generar(1,1)
    return laberinto

# Dibujar en pantalla el laberinto
def dibujar_laberinto(laberinto):
    for i in range(M):
        for j in range(N):
            color = BLANCO if laberinto[i][j] == 0 else NEGRO
            pygame.draw.rect(pantalla, color, (j * TAM_CELDA, i * TAM_CELDA, TAM_CELDA, TAM_CELDA))


class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((TAM_CELDA,TAM_CELDA))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.topleft = (TAM_CELDA, TAM_CELDA)
    
    def mover(self, dx, dy, laberinto):
        if 0<=(self.rect.x+dx) // TAM_CELDA < N and 0 <= (self.rect.y+dy)// TAM_CELDA < M:
            if laberinto[(self.rect.y + dy)//TAM_CELDA][(self.rect.x + dx)//TAM_CELDA] == 0:
                self.rect.x += dx
                self.rect.y += dy

#funcion principal
def main():

    laberinto = generar_laberinto()

    jugador = Jugador()

    todos_sprites = pygame.sprite.Group()
    todos_sprites.add(jugador)

    reloj = pygame.time.Clock()

    corriendo = True

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
        
        teclas = pygame.key.get_pressed()
        dx = dy = 0

        if teclas[pygame.K_LEFT]:
            dx = -TAM_CELDA
        if teclas[pygame.K_RIGHT]:
            dx = TAM_CELDA
        if teclas[pygame.K_UP]:
            dy = -TAM_CELDA
        if teclas[pygame.K_DOWN]:
            dy = TAM_CELDA
        
        jugador.mover(dx, dy, laberinto)

        pantalla.fill(NEGRO)
        dibujar_laberinto(laberinto)
        todos_sprites.draw(pantalla)

        pygame.display.flip()

        reloj.tick(10)
    
    pygame.quit()

if __name__ == "__main__":
    main()