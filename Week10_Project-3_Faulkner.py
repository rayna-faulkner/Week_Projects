import turtle

def drawFractalLine(distance, angle, level):
    if level == 0:
        turtle.forward(distance)
    else:
        drawFractalLine(distance/3, angle, level-1)
        turtle.left(angle)
        drawFractalLine(distance/3, angle, level-1)
        turtle.right(angle*2)
        drawFractalLine(distance/3, angle, level-1)
        turtle.left(angle)
        drawFractalLine(distance/3, angle, level-1)

def drawKochSnowflake(size, level):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-size/2, -size/6)
    turtle.pendown()
    for _ in range(3):
        drawFractalLine(size, 60, level)
        turtle.right(120)

    turtle.hideturtle()
    turtle.done()

def main():
    size = 300
    level = 4
    drawKochSnowflake(size, level)

if __name__ == '__main__':
    main()
