import turtle


# title
turtle.title ("20.py")


# draw text
colors = ["red", "blue", "black", "purple", "orange", "brown"]
text = "Python"

for i in range (len (text)):
	turtle.color (colors[i])
	turtle.write (text[i], font=("Source Code Pro",72,"normal"))
	turtle.penup ()
	turtle.forward (60)
	turtle.pendown ()



# pause
turtle.hideturtle ()
input ("Press enter to continue...")
