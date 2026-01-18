import pgzrun
import time
WIDTH=600
HEIGHT=600


ship=Actor("ship")
ship.x=300
ship.y=570

bullets=[]
bullet_count=0
bugs=[]
bug=Actor("bug")
bugs.append(bug)
bugs[-1].x=200
bugs[-1].y=-10

def on_key_down(key):
    if key==keys.SPACE:
        print("red")
        bullet=Actor("bullet")
        bullets.append(bullet)
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y-50

def draw():
    # global bullets
    screen.blit("space",(0,0))
    ship.draw()
    for bullet in bullets:
        bullet.draw()
    bug.draw()
    






def update():
    global bullets
    if keyboard.left:
        ship.x=ship.x-5
    if keyboard.right:
        ship.x=ship.x+5

    for bullet in bullets:
        if bullet.y<=0:
            bullets.remove(bullet)
        else:
            bullet.y=bullet.y-2
    for bug in bugs:
        if bug.y>=602:
            bug.y=-10
        else:
            bug.y=bug.y+2

    
            # for i in range (10):
            #     bullet.y=bullet.y+3
            #     time.sleep(1)
            # bullets.pop(bullet)
            # bullet_count=bullet_count+1


















pgzrun.go()









