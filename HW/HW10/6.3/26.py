import turtle

# title
turtle.title ("26.py")
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

def drawStar (man, center, lengths, color, filled = 0):
	move (man, center.x, center.y)
	man.color (color)
	man.fillcolor (color)
	if (filled == 1):
		man.begin_fill ()
	for i in range (5):
		man.forward (40)
		man.right (180 - 36)
	if (filled == 1):
		man.end_fill ()


def drawRectangle (pants, center, lengths, color, filled = 0):
	move (pants, center.x + lengths.w / 2, center.y + lengths.h / 2)
	
	if (filled == 1):
		pants.begin_fill ()
	pants.color (color)
	#pants.pensize (3)
	pants.goto (center.x + lengths.w / 2, center.y - lengths.h / 2)
	pants.goto (center.x - lengths.w / 2, center.y - lengths.h / 2)
	pants.goto (center.x - lengths.w / 2, center.y + lengths.h / 2)
	pants.goto (center.x + lengths.w / 2, center.y + lengths.h / 2)
	if (filled == 1):
		pants.end_fill ()
	pants.hideturtle ()
	


# driver code
orig = length (200, 300)
center = point (0, 0)
pen.pensize (2)
drawRectangle (pen, center, orig, "black", filled=0)
orig.h, orig.w = 100, 150
pen.pensize (1)
center.x, center.y = center.x - orig.w/2, center.y - orig.h/2
drawRectangle (pen, center, orig, "black", filled=1)
center.x, center.y = center.x + orig.w, center.y + orig.h
drawRectangle (pen, center, orig, "red", filled=1)
center.x, center.y = center.x - orig.w - 20, center.y
drawStar (pen, center, orig, "black", filled=1)
move (pen, center.x + 20, center.y - 6.5)
pen.dot (15, "black")
center.x, center.y = center.x + orig.w , center.y - orig.h
drawStar (pen, center, 30, "red", filled=1)
move (pen, center.x + 20, center.y - 6.5)
pen.dot (15, "red")







# pause
turtle.hideturtle ()
input ("Press enter to continue...")
