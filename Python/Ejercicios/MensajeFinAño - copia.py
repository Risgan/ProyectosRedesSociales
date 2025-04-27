import pygame
import random
import math
import sys

# Initialize pygame
pygame.init()

# Set up display
width, height = 720, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fireworks 2025')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Particle class
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
        # Move particle based on angle and speed
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

        # Decrease lifetime (for fading)
        self.lifetime -= 5
        self.radius += 0.1

    def draw(self, screen):
        if self.lifetime > 0:
            # Fade the particle based on lifetime
            color = (self.color[0], self.color[1], self.color[2], self.lifetime)
            pygame.draw.circle(screen, color, (int(self.x), int(self.y)), int(self.radius))

# Firework class
class Firework:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.particles = []
        self.exploded = False
        self.colors = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA]
        self.explosion_size = random.randint(40, 80)

    def explode(self):
        # Create particles with random angles and speeds
        num_particles = random.randint(50, 100)
        for _ in range(num_particles):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(3, 6)
            color = random.choice(self.colors)
            self.particles.append(Particle(self.x, self.y, color, angle, speed))
        self.exploded = True

    def update(self):
        for particle in self.particles:
            particle.update()

    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)

# Text class to handle '2025' text display
class FadingText:
    def __init__(self, text, x, y, duration, color):
        self.text = text
        self.x = x
        self.y = y
        self.duration = duration
        self.alpha = 255
        self.color = color

    def update(self):
        # Fade the text over time
        self.alpha -= 5
        if self.alpha < 0:
            self.alpha = 0

    def draw(self, screen):
        font = pygame.font.SysFont("Arial", 48)
        text_surface = font.render(self.text, True, self.color)
        text_surface.set_alpha(self.alpha)
        screen.blit(text_surface, (self.x, self.y))

# Main game loop
def main():
    clock = pygame.time.Clock()
    fireworks = []
    text = None
    start_time = pygame.time.get_ticks()

    while True:
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Create new firework randomly
        if random.random() < 0.02:
            firework = Firework(random.randint(0, width), random.randint(0, height // 2))  # Random positions
            fireworks.append(firework)

        # Update fireworks
        for firework in fireworks:
            if not firework.exploded:
                firework.explode()
                text_color = random.choice([RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA])  # Random color for text
                text = FadingText('2025', firework.x - 50, firework.y - 50, 2000, text_color)
            firework.update()
            firework.draw(screen)

        # Update and draw the fading text
        if text:
            text.update()
            text.draw(screen)

        # Remove fireworks after they have exploded and finished fading
        fireworks = [f for f in fireworks if any(p.lifetime > 0 for p in f.particles)]

        pygame.display.flip()

        # Exit after a certain time
        if pygame.time.get_ticks() - start_time > 30000:  # Run for 30 seconds
            pygame.quit()
            sys.exit()

        clock.tick(120)

if __name__ == "__main__":
    main()
