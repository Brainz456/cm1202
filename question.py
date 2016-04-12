class question:
	def __init__(self, QuestionID, QuestionAsked, PossibleAnswers, CorrectAnswer):
         self.questionID = str(QuestionID)
         self.questionAsked = QuestionAsked
         self.possibleAnswers = PossibleAnswers
         self.correctAnswer = str(CorrectAnswer)
	def __str__(self):
         return "QuestionID: %s, Question: %s, Possible Answers: %s, Correct Answer: %s" % (self.questionID,self.questionAsked, self.possibleAnswers,self.correctAnswer)
	
