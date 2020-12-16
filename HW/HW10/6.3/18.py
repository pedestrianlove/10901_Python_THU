import turtle


# title
turtle.title ("18.py")


# draw shapes
turtle.begin_fill ()
turtle.pensize (5)
turtle.color ("black")
turtle.goto (250, 0)
turtle.goto (250, 105)
turtle.goto (-250, 105)
turtle.goto (-250, 0)
turtle.goto (0, 0)

turtle.color ("yellow")
turtle.end_fill ()


# draw text
turtle.penup ()
turtle.goto (0, 0)
turtle.pendown ()
turtle.color ("red")
turtle.write ("PYTHON", align="center", font=("Source Code Pro",72,"normal"))



# pause
turtle.hideturtle ()
input ("Press enter to continue...")
