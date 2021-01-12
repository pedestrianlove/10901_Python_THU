import turtle

def drawRectangle (t, x, y, w, h, colorP = "black"):
	## Draw a rectangle with bottom-left corner (x, y)
	## width w, height h, pencolor colorP
	t .pencolor (colorP)
	t.up ()
	t.goto (x, y)
	t.down ()
	t.goto (x + w, y)
	t.goto (x + w, y + h)
	t.goto (x + w, y + h)
	t.goto (x, y + h)
	t.goto (x, y)
	t.end_fill ()

def drawRectangle2 (t, x, y, w, h, colorP = 'black'):
	t.pencolor (colorP)
	t.up ()
	t.goto (x, y)
	t.down ()
	for i in range (2):
		t.forward (w)
		t.left (90)
		t.forward (h)

def drawFivePointStar (t, x, y, lengthOfSide):
	t.up ()
	t.goto (x, y)
	t.left (36)
	t.down ()
	for i in range (5):
		t.forward (lengthOfSide)
		t.left (144)



# driver code
t = turtle.Turtle ()
#t.hideturtle ()
#drawRectangle (t, 0, 0, 100, 150, 'red')
#t.hideturtle ()
#drawRectangle2 (t, 0, 0, 100, 150, 'red')
t.hideturtle ()
lengthOfSide = 400
drawFivePointStar (t, -200, -200, lengthOfSide)
