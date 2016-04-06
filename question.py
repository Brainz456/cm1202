class question(object):
	def __init__(self, QuestionID, PossibleAnswers, CorrectAnswer):
		self.QuestionID = int(QuestionID)
		self.PossibleAnswers = PossibleAnswers
		self.CorrectAnswer = str(CorrectAnswer)
	
	def get_ID(self):
		return self.QuestionID
	
	def get_PossibleAnswers(self):
		return self.PossibleAnswers
	
	def get_CorrectAnswer(self):
		return self.CorrectAnswer
