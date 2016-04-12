class test:
    def __init__(self,TestID,Topic,Questions):
		
      #Variables need assigning temp values in place
      self.testID = str(TestID)
      self.questions = Questions
      self.topic = Topic
    def __str__(self):
        return "TestID: %s, Topic: %s" % (self.testID, self.topic)
    def Get_Questions(QuestionID):
        #form
        pass
    def Store_answers(StudentID, Results):
        #Store list
        pass
    def Check_Answers(Answers, CorrectAnswers):
        return      #Return Boolean

    def Create_Question(QuestionAsked, PossibleAnswers, CorrectAnswer):# ISNT WORKING, DONT KNOW WHY
        with open("data/questions.txt","a+") as file:
            temp = str()
            for line in file:
                temp = temp + line
            print(temp)
            num_questions = temp.count("\n") + 1
            temp = str(temp)
            num_questions = str(num_questions)
            written = str(temp + "Q" + num_questions + ";" + QuestionAsked + ";" + PossibleAnswers + ";" + CorrectAnswer + "\n")
            file.write(written)
            temp = str()
            
    def Add_Question(self,QuestionID):# THIS WORKS
        self.questions.append(QuestionID)
        print("Question",QuestionID,"added to test.") 