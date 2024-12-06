import pygame
import time
import random

# Inicializar Pygame
pygame.init()

# Definir colores
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Definir tamaño de pantalla
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Definir velocidad de la serpiente y tamalo
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

# Definir fuente
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Funcion para morar puntaje
def Your_score(score):
    value = score_font.render("Tu puntaje: " + str(score), True, white)
    screen.blit(value, [0, 0])

# Funcion para dibujar la serpiente
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

# Funcion para mostrar mensaje fin del juego
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

# Funcion para el juego
def gameLoop():
    game_over = False
    game_close = False

    # Posicion inicial de la serpiente
    x1 = width / 2
    y1 = height / 2

    # Movimiento inicial de serpiente
    x1_change = 0
    y1_change = 0

    # Cuerpo de la serpiente
    snake_list = []
    length_of_snake = 1

    # Posicion de la comida
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        
        while game_close:
            screen.fill(blue)
            message("Perdiste! Presiona Q-Salir o C-Jugar de nuevo", red)
            Your_score(length_of_snake - 1)
            pygame.display.update()


            # Control de teclas despues de perder
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        # control de los eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Limites de la pantalla
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(black)

        # Dibujar la comida
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        # Actualizar la serpiente
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Colision si chocha con sigo misma
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Dibujar la serpiente
        our_snake(snake_block, snake_list)
        Your_score(length_of_snake - 1)

        pygame.display.update()

        # Si la serpiente come la comida
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # control de velocidad
        clock.tick(snake_speed)
    
    #Salir del juego
    pygame.quit()

# Iniciar el juego
gameLoop()