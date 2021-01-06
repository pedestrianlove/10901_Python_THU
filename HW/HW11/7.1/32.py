class Quizzes:
	def __init__ (self):
		self.grade = []
		for i in range (6):
			tmp = eval (input ("Enter grade on quiz {:d}: ".format (i+1)))
			self.grade.append (tmp)

	def average (self):
		mini = min (self.grade)
		grade.remove (mini)
		return sum (self.grade) / len (self.grade)
	
	def __str__ (self):
		return "Quiz average: {:.1f}".format (self.average ())

# driver code
quiz = Quizzes ()
print (quiz)

