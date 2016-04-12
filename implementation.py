from tkinter import *

class FinalProgram(Tk):

	def __init__(self, *args, **kwargs):
		Tk.__init__(self)
		container = Frame(self)

		container.pack(side = 'top', fill = 'both', expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		menubar = Menu(container)
		lessonmenu = Menu(menubar, tearoff = 0)
		lessonmenu.add_command(label="Maths", command = viewMathsLesson)
		menubar.add_cascade(label = "Lessons", menu = lessonmenu)
		menubar.add_command(label = "Log out", command = root.quit)
		Tk.config(self, menu = menubar)

		menubar = Menu(container)
		filemenu = Menu(menubar, tearoff = 0)

		self.frames = { }

		for F in (MenuPage, LessonSelection, TestSelection, viewMathsLesson, viewArchitectureLesson, viewMathsTest, viewArchitectureTest):
			frame = F(container,self)
			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky = 'nsew')

		self.show_frame(MenuPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

class MenuPage(Frame):
	
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.grid()
	
		lblMenu = Label(self, text = 'Menu', font= ('MS', 25, 'bold'))
		lblMenu.grid(row=3, column=7,sticky = NE)

		butLessons = Button(self, text = "Lessons", font= ('MS', 25), 
			command = lambda: controller.show_frame(LessonSelection))
		butLessons.grid(row=4, column = 7)

		butTests = Button(self, text = "Tests", font= ('MS', 25),
			command = lambda: controller.show_frame(TestSelection))
		butTests.grid(row=5, column = 7)

	def view2Lessons(self):
		print("2 lessons")

	def view2Tests(self):
		print("2tests")

class LessonSelection(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.grid()
		
		lblLesson = Label(self, text = 'Choose a lesson:', font= ('MS', 25, 'bold'))
		lblLesson.grid(row=1, column=7,sticky = NE)

		butMathsLesson = Button(self, text ='Maths', font= ('MS', 25),
			command = lambda: controller.show_frame(viewMathsLesson))
		butMathsLesson.grid(row=2, column = 7)

		butArchitectureLesson = Button(self, text ='Architecture', font= ('MS', 25),
			command = lambda: controller.show_frame(viewArchitectureLesson))
		butArchitectureLesson.grid(row=3, column = 7)

		butReturn = Button(self, text ='Return to Main Menu', font= ('MS', 25),
			command = lambda: controller.show_frame(MenuPage))
		butReturn.grid(row=4, column = 7)

class TestSelection(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.grid()
		
		lblTest = Label(self, text = 'Choose a test:', font= ('MS', 25, 'bold'))
		lblTest.grid(row=1, column=7,sticky = NE)

		butMathsTest = Button(self, text ='Maths', font= ('MS', 25),
			command = lambda: controller.show_frame(viewMathsTest))
		butMathsTest.grid(row=2, column = 7)

		butArchitectureTest = Button(self, text ='Architecture', font= ('MS', 25),
			command = lambda: controller.show_frame(viewArchitectureTest))
		butArchitectureTest.grid(row=3, column = 7)

		butReturn = Button(self, text ='Return to Main Menu', font= ('MS', 25),
			command = lambda: controller.show_frame(MenuPage))
		butReturn.grid(row=4, column = 7)


class viewMathsLesson(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.grid()
		
		lblOutput = Label(self, text = 'it will go to the maths lesson page', font = ('MS', 25))
		lblOutput.grid(row=1, column = 7)

		butReturn = Button(self, text ='Return to Main Menu', font= ('MS', 25),
			command = lambda: controller.show_frame(MenuPage))
		butReturn.grid(row=4, column = 7)

	
class viewArchitectureLesson(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.grid()

		lblOutput = Label(self, text = 'it will go to the architecture lesson page', font = ('MS', 25))
		lblOutput.grid(row=1, column = 7)

		butReturn = Button(self, text ='Return to Main Menu', font= ('MS', 25),
			command = lambda: controller.show_frame(MenuPage))
		butReturn.grid(row=4, column = 7)

class viewMathsTest(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.grid()

		lblOutput = Label(self, text = 'it will go to the maths test page', font = ('MS', 25))
		lblOutput.grid(row=1, column = 7)

		butReturn = Button(self, text ='Return to Main Menu', font= ('MS', 25),
			command = lambda: controller.show_frame(MenuPage))
		butReturn.grid(row=4, column = 7)

class viewArchitectureTest(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.grid()

		lblOutput = Label(self, text = 'it will go to the architecture test page', font = ('MS', 25))
		lblOutput.grid(row=1, column = 7)

		butReturn = Button(self, text ='Return to Main Menu', font= ('MS', 25),
			command = lambda: controller.show_frame(MenuPage))
		butReturn.grid(row=4, column = 7)

root = Tk()
root.withdraw()
app = FinalProgram(root)
root.mainloop()