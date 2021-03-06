"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from random import choice, randint
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
c = randint(0,4)
cs = randint(0,4)

if c == 0:
    color = 'blue'
elif c == 1:
    color = 'cyan'
elif c == 2:
    color = 'green'
elif c == 3:
    color = 'aqua'
elif c == 4:
    color = 'fuchsia'

if cs == 0:
    colors = 'blue'
elif cs == 1:
    colors = 'cyan'
elif cs == 2:
    colors = 'green'
elif cs == 3:
    colors = 'aqua'
elif cs == 4:
    colors = 'fuchsia'

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colors)
    
    square(food.x, food.y, 9, color)
    update()
    ontimer(move, 100)

    if (-200 < food.x < 190 and -200 < food.y < 190):
        food.x = food.x + randrange(-1, 1) * 10
        food.y = food.y + randrange(-1, 1) * 10
    else:
        food.x = randrange(-1, 1) * 10
        food.y = randrange(-1, 1) * 10

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
