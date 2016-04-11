class test:
    def __init__(self,TestID,Topic):
		
      #Variables need assigning temp values in place
      self.testID = int(TestID)
      self.questions = []
      self.topic = Topic
    def __str__(self):
        return "TestID: %d, Topic: %s" % (self.testID, self.topic)
    def Get_Questions(QuestionID):
        #form
        pass
    def Store_answers(StudentID, Results):
        #Store list
        pass
    def Check_Answers(Answers, CorrectAnswers):
        return      #Return Boolean

    def Create_Questions(Input):
        pass
    
    def Add_Question(self,QuestionID):
        self.questions.append(QuestionID)