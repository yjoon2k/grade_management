from tkinter import *
from functools import partial
#import matplotlib.pylot as plt
#import numpy as np

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.score = []
    
    def add_score(self, score):
        self.score.append(score)


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

def printscore(i):
    for j in i.score:
        print(j)
    

root = Tk()
root.title("GUI test")
root.geometry("540x380+200+100")
st_1 = []
st_2 = []
st_3 = []
st_3.append(Student("김승태", 3))
st_3[0].add_score(30)
st_3.append(Student("배상준", 3))
st_3[1].add_score(40)
st_3.append(Student("신재연", 3))
st_3[2].add_score(50)
st_3.append(Student("임주원", 3))
st_3[3].add_score(60)
st_3.append(Student("최나영", 3))
st_3[4].add_score(70)
st_3.append(Student("최다연", 3))
st_3[5].add_score(80)


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
for i in st_3:
    Button(frame_student_3, text = i.name, command = partial(printscore,i)).pack()




root.mainloop()