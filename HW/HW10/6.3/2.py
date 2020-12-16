import turtle


# title
turtle.title ("2.py")

# draw a blue horizontal line
turtle.color ("blue")
turtle.forward (100)

# draw a red dot (diameter 100 pixel)
turtle.color ("red")
turtle.fillcolor ("red")
turtle.speed (0)
turtle.begin_fill ()
## draw circle (not filled)
length = 370
x = 0
while x <= length:
	turtle.right (1)
	turtle.forward (0.88)
	x += 1

## fill the red circle
turtle.end_fill ()
turtle.hideturtle ()

# pause
input ("Press enter to continue...")
