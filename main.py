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

player = Rectangle(Point(50, 50), Point(0, 0))
player.setOutline("red")
player.setFill("red")
player.move(width / 2, height - 2 * player_size)
player.draw(win)

def enemigo(win):

    enemy = Rectangle(Point(enemy_size, enemy_size), Point(0, 0))
    enemy.setOutline("blue")
    enemy.setFill("blue")
    enemy.move(randint(0, width - 100), 0)
    enemy.draw(win)

    return enemy

blue = enemigo(win)

while not Game_over:
    px = player.getCenter().getX()
    py = player.getCenter().getY()

    ex = blue.getCenter().getX()
    ey = blue.getCenter().getY()

    if (ex >= px and ex < (px + player_size)) or (px >= ex and px < (ex + enemy_size)):
        if (ey >= py and ey < (py + player_size)) or (py >= ey and py < (ey + enemy_size)):
            Game_over = True
        print("false")


    if blue.getCenter().getY() > 750:
        blue.undraw()
        blue = enemigo(win)



    blue.move(0, 10)
    update(20)



    dx, dy = 45, 0
    p = win.checkKey()
    if p == 'Left':
        player.move(-dx, dy)
    elif p == 'Right':
        player.move(dx, dy)


while Game_over:

    win1 = GraphWin('GAME OVER', width, height)
    text = Text(Point(width/2, height/2), "GAME OVER")
    text.setSize(30)
    text.draw(win1)
    win.getMouse()
    win.close()
