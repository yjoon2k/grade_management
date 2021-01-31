from tkinter import *
import matplotlib.pylot as plt
import numpy as np

class Student:
    score = []
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def add_grade(self, grade):
        self.score.append(grade)


def grade_pick_1():
    frame_student_2.pack_forget()
    frame_student_3.pack_forget()
    frame_student_1.pack(side="right")

def grade_pick_2():
    frame_student_1.pack_forget()
    frame_student_3.pack_forget()
    frame_student_2.pack(side="right")

def grade_pick_3():
    frame_student_2.pack_forget()
    frame_student_1.pack_forget()
    frame_student_3.pack(side="right")

root = Tk()
root.title("GUI test")
root.geometry("540x380+200+100")
st_1 = []
st_2 = []
st_3 = []


frame_grade = LabelFrame(root, relief = "solid", bd = 1)
frame_grade.pack(side="left")
Button(frame_grade, text = "1학년", command = grade_pick_1).pack()
Button(frame_grade, text = "2학년", command = grade_pick_2).pack()
Button(frame_grade, text = "3학년", command = grade_pick_3).pack()

frame_student_1 = LabelFrame(root, text = "1학년")
Button(frame_student_1, text = "1학년_누구누구1").pack()
Button(frame_student_1, text = "1학년_누구누구2").pack()
Button(frame_student_1, text = "1학년_누구누구3").pack()
frame_student_2 = LabelFrame(root, text = "2학년")
Button(frame_student_2, text = "2학년_누구누구1").pack()
Button(frame_student_2, text = "2학년_누구누구2").pack()
Button(frame_student_2, text = "2학년_누구누구3").pack()
frame_student_3 = LabelFrame(root, text = "3학년")
Button(frame_student_3, text = "3학년_누구누구1").pack()
Button(frame_student_3, text = "3학년_누구누구2").pack()
Button(frame_student_3, text = "3학년_누구누구3").pack()




root.mainloop()