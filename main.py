from ufo import *
import turtle as tr
from random import randint

tr.screensize(700, 700)
tr.tracer(5)
tr.hideturtle()

for cd in range(20, 200):
    a = randint(-1, 1)
    x = cd * a
    a = randint(-1, 1)
    y = cd * a
    ufo1 = Ufo('UFO', x, y, 150, 'green', 6, 5)
    ufo1.show()
    tr.clear()


tr.update()