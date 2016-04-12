from question import question
from test import test
from module import module
#from lecturer import lecturer
#from student import student
from lesson import lesson
listOfQuestions = []
listOfTests = []
listOfModules = []
listOfLecturers = []
listOfStudents = []
listOfLessons = []

with open("data/questions.txt") as questionsText:
    temp = []
    for line in questionsText:
        x = []
        x = line.split(";")
        x[3] = x[3].rstrip()
        temp.append(x)
    for questions in temp:
        y = question(questions[0],questions[1],questions[2],questions[3])
        listOfQuestions.append(y)
for questions in listOfQuestions:
    print(questions)
print(listOfQuestions)
with open("data/tests.txt") as testsText:
    temp = []
    for line in testsText:
        x = []
        x = line.split(";")
        x[3] = x[3].rstrip()
        temp.append(x)
    for tests in temp:
        y = test(tests[0],tests[1],tests[2],tests[3])
        listOfTests.append(y)
        
with open("data/modules.txt") as modulesText:
    temp = []
    for line in modulesText:
        x = []
        x = line.split(";")
        x[3] = x[3].rstrip()
        temp.append(x)
    for modules in temp:
        y = module(modules[0],modules[1],modules[2],modules[3])
        listOfModules.append(y) 
        
"""with open("data/lecturers.txt") as lecturersText:
    temp = []
    for line in lecturersText:
        x = []
        x = line.split(";")
        x[3] = x[3].rstrip()
        temp.append(x)
    for lecturers in temp:
        y = lecturer(lecturers[0],lecturers[1],lecturers[2],lecturers[3])
        listOfQuestions.append(y)"""
        
"""with open("data/students.txt") as studentsText:
    temp = []
    for line in studentsText:
        x = []
        x = line.split(";")
        x[3] = x[3].rstrip()
        temp.append(x)
    for students in temp:
        y = student(students[0],students[1],students[2],students[3])
        listOfStudents.append(y)
"""
with open("data/lessons.txt") as lessonsText:
    temp = []
    for line in lessonsText:
        x = []
        x = line.split(";")
        x[3] = x[3].rstrip()
        temp.append(x)
    for lessons in temp:
        y = lesson(lessons[0],lessons[1],lessons[2],lessons[3])
        listOfQuestions.append(y)