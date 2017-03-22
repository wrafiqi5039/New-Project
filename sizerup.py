from gamelib import *

game = Game(640,480,"Size-Up")

bk = Image("images\\maze.png",game)
bk.resizeTo(game.width, game.height)

game.setBackground(bk)

timer = 6000

Sizzo = Image("images\\w2.png",game)
Sizzo.resizeBy(-99)
Sizzo.moveTo(50,50)
Ghost = Image("images\\ghost.png",game)
Ghost.resizeBy(-95)

title = Image("images\\km2.png",game)
bk.draw()
title.draw()
game.drawText("Press [SPACE] to play",320,400)
game.update(1)
game.wait(K_SPACE)

while not game.over:
    timer-=1
    if timer <= 0:
        game.over = True
    game.processInput()
    game.drawBackground()
    Sizzo.draw()
    Ghost.draw()
    
    if keys.Pressed[K_UP]:
        Sizzo.moveY(-2)
    if keys.Pressed[K_DOWN]:
        Sizzo.moveY(2)
    if keys.Pressed[K_RIGHT]:
        Sizzo.moveX(2)
    if keys.Pressed[K_LEFT]:
        Sizzo.moveX(-2)
    if keys.Pressed[K_w]:
        Ghost.moveY(-2)
    if keys.Pressed[K_s]:

        Ghost.moveY(2)
    if keys.Pressed[K_d]:
        Ghost.moveX(2)
    if keys.Pressed[K_a]:
        Ghost.moveX(-2)
    if Sizzo.collidedWith(Ghost):
        game.over = True
    game.drawText


    game.drawText("Timer = " + str(timer), 500,0)

    game.update(60)
game.quit()










































