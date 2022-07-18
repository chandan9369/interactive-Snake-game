import pygame
import random
import time
import os

#MUSIC
def music(str):
    pygame.mixer.init()
    pygame.mixer.music.load(str)
    pygame.mixer.music.play()
    # pygame.mixer.music.rewind()

def music_rew(str):
    pygame.mixer.music.load(str)
    pygame.mixer.music.play()
    pygame.mixer.music.rewind()

pygame.init()

#SPEAK
def read(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice").Speak

    speak(str)


def greet():
    read("\nWelcome to Snake Game ")
    print("\tWelcome to Snake Game")
    read("\tThe rules of these games are as follows")
    print("\tThe rules of these games are as follows")
    read("\twhenever snake eat food score increased by 10")
    print("\twhenever snake eat food score increased by 10")
    read("\tif snack touches its body then game is over")
    print("\tif snack touches its body then game is over")

    time.sleep(2)

    read("functions for playing this snake game on desktop ")
    print("\n\tfunctions for playing this snake game on desktop")
    read("\tPress left arrow key to move the snake to the left")
    print("\tPress left arrow key to move the snake to the left")
    read("\tPress right arrow key to move the snake to the right")
    print("\tPress right arrow key to move the snake to the right")
    read("\tPress up arrow key to move the snake to the up")
    print("\tPress up arrow key to move the snake to the up")
    read("\tPress down arrow key to move the snake to the down")
    print("\tPress down arrow key to move the snake to the down")


# greet()
# read("\nNow game will start in few seconds...")
# time.sleep(3)
# read("Enjoy the game")

#colore

dGreen=(102,51,0)
red=(204,0,0)
lGreen=(153,255,153)
white=(255,255,255)
black=(0,0,0)
color1=(0,153,153)
yellow=(255,255,0)
dBlue=(0,51,102)
lightViolet=(204,255,229)
light_black=(192,192,192)
pink=(255,204,204)
lBlue1=(204,229,255)
BLACK=(51,51,0)
lpink=(255,205,153)
green=(0,204,0)
#this colors are initialized as per rgb values of
# color for more go to https://www.rapidtables.com/web/color/RGB_Color.html

displayWidth=900
displayHeight=600

#Game Window
GameWindow=pygame.display.set_mode((displayWidth,displayHeight))
icon = pygame.image.load("snake (1).png")
pygame.display.set_icon(icon)

pygame.display.set_caption("Snack Game")
pygame.display.update()

# backGround Image
def back(str):
    bg=pygame.image.load(str)
    GameWindow.blit(bg,(0,0))


# Displaying text
font=pygame.font.SysFont(None,50)
def ScreenScore(text,color,x,y):
      screen_text=font.render(text,True,color)
      GameWindow.blit(screen_text,[x,y])

# Plotting snake
def plotSnake(gm,col,size,*snklist):
    snklist=list(snklist)
    for x,y in snklist:
        # pygame.draw.rect(gm, col,[x,y,size,size])
        pygame.draw.ellipse(gm,col,[x,y,size,size],0)

# Drawing Apple
def draw_apple(gm,x,y):
    icon = pygame.image.load('apple.png')
    gm.blit(icon,(x,y))

# def draw_
# Game Loop

def gameloop():
    with open("highScore.txt","r") as f:
        high = f.read()

    # game Specific variable
    Game_exit = False
    Game_over = False
    snake_x = random.randint(0, displayWidth)
    snake_y = random.randint(0, displayHeight)
    snake_size = 20
    food_size = 15
    fps = 60  # fps=frame per second

    initial_velocity = 3

    clock = pygame.time.Clock()
    snake_velocity_x = 0
    snake_velocity_y = 0

    X_food = random.randint(20, displayWidth / 2)
    Y_food = random.randint(20, displayHeight / 2)

    score = 0
    snakeList = []
    snake_length = 1

    while not Game_exit:
        if Game_over:
            GameWindow.fill(lBlue1)
            back("back3.png")
            # pygame.mixer.music.rewind()
            # ScreenScore("Press Enter To Continue",lpink,220, 250)
            ScreenScore(": " + str(int(score)),white, 530,305)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        music_rew("Snake Game - Theme Song.mp3")
                        print("\n")
                        gameloop()

        else:

           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   Game_exit = True

               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_RIGHT:
                       snake_velocity_x += initial_velocity
                       snake_velocity_y = 0

                   if event.key == pygame.K_LEFT:
                       snake_velocity_x -= initial_velocity
                       snake_velocity_y = 0

                   if event.key == pygame.K_UP:
                       snake_velocity_y = -initial_velocity
                       snake_velocity_x = 0

                   if event.key == pygame.K_DOWN:
                       snake_velocity_y = initial_velocity
                       snake_velocity_x = 0


                   # this below condition is for cheating
                   if event.key == pygame.K_q:
                       score+=10

           if abs(snake_x - X_food) < 6 and abs(snake_y - Y_food) < 6:
               score += 10
               print("Score : ", score)
               X_food = random.randint(20, displayWidth / 2)
               Y_food = random.randint(20, displayHeight / 2)
               snake_length += 5


           # showing high score
           if score>int(high):
               high=score
               if (os.path.exists("highscore.txt")):
                   with open("highScore.txt", "w") as m:
                       m.write(str(high))

           snake_x += snake_velocity_x
           snake_y += snake_velocity_y

           GameWindow.fill(lBlue1)
           back("back2.png")



           ScreenScore("Score : " + str(score),white,350,2)
           ScreenScore("High Score : " + str(int(high)),white,300,550)
           # pygame.draw.rect(GameWindow,red, [X_food, Y_food, food_size, food_size])
           draw_apple(GameWindow,X_food,Y_food)

           head = []
           head.append(snake_x)
           head.append(snake_y)
           snakeList.append(head)

           plotSnake(GameWindow, green, snake_size, *snakeList)

           if len(snakeList) > snake_length:
               del snakeList[0]

           if head in snakeList[:-1]:
               Game_over = True
               music("Snake death shout.mp3")


           if snake_x < 0 or snake_x > displayWidth or snake_y < 0 or snake_y > displayHeight:
               Game_over = True
               music("Snake death shout.mp3")




        pygame.display.update()  # this we have to use to update
        clock.tick(fps)

    pygame.quit()
    quit()



def Welcome():
    Game_exit=False
    clock = pygame.time.Clock()
    music("Snake Game - Theme Song.mp3")
    # GameWindow.blit(backImage1)
    while not Game_exit:
        GameWindow.fill(lBlue1)
        back("back1.png")
        # ScreenScore("Welcome to Snake World ",black,220,250)
        # ScreenScore("Press space baar to play Snack Game",black, 150, 300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game_exit = True

            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(60)

Welcome()

