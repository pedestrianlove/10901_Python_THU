# 1. Projectile Motion

# function area
def isValid (h, v):
	if h > 0 and v > 0:
		return True
	return False
def getInput ():
	h = eval (input ("Enter the initial height of the ball: "))
	v = eval (input ("Enter the initial velocity of the ball: "))
	if isValid (h, v):
		return h, v
	else:
		print ("Input invalid, please try again.")
		return getInput ()

def height (h, v, t):
	return h + v * t - 16 * (t**2)
def maxHeight (h, v):
	return height (h, v, v / 32)
def groundTime (h, v):
	t = 0
	while height (h, v, t) > 0:
		t += 0.01
	return t


# driver code
init_height, init_velocity = getInput ()
print ("The maximum height of the ball is {:.2f} feet.".format (maxHeight (init_height, init_velocity)))
print ("The ball will hit the ground after approximately {:.2f} seconds.".format (groundTime (init_height, init_velocity)))



