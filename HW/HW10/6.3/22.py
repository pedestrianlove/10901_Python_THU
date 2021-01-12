import turtle

# title
turtle.title ("22.py")
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
orig = length (180, 270)
center = point (0, 0)
size = length (orig.h / 3, 270)
center.y += size.h
drawRectangle (pen, center, size, "orange", filled=1)
center.y -= 2*size.h
drawRectangle (pen, center, size, "black", filled=1)
center.y += size.h
drawRectangle (pen, center, orig, "black")

move (pen, 0, 0)
pen.dot (30, "orange")






# pause
turtle.hideturtle ()
input ("Press enter to continue...")
