import pgzrun

WIDTH=600
HEIGHT=600


ship=Actor("ship")
ship.x=300
ship.y=570


# def bug_code():
#     for i in range(10)
#         bug=Actor("bug")



def draw():
    screen.blit("space",(0,0))
    ship.draw()




def update():
    if keyboard.left:
        ship.x=ship.x-5
    if keyboard.right:
        ship.x=ship.x+5














pgzrun.go()









