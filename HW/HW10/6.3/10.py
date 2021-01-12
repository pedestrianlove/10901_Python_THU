import turtle


# title
turtle.title ("10.py")

# draw 1 square and 1 dot centered at (0, 0)
turtle.penup ()
turtle.goto (150, 150)
turtle.pendown ()

# draw a square
turtle.begin_fill ()
turtle.color ("yellow")
for i in range (4):
	turtle.right (90)
	turtle.forward (300)
turtle.end_fill ()

# draw a dot at center
turtle.penup ()
turtle.goto (0, 0)
turtle.pendown ()
turtle.dot (300, "black")










# pause
turtle.hideturtle ()
input ("Press enter to continue...")
