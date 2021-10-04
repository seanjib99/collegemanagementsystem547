from tkinter import *
from tkinter import  messagebox
from PIL import Image, ImageTk
from tkinter import ttk



class Course:
    def __init__(self,project):
        self.project=project
        self.project.title("Courses")
        self.project.geometry("1300x498+0+280")
        self.project.focus_force()

        self.coursename=StringVar()
        self.duration=StringVar()
        self.coursecredit = StringVar()
        self.charges = StringVar()
        self.coursehead = StringVar()
        self.description = StringVar()
        self.courseid = StringVar()

        #>>>>>>>>>>>>>>>>> Title >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        title = Label(self.project, text="Course", compound=LEFT,font=("goudy old style", 30, "bold"), bg="#363e45", fg="Yellow")
        title.place(x=0, y=0, relwidth=1, height=50)

        #>>>>>>>>>>>>>>>>>>>>>>>Subtitle and Button <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        course_name_label=Label(self.project,text="Course Name",font=("goudy old style",15,"bold"),fg="#7307f7")
        course_name_label.place(x=0,y=80)

        self.cname=Entry(self.project,textvar=self.coursename, font=("goudy old style", 15, "bold"), bg="white").place(x=130, y=83)

        duration_name_label = Label(self.project, text="Duration", font=("goudy old style", 15, "bold"), fg="#7307f7")
        duration_name_label.place(x=0, y=120)

        self.duration_entry = Entry(self.project,textvar=self.duration, font=("goudy old style", 15, "bold"), bg="white").place(x=130, y=120)



if __name__=="__main__":
    tk=Tk()
    obj=Course(tk)
    tk.mainloop()