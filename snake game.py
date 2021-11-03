# Importting module using in this program
import pygame
import random
import os
pygame.mixer.init()

pygame.init()

darkgreen = (0, 150, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)


screen_width = 900
screen_height = 600
gamewindow = pygame.display.set_mode((screen_width, screen_height))

bg = pygame.image.load("C:\\Users\\MUHSIN\\My Projects\\snake Game\\folder\\back.jpg")
intro = pygame.image.load("C:\\Users\\MUHSIN\\My Projects\\snake Game\\folder\\wc.png.png")
outro = pygame.image.load("C:\\Users\\MUHSIN\\My Projects\\snake Game\\folder\\gameover.png.png")


pygame.display.set_caption("snake game")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont('Harrington', 55)

def text_screen(text, colour, x,y):
    screen_text = font.render(text, True, colour)
    gamewindow.blit(screen_text, [x,y])

def plot_snake(gamewindow, colour, snk_list , snakesize):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow, colour, [x,y, snakesize, snakesize])

def welcomScreen():
    pygame.mixer.music.load("C:\\Users\\MUHSIN\\My Projects\\snake Game\\music\\wc.mp3.mp3")
    pygame.mixer.music.play()
    gamewindow.blit(intro, (0, 0))
    exit_game = False
    while not exit_game:
        gamewindow.blit(intro, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load("C:\\Users\\MUHSIN\\My Projects\\snake Game\\music\\back.mp3.mp3")
                    pygame.mixer.music.play()
                    gamewindow.blit(bg, (0, 0))
                    gameloop()

        pygame.display.update()
        clock.tick(60)

def gameloop():
    exit_game = False
    game_over = False
    snake_x = 50
    snake_y = 50
    velocity_x = 0
    velocity_y = 0
    if (not os.path.exists("Highscore.txt")):
        with open("Highscore.txt", "w") as f:
            f.write("0")
    with open("Highscore.txt", "r") as f:
        Highscore = f.read()
    apple_x = random.randint(20, screen_width/2)
    apple_y = random.randint(20, screen_height/2)
    score = 0
    init_velocity = 3
    snake_size = 30
    fps = 60
    snk_list = []
    snk_lenght = 1

    while not exit_game:
        if game_over:
            with open("Highscore.txt", "w") as f:
                f.write(str(Highscore))
            gamewindow.blit(outro, (0, 0))
            text_screen("Score: " + str(score), darkgreen, 375, 350)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcomScreen()

        else:

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_f:
                        score += 10


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - apple_x) < 6 and abs(snake_y - apple_y) < 6:
                score += 10
                apple_x = random.randint(20, screen_width/2)
                apple_y = random.randint(20, screen_height/2)
                snk_lenght += 5
                if score > int(Highscore):
                    Highscore = score

            gamewindow.fill(black)
            gamewindow.blit(bg, (0, 0))
            text_screen("score : " + str(score) + "  Highscore: "+str(Highscore), darkgreen, 5, 5)
            pygame.draw.rect(gamewindow, white, [apple_x, apple_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_lenght:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                gamewindow.blit(outro, (0, 0))
                pygame.mixer.music.load("C:\\Users\\MUHSIN\\My Projects\\snake Game\\music\\gameover.mp3.mp3")
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                gamewindow.blit(outro, (0, 0))
                pygame.mixer.music.load("C:\\Users\\MUHSIN\\My Projects\\snake Game\\music\\gameover.mp3.mp3")
                pygame.mixer.music.play()
                gamewindow.blit(outro, (0, 0))
            plot_snake(gamewindow, red, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcomScreen()