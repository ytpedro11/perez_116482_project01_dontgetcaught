from graphics import *
from random import randint

width = 900
height = 700

player_size = 50
enemy_size = 50
enemy_pos = [randint(0, width - enemy_size), 0]
enemy_list = [10]
win = GraphWin('Game', width, height)
Game_over = False
def player_rojo(win):

    player = Rectangle(Point(50, 50), Point(0, 0))
    player.setOutline("red")
    player.setFill("red")
    player.move(width / 2, height - 2 * player_size)
    player.draw(win)

    return player

def movimiento_player(win,player):
    dx, dy = 45, 0
    p = win.checkKey()
    if p == 'Left':
        player.move(-dx, dy)
    elif p == 'Right':
        player.move(dx, dy)

def enemigo(win):

    enemy = Rectangle(Point(enemy_size, enemy_size), Point(0, 0))
    enemy.setOutline("blue")
    enemy.setFill("blue")
    enemy.move(randint(0, width - 100), 0)
    enemy.draw(win)

    return enemy







def collision (player,enemy):
    px = player.getCenter().getX()
    py = player.getCenter().getY()

    ex = enemy.getCenter().getX()
    ey = enemy.getCenter().getY()

    if (ex >= px and ex < (px + player_size)) or (px >= ex and px < (ex + enemy_size)):
        if (ey >= py and ey < (py + player_size)) or (py >= ey and py < (ey + enemy_size)):
            return True
    print('false')

blue = enemigo(win)
jugador = player_rojo(win)

while not Game_over:


    movimiento_player(win,jugador)


    if collision(jugador,blue):
        break

    if blue.getCenter().getY() > 750:
        blue.undraw()
        blue = enemigo(win)

    blue.move(0, 10)

    update(40)









