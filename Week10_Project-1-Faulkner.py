from turtle import Turtle
import math

def drawCircle(t, x, y, r):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(120):
        t.forward((2 * math.pi * r) / 120)
        t.left(3)

def main():
    t = Turtle()
    x = 50
    y = 75
    radius = 100
    drawCircle(t, x, y, radius)

if __name__ == '__main__':
    main()
