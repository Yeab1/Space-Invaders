import turtle
import math
import random
import pygame
print("ftp stands fpr first time player....it is the easiest level. vh stands for very hard and is the hardest level of the game")
question = input("choose level[extreme/advanced/experienced/easy/recruit]")

#add some music
pygame.init()

shoot_sound = pygame.mixer.Sound("shoot.wav")
explosion = pygame.mixer.Sound("hit.wav")
background_music = pygame.mixer.music.load("space_2018_bgmusic.wav")
game_over = pygame.mixer.Sound("gameover.wav")


#create the window to play with
pygame.mixer.music.play(-1)
wn = turtle.Screen()
wn.bgcolor("white")
wn.title('space 2018!')
wn.bgpic("space_2018_bg.gif")
print("press space to shoot and the left and right arrows to move")
print("hint: hit the enemies on the left and right extremes!")

    #register shapes to use

turtle.register_shape("player.gif")
turtle.register_shape("enemy.gif")
turtle.register_shape("bullet.gif")

    #create the border

border_pen = turtle.Turtle()
border_pen.speed(100000000)
border_pen.color("black")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(4)

for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)

border_pen.hideturtle()

    #create a score board
score = 0

    #create the border
score_pen = turtle.Turtle()
score_pen.speed(10)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 260)
score_pen.pendown()
score_pen.pensize(2)
score_pen.forward(150)
score_pen.left(90)
score_pen.forward(30)
score_pen.left(90)
score_pen.forward(150)
score_pen.left(90)
score_pen.forward(30)
score_pen.hideturtle()
scorestring = "score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial",20, "normal"))


    #create a player Turtle

player = turtle.Turtle()
player.color("Blue")
player.shape("player.gif")
player.penup()
player.speed(10000)
player.setposition(0,-260)
player.left(90)
losestring = "Game over! you scored: %s" %score
    #move the player left and right

playerspeed = 25

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x<-280:
        x = -280
    player.setx(x)

    #create keyboard bindings

turtle.listen()
turtle.onkey(move_left, "Left")

def move_right():
    x = player.xcor()
    x += playerspeed
    if x>280:
        x = 280
    player.setx(x)
    #create keyboard bindings
turtle.listen()
turtle.onkey(move_right, "Right")

    #make the bullet

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("bullet.gif")
bullet.penup()
bullet.speed(10000)
bullet.hideturtle()
bullet.left(90)
bullet.shapesize(0.5, 0.5)

    #shoot the bullet
    #put the bullet just above the player to start with

bulletspeed = 70
bulletstate = "ready"

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()
        pygame.mixer.Sound.play(shoot_sound)

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2)+ math.pow(t1.ycor()- t2.ycor(), 2))
    if question == "easy":
        if distance < 45:
            return True
        else:
            return False
    elif question == "experienced":
        if distance < 35:
            return True
        else:
            return False
    elif question == "extreme":
        if distance < 15:
            return True
        else:
            return False
    elif question == "recruit":
        if distance < 60:
            return True
        else:
            return False
    elif question == "advanced":
        if distance < 25:
            return True
        else:
            return False

    #create keyboard Bindings
turtle.listen()
turtle.onkey(fire_bullet, "space")

    #choose the number of enemies

number_of_enemies = 5
    #create an empty list of enemies
enemies = []

    #Add enemies to the list
for i in range(number_of_enemies):
    #create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:

    enemy.color("red")
    enemy.shape("enemy.gif")
    enemy.penup()
    x = random.randint(-200, 200)
    y = random.randint(200, 250)
    enemy.speed(100000000)
    enemy.setposition(x, y)
    enemy.shapesize(1.0, 1.0)

enemyspeed = 8

    #main game loop
while True:

    for enemy in enemies:
            #move the enemy

        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.ycor()<-280:
                #player loses if the enemies go out of the screen

            lose = turtle.Turtle()
            lose.speed(3)
            lose.color("white")
            lose.penup()
            lose.setposition(-220, -30)
            lose.pendown()
            lose.pensize(0)
            lose.forward(440)
            lose.left(90)
            lose.forward(50)
            lose.left(90)
            lose.forward(440)
            lose.left(90)
            lose.forward(50)
            lose.hideturtle()

            losestring = "Game over! you scored: %s" %score
            lose.write(losestring, False, align="left", font=("Comic Sans MS",25, "normal"))
            pygame.mixer.music.fadeout(4000)
            pygame.mixer.Sound.play(game_over)
        if enemy.xcor() > 280:
            for e in enemies:
                y = enemy.ycor()
                y -= 40
                e.sety(y)
            #change the enemy direction
            enemyspeed *= -1



        if enemy.xcor() < -280:
            for e in enemies:

                y = enemy.ycor()
                y-=40
                e.sety(y)
            #change the enemy direction
            enemyspeed *= -1

            #check f or the collision between bullet and the enemy
        if isCollision(bullet, enemy):

                #reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
                #reset the enemy
            enemy.setposition(-200, 250)
                #change the score
            score += 50
            scorestring = "score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Comic Sans MS",20, "normal"))
            pygame.mixer.Sound.play(explosion)
            pygame.mixer.Sound(explosion).set_volume(1.0)
            #check for the collision between the bullet and the player
        if isCollision(player, enemy):

            player.hideturtle()
            enemy.hideturtle()
                #create "you lose"

            lose = turtle.Turtle()
            lose.speed(3)
            lose.color("white")
            lose.penup()
            lose.setposition(-220, -30)
            lose.pendown()
            lose.pensize(0)
            lose.forward(440)
            lose.left(90)
            lose.forward(50)
            lose.left(90)
            lose.forward(440)
            lose.left(90)
            lose.forward(50)
            lose.hideturtle()

            losestring = "Game over! you scored: %s" %score
            lose.write(losestring, False, align="left", font=("Comic Sans MS",25, "normal"))
            print ("!!!GAME OVER!!!")
            print ("Nice,try u scored: ", score)
            pygame.mixer.music.fadeout(4000)
            pygame.mixer.Sound.play(game_over)
            break


        #move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)



        #check if the bullet reaches the top of the window
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"
else:
    print("Ok then, good day!")
    print("come back for a good game when you are in a good mood")




