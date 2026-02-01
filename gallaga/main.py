import pgzrun
import time
import random
WIDTH=600
HEIGHT=600


ship=Actor("ship")
ship.x=300
ship.y=570
bomb=Actor("bomb")
bomb.x=random.randint(30,570)
bomb.y=-10
bullets=[]
bullet_count=0
bugs=[]
bug=Actor("bug")
bugs.append(bug)
bugs[-1].x=random.randint(30,570)
bugs[-1].y=-10
score=0
shot_bugs=0
def on_key_down(key):
    if key==keys.SPACE:
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
    bomb.draw()
    screen.draw.text(str(score),center=(550,50),fontsize=(60))
    screen.draw.text("shot bugs:{}".format(shot_bugs),center=(510,100),fontsize=(40))
    






def update():
    global bullets,score,shot_bugs
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
            bug.x=random.randint(30,570)
        else:
            bug.y=bug.y+2
    if bomb.y>=602:
        bomb.y=-50
        bomb.x=random.randint(30,570)
    else:
        bomb.y=bomb.y+2
    for bug in bugs:
        for bullet in bullets:
            if bullet.colliderect(bug):
                bullets.remove(bullet)
                shot_bugs=shot_bugs+1
                score=score+10
                bug.y=-10
                bug.x=random.randint(30,570)
    for bullet in bullets:
        if bullet.colliderect(bomb):
            bullets.remove(bullet)
            score=score-10
            bomb.y=-100
            bomb.x=random.randint(30,570)


            # for i in range (10):
            #     bullet.y=bullet.y+3
            #     time.sleep(1)
            # bullets.pop(bullet)
            # bullet_count=bullet_count+1















 




pgzrun.go()









