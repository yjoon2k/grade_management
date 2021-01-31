from tkinter import *
from functools import partial
import matplotlib.pyplot as plt
import numpy as np

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
    top_label.config(text=i.name+"학생의 성적그래프")
    x = np.arange(len(i.score))
    cnt = []
    for j in range(1, len(i.score) + 1):
        cnt.append(j)
    
    plt.bar(x, i.score)
    plt.xticks(x, cnt)
    plt.show()
    
    

root = Tk()
root.title("GUI test")
root.geometry("540x380+200+100")
st_1 = []
st_2 = []
st_3 = []
st_3.append(Student("홍길동", 3))
st_3[0].add_score(30)
st_3[0].add_score(40)
st_3[0].add_score(50)
st_3[0].add_score(60)
st_3[0].add_score(70)
st_3.append(Student("김철수", 3))
st_3[1].add_score(80)
st_3[1].add_score(30)
st_3[1].add_score(20)
st_3[1].add_score(100)
st_3[1].add_score(95)
st_3.append(Student("이영희", 3))
st_3.append(Student("가나다", 3))
st_3.append(Student("라마바", 3))
st_3.append(Student("사아자", 3))


frame_grade = LabelFrame(root, relief = "solid", bd = 1)
frame_grade.pack(side="left")
Button(frame_grade, text = "1학년", command = grade_pick_1).pack()
Button(frame_grade, text = "2학년", command = grade_pick_2).pack()
Button(frame_grade, text = "3학년", command = grade_pick_3).pack()

top_label = Label(root, text="성적관리프로그램")
top_label.pack(side="top")

frame_student_1 = LabelFrame(root, text = "1학년")
Button(frame_student_1, text = "1학년_누구누구1").pack()
Button(frame_student_1, text = "1학년_누구누구2").pack()
Button(frame_student_1, text = "1학년_누구누구3").pack()
frame_student_2 = LabelFrame(root, text = "2학년")
Button(frame_student_2, text = "2학년_누구누구1").pack()
Button(frame_student_2, text = "2학년_누구누구2").pack()
Button(frame_student_2, text = "2학년_누구누구3").pack()

frame_student_1.pack(side="right")

frame_student_3 = LabelFrame(root, text = "3학년")
for i in st_3:
    Button(frame_student_3, text = i.name, command = partial(printscore,i)).pack()




root.mainloop()