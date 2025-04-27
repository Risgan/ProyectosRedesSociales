import pygame
import time
import math
import random

# Inicializar pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 700, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("San Valentín")

# Colores
BLACK = (0, 0, 0)
RED = (255, 0, 0)
RAINBOW_COLORS = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), 
                    (0, 0, 255), (75, 0, 130), (148, 0, 211)]

# Fuente para el texto
font = pygame.font.Font(None, 50)

# Lista de fuegos artificiales
fireworks = []

class Firework:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.particles = [(x, y, random.uniform(-4, 4), random.uniform(-4, 4)) 
                        for _ in range(50)]
        self.timer = 20
    
    def update(self):
        self.timer -= 1
        self.particles = [(px + vx, py + vy, vx * 0.8, vy * 0.8 + 0.2) for px, py, vx, vy in self.particles]
    
    def draw(self, surface):
        for px, py, _, _ in self.particles:
            pygame.draw.circle(surface, self.color, (int(px), int(py)), 2)

def draw_heart(surface, x, y, size, fill=True):
    points = []
    for t in range(0, 360, 2):
        rad = math.radians(t)
        px = int(x + size * 16 * math.sin(rad) ** 3)
        py = int(y - size * (13 * math.cos(rad) - 5 * math.cos(2 * rad) - 2 * math.cos(3 * rad) - math.cos(4 * rad)))
        points.append((px, py))
    
    if fill:
        pygame.draw.polygon(surface, RED, points)
    else:
        pygame.draw.polygon(surface, RED, points, 3)

# Loop principal
running = True
fill_heart = True
color_index = 0
clock = pygame.time.Clock()
time_last_toggle = time.time()

while running:
    screen.fill(BLACK)
    
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for _ in range(7):
                fireworks.append(Firework(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50), random.choice(RAINBOW_COLORS)))
    
    # Renderizar texto con color de arcoíris
    text_color = RAINBOW_COLORS[color_index]
    text = font.render("Feliz", True, text_color)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 130))
    screen.blit(text, text_rect)
    
    # Dibujar corazón
    draw_heart(screen, WIDTH // 2, HEIGHT // 2 - 50, 5, fill_heart)
    
    # Renderizar texto con color de arcoíris
    text = font.render("San Valentín", True, text_color)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(text, text_rect)
    
    # Dibujar fuegos artificiales
    for firework in fireworks[:]:
        firework.update()
        firework.draw(screen)
        if firework.timer <= 0:
            fireworks.remove(firework)
    
    pygame.display.flip()
    
    # Alternar estado del corazón y cambiar color del texto cada 0.5s
    if time.time() - time_last_toggle >= 0.3:
        fill_heart = not fill_heart
        color_index = (color_index + 1) % len(RAINBOW_COLORS)
        time_last_toggle = time.time()
    
    clock.tick(60)
    
pygame.quit()
