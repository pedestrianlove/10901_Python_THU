import turtle


# title
turtle.title ("8.py")

# draw a square of length 80 centered at (0, 0) (red edge and filled with orange)
## draw border
turtle.pensize (2)
turtle.color ("red")
for i in range (3):
	turtle.forward (100)
	turtle.left (120)

turtle.hideturtle ()


# pause
input ("Press enter to continue...")
