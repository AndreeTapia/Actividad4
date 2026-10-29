"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange
from turtle import *

from freegames import vector

gravity = 0.35
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
state = {'score': 0}
writer = Turtle(visible=False)
writer.up()
writer.goto(130, 180)
writer.color('black')
writer.write(f"Puntuación: {state['score']}", font=("Arial", 14, "normal"))


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    writer.undo()
    writer.up()
    writer.goto(130, 180)
    writer.color('black')
    writer.write(f"Puntuación: {state['score']}", font=("Arial", 14, "normal"))

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)  
        dot(6, 'red')

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5
    
    if inside(ball):
        global gravity
        speed.y -= gravity
        ball.move(speed)
    
    dupe = targets.copy()
    targets.clear()

    for target in dupe:    
        if abs(target - ball) > 13:
            targets.append(target)
        else:
            state['score'] += 1
            writer.undo()    
            writer.write(f"Puntuación: {state['score']}", font=("Arial", 14, "normal"))
            
    draw()
    
    for target in targets:
        if not inside(target):
            return
    
    ontimer(move, 50)


def mas_gravedad():
    global gravity
    gravity += 0.05
    print("Gravedad:", round(gravity, 2))

def menos_gravedad():
    global gravity
    if gravity > 0.05:
        gravity -= 0.05
    print("Gravedad:", round(gravity, 2))


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
listen()
onkey(mas_gravedad, 'Up')     # Flecha arriba aumenta la gravedad
onkey(menos_gravedad, 'Down') # Flecha abajo disminuye la gravedad
move()
done()
