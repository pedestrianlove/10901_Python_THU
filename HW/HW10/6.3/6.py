import turtle


# title
turtle.title ("6.py")

# move turtle pen
turtle.penup ()
turtle.goto (40, 40)
turtle.pendown ()

# draw a square of length 80 centered at (0, 0) (red edge and filled with orange)
turtle.fillcolor ("orange")
turtle.begin_fill ()
## draw border
turtle.pensize (2)
turtle.color ("red")
turtle.goto (40, -40)
turtle.goto (-40, -40)
turtle.goto (-40, 40)
turtle.goto (40, 40)

# fill in color
turtle.color ("orange")
turtle.end_fill ()
turtle.hideturtle ()


# pause
input ("Press enter to continue...")
