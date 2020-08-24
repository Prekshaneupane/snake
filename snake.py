import pygame
import random
import os

pygame.mixer.init()
pygame.init()

#color
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

#create window
screen_width = 700
screen_height = 600
gamewn = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_mode((screen_width, screen_height))

#caption
pygame.display.set_caption("snake Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

def text_screen(text, color, x, y):
    screen_text= font.render(text, True, color)
    gamewn.blit(screen_text,[x,y])

#body
def plot_snake(gamewn, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gamewn, color, [x, y, snake_size, snake_size])
   
def welcome():
    exit_game = False
    while not exit_game:
        gamewn.fill((255, 233,210))
        text_screen("WELCOME TO SNAKE GAME", black, 240, 250)
        text_screen("PRESS SPACE TO PLAY", black, 240, 280)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('music.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update() 
        clock.tick(60)

#game loop
def gameloop():
    #variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_list = []
    snake_length = 1

 #check highscore file
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        highscore = f.read()
     
    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60

    while not exit_game:
        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(highscore))

            gamewn.fill(white)
            text_screen("GAME OVER!  PRESS ENTER TO CONTINUE", red, 100, 250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()


        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

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
                    if event.key == pygame.K_q:
                          score += 10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score += 10
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snake_length += 5
                if score>int(highscore):
                    highscore = score 

            gamewn.fill(white)
            

            text_screen("Score:" + str(score)  +   "   Highscore: " +str(highscore), red, 5, 5)
            pygame.draw.rect(gamewn, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
            plot_snake(gamewn, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
                
    pygame.quit()
    quit()
welcome()  

