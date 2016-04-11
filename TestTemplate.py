#Basic template to work off for the front page Tkinter

from tkinter import *

def run_lesson():
    print("run lesson code")

def run_test():
    print("run Test code")

def return_to_menu():
    print("run Menu code")


#Code to generate initial screen--------------------------------------------------------
root = Tk()
root.resizable(width=FALSE, height=FALSE)
root.geometry("800x800")

Module = Label(root, text="Module", font=("-weight bold", 28))
logo = PhotoImage(file="CardiffUniLogo.png")
Logo_Label = Label(root, image=logo)

lesson_Button = Button(root, text = "Lesson", font=("", 16),  command=run_lesson)
test_button = Button(root, text = "Test", font=("", 16), command=run_test)
main_menu = Button(root, text = "Return to Main Menu", font=("", 16), command=return_to_menu)

Logo_Label.place(x=685, y=5)

Module.pack(anchor=CENTER, pady=(20, 0))
lesson_Button.pack(anchor=CENTER, pady=(50,20))
test_button.pack(anchor=CENTER, pady=(20,50))
main_menu.pack(anchor=CENTER, pady=(50,50))

status_bar = Label(root, text="Logged in as ....", bd=1, relief=SUNKEN, anchor=W)

status_bar.pack(side=BOTTOM, fill=X)

root.mainloop()
