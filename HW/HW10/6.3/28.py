import turtle

# title
turtle.title ("28.py")
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




# data list
val = [753, 172, 70]
desc = ["Public (not charter or magnet)", "Private", "Other"]
font_offset = 0
# driver code
pen.pensize (2)
move (pen, 0, -480)
pen.write ("Type of High School Attended by Fall 2013 College Freshman", font=("Source Code Pro", 12,"normal"))
move (pen, 0, 0)

for i in range (3):
	# draw bar
	orig = length (val[i], 150)
	center = point (150 * i, -400)
	drawBar (pen, center, orig, "sky blue", filled = 1)
	# handle text
	font_offset += 20
	move (pen, center.x, center.y - font_offset)
	pen.color ("black")
	pen.write (desc[i], font=("Source Code Pro", 9,"normal"))
	move (pen, center.x, center.y + font_offset)

	# handle value on top
	move (pen, center.x, center.y + val[i])
	pen.write ("{:.1f}%".format (val[i] / 10), font=("Source Code Pro", 14, "normal"))
	move (pen, center.x, center.y - val[i])






# pause
turtle.hideturtle ()
input ("Press enter to continue...")
