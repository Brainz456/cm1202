from tkinter import *

class FinalProgram(Tk):

	def __init__(self, *args, **kwargs):

		Tk.__init__(self)
		#icon and program name
		Tk.iconbitmap(self, default = 'CardiffUniIcon.ico')
		Tk.wm_title(self, 'DQS Program')

		#creates a container that contains all the frames
		container = Frame(self)
		container.pack(side = 'top', fill = 'both', expand = True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		#creates a menu at the top of the window
		menubar = Menu(container)
		lessonmenu = Menu(menubar, tearoff = 0)
		lessonmenu.add_command(label="Maths Lesson", command = lambda: self.show_frame(viewMathsLesson))
		lessonmenu.add_command(label="Architecture Lesson", command = lambda: self.show_frame(viewArchitectureLesson))
		menubar.add_cascade(label = "Lessons", menu = lessonmenu)
		testmenu = Menu(menubar, tearoff = 0)
		testmenu.add_command(label = 'Maths Test', command = lambda: self.show_frame(viewMathsTest))
		testmenu.add_command(label = 'Architecture Test', command = lambda: self.show_frame(viewArchitectureTest))
		menubar.add_cascade(label = 'Tests', menu = testmenu)
		menubar.add_command(label = "Log out", command = quit)
		Tk.config(self, menu = menubar)
		
		#a dictonary of all the frames used in the program		
		self.frames = { }

		#goes through each frame in the dictonary, selecting the current frame and bringing it at the front 
		for F in (MenuPage, LessonSelection, TestSelection, viewMathsLesson, viewArchitectureLesson, viewMathsTest, viewArchitectureTest):
			frame = F(container,self)
			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky = 'nsew')

		#showing current frame
		self.show_frame(MenuPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

#creating the main menu page
class MenuPage(Frame):
	
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.grid()
	
		lblMenu = Label(self, text = 'Menu', font= ('MS', 40))
		lblMenu.pack(anchor=CENTER, pady=(20, 0))

		butLessons = Button(self, text = "Lessons", font= ('MS', 20), 
			command = lambda: controller.show_frame(LessonSelection))
		butLessons.pack(anchor=CENTER, pady=(50,20))

		butTests = Button(self, text = "Tests", font= ('MS', 20),
			command = lambda: controller.show_frame(TestSelection))
		butTests.pack(anchor=CENTER, pady=(20,50))

#creating the lesson selection page
class LessonSelection(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.grid()
		
		lblLesson = Label(self, text = 'Choose a lesson:', font= ('MS', 40))
		lblLesson.pack(anchor=CENTER, pady=(20, 0))

		butMathsLesson = Button(self, text ='Maths', font= ('MS', 20),
			command = lambda: controller.show_frame(viewMathsLesson))
		butMathsLesson.pack(anchor=CENTER, pady=(50,20))

		butArchitectureLesson = Button(self, text ='Architecture', font= ('MS', 20),
			command = lambda: controller.show_frame(viewArchitectureLesson))
		butArchitectureLesson.pack(anchor=CENTER, pady=(20,50))

		butReturn = Button(self, text ='Return to Main Menu', font= ('MS', 10),
			command = lambda: controller.show_frame(MenuPage))
		butReturn.pack(anchor=NW, pady=(50,50))
#creating the test selection page
class TestSelection(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.grid()
		
		lblTest = Label(self, text = 'Choose a test:', font= ('MS', 40))
		lblTest.pack(anchor=CENTER, pady=(20, 0))

		butMathsTest = Button(self, text ='Maths', font= ('MS', 20),
			command = lambda: controller.show_frame(viewMathsTest))
		butMathsTest.pack(anchor=CENTER, pady=(50,20))

		butArchitectureTest = Button(self, text ='Architecture', font= ('MS', 20),
			command = lambda: controller.show_frame(viewArchitectureTest))
		butArchitectureTest.pack(anchor=CENTER, pady=(20,50))

		butReturn = Button(self, text ='Return to Main Menu', font= ('MS', 10),
			command = lambda: controller.show_frame(MenuPage))
		butReturn.pack(anchor=CENTER, pady=(50,50))


class viewMathsLesson(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.grid()
		
		lblOutput = Label(self, text = 'it will go to the maths lesson page', font = ('MS', 25))
		lblOutput.grid(row=1, column = 7)

		butReturn = Button(self, text ='Return to Main Menu', font= ('MS', 10),
			command = lambda: controller.show_frame(MenuPage))
		butReturn.grid(row=4, column = 7)

	
class viewArchitectureLesson(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.grid()

		lblOutput = Label(self, text = 'it will go to the architecture lesson page', font = ('MS', 25))
		lblOutput.grid(row=1, column = 7)

		butReturn = Button(self, text ='Return to Main Menu', font= ('MS', 10),
			command = lambda: controller.show_frame(MenuPage))
		butReturn.grid(row=4, column = 7)

class viewMathsTest(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.grid()

		lblOutput = Label(self, text = 'it will go to the maths test page', font = ('MS', 25))
		lblOutput.grid(row=1, column = 7)

		butReturn = Button(self, text ='Return to Main Menu', font= ('MS', 10),
			command = lambda: controller.show_frame(MenuPage))
		butReturn.grid(row=4, column = 7)

class viewArchitectureTest(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.grid()

		lblOutput = Label(self, text = 'it will go to the architecture test page', font = ('MS', 25))
		lblOutput.grid(row=1, column = 7)

		butReturn = Button(self, text ='Return to Main Menu', font= ('MS', 10),
			command = lambda: controller.show_frame(MenuPage))
		butReturn.grid(row=4, column = 7)

root = Tk()
root.withdraw()

#fixed window dementions 
app = FinalProgram(root)
app.resizable(width=FALSE, height=FALSE)
app.geometry("800x800")

status_bar = Label(app, text="Logged in as ....", bd=1, relief=SUNKEN, anchor=W)
status_bar.pack(side=BOTTOM, fill=X)

root.mainloop()