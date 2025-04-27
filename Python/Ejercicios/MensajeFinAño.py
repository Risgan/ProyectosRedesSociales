import pygame
import random
import math
import sys

pygame.init()

width, height = 720, 800

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fireworks 2025')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

class Particle:
    def __init__(self, x, y, color, angle, speed):
        self.x = x
        self.y = y
        self.color = color
        self.angle = angle
        self.speed = speed
        self.lifetime = 255
        self.radius = 3

    def update(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

        self.lifetime -= 5
        self.radius += 0.1

    def draw(self, screen):
        if self.lifetime > 0:
            color = (self.color[0], self.color[1], self.color[2], self.lifetime)
            pygame.draw.circle(screen, color, (int(self.x), int(self.y)), int(self.radius))

class Firework:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.particles = []
        self.exploded = False
        self.colors = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA]
        self.explosion_size = random.randint(40, 80)
    
    def explode(self):
        for i in range(100):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(1, 5)
            color = random.choice(self.colors)
            self.particles.append(Particle(self.x, self.y, color, angle, speed))
        
        self.exploded = True

    def update(self):
        if not self.exploded:
            self.y -= 5
        else:
            for particle in self.particles:
                particle.update()
                if particle.lifetime <= 0:
                    self.particles.remove(particle)

    def draw(self, screen):
        if not self.exploded:
            pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 3)
        else:
            for particle in self.particles:
                particle.draw(screen)

class FadingText:
    def __init__(self, text, x, y, font_size, color):
        self.text = text
        self.x = x
        self.y = y
        self.font = pygame.font.Font(None, font_size)
        self.color = color
        self.lifetime = 255

    def update(self):
        self.lifetime -= 1

    def draw(self, screen):
        if self.lifetime > 0:
            text = self.font.render(self.text, True, (self.color[0], self.color[1], self.color[2], self.lifetime))
            screen.blit(text, (self.x, self.y))

def main():
    clock = pygame.time.Clock()
    Fireworks = []
    text = None
    start_time = pygame.time.get_ticks()

    while True:
        screen.fill(BLACK)

        if text is None:
            if pygame.time.get_ticks() - start_time < 2000:
                text = FadingText("2025", width // 2 - 50, height // 2 - 50, 48, WHITE)
            else:
                text = FadingText("Happy New Year!", width // 2 - 100, height // 2 - 50, 48, WHITE)

        text.update()
        text.draw(screen)

        if text.lifetime <= 0:
            if len(Fireworks) < 5:
                Fireworks.append(Firework(random.randint(50, width - 50), height))

        for firework in Fireworks:
            firework.update()
            firework.draw(screen)
            if firework.exploded and not firework.particles:
                Fireworks.remove(firework)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()