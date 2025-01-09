import pgzrun, random

TITLE="Ship Shooting"
WIDTH=800
HEIGHT=700

speed=5

bullets=[]
enemies=[]
directions=1
gameover=False

score=0
ship=Actor("ship.png")
ship.dead=False
for i in range(7):
    for j in range(4):
        enemy=Actor("bug.png")
        enemies.append(enemy)
        enemies[-1].x=100+50*i #to update recently added element
        enemies[-1].y=-100+50*j


ship.pos=(WIDTH/2, HEIGHT-50)

def draw():
    global gameover
    screen.clear()
    screen.fill("lightpink")
    if not ship.dead:  
        ship.draw()
    for i in enemies:
        i.draw()
    screen.draw.text(str(score), (50,50), color="navy")
    for i in bullets:
        i.draw()
    if gameover:
        screen.draw.text("GAME OVER", (WIDTH/2,HEIGHT/2), color="navy")
    if len(enemies)==0:
        gameover=True
    
def update():
    global score, directions
    if keyboard.left:
        ship.x-=speed
        if ship.x<50:
            ship.x=50
    elif keyboard.right:
        ship.x+=speed
        if ship.x>WIDTH-50:
            ship.x=WIDTH-50
    if len(enemies)>0 and (enemies[-1].x>WIDTH-80 or enemies[0].x<80):
        movedown=True
        directions=directions*(-1)
    for i in enemies:
        i.y+=2
        i.x+=5*directions
        if i.y>HEIGHT:
            enemies.remove(i)
        for c in bullets:
            if i.colliderect(c):
                enemies.remove(i)
                bullets.remove(c)
                score+=20
        if i.colliderect(ship):
            ship.dead=True
       
    for b in bullets:
        b.y-=5
        if b.y<0:
            bullets.remove(b)   
    
def on_key_down(key):
    if key==keys.SPACE and not ship.dead:
        bullets.append(Actor("bullet"))
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y-50



pgzrun.go()