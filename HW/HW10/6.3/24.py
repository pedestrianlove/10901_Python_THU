import turtle

# title
turtle.title ("24.py")
pen = turtle.Turtle ()

class point:
	def __init__ (self, x, y):
		self.x = x
		self.y = y
class length:
	def __init__ (self, height, width):
		self.h = height
		self.w = width

def move (man, x, y):
	man.penup ()
	man.goto (x, y)
	man.pendown ()

def drawRectangle (pants, center, lengths, color, filled = 0):
	move (pants, center.x + lengths.w / 2, center.y + lengths.h / 2)
	
	if (filled == 1):
		pants.begin_fill ()
	pants.color (color)
	pants.pensize (3)
	pants.goto (center.x + lengths.w / 2, center.y - lengths.h / 2)
	pants.goto (center.x - lengths.w / 2, center.y - lengths.h / 2)
	pants.goto (center.x - lengths.w / 2, center.y + lengths.h / 2)
	pants.goto (center.x + lengths.w / 2, center.y + lengths.h / 2)
	if (filled == 1):
		pants.end_fill ()
	pants.hideturtle ()
	


# driver code
orig = length (500, 500)
center = point (0, 0)
drawRectangle (pen, center, orig, "red", filled=1)
orig.h, orig.w = 100, 100
drawRectangle (pen, center, orig, "white", filled=1)
center.x += orig.h
drawRectangle (pen, center, orig, "white", filled=1)
center.x -= 2*orig.h
drawRectangle (pen, center, orig, "white", filled=1)
center.x += orig.h
center.y += orig.h
drawRectangle (pen, center, orig, "white", filled=1)
center.y -= 2*orig.h
drawRectangle (pen, center, orig, "white", filled=1)







# pause
turtle.hideturtle ()
input ("Press enter to continue...")
