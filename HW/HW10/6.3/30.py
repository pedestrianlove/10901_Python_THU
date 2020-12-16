import turtle

# title
turtle.title ("30.py")
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
	
def drawBar (pants, center, lengths, color, filled = 0):
	move (pants, center.x, center.y)
	
	if (filled == 1):
		pants.begin_fill ()
	pants.color ("black")
	#pants.pensize (3)
	pants.goto (center.x + lengths.w, center.y)
	pants.goto (center.x + lengths.w, center.y + lengths.h)
	pants.goto (center.x, center.y + lengths.h)
	pants.goto (center.x, center.y)
	pants.color (color)
	if (filled == 1):
		pants.end_fill ()
	pants.hideturtle ()

def drawLineChart (pen, )


# data list
val = [[[1978, 59], [1988, 74], [1998, 73], [2008, 77]], [[1978, 60], [1988, 43], [1998, 44], [2008, 51]]]
desc = ["well off financially", "meaningful philosophy of life"]
# driver code

for i in range (2):
	# draw line






# pause
turtle.hideturtle ()
input ("Press enter to continue...")
